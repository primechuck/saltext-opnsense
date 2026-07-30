# Makefile for saltext-opnsense — maintainable codegen pipeline
# Single entrypoint: make gen-all (wraps tools/generate_all.py)
# See docs/MAINTENANCE.md for full sprint checklist

PYTHON ?= python3
CORE_REF ?= 25.7
PLUGINS_REF ?= 25.7
CORE ?= $(CORE_REF)
ARGS ?=
DRY ?=

TOOLS_DIR := tools
SRC_UTILS := src/saltext/opnsense/utils
SRC_JSON := $(SRC_UTILS)/controllers.json
SRC_MODELS_JSON := $(SRC_UTILS)/models.json

.PHONY: help gen-spec gen-models gen-wrappers bump sync verify test lint gen-all clean

help:
	@echo "saltext-opnsense maintenance"
	@echo ""
	@echo "Targets:"
	@echo "  gen-spec      - Clone core/plugins @ REF and parse controllers.php -> src/.../utils/controllers.json"
	@echo "  gen-models    - Parse Model XML -> src/.../utils/models.json"
	@echo "  gen-wrappers  - Spec -> 76 exec + 76 state wrappers (auto-generated)"
	@echo "  bump          - Upstream version sprint: make bump CORE=25.7"
	@echo "  sync          - Copy src -> extmods directories for gitfs file-based install"
	@echo "  verify        - Prove all 76 modules import (exec+state+dynamic)"
	@echo "  test          - pytest tests/unit -q"
	@echo "  lint          - ruff check src tests tools"
	@echo "  gen-all       - Full pipeline: spec -> wrappers -> sync -> verify -> test (via generate_all.py)"
	@echo "  clean         - Remove caches, /tmp/opnsense-spec, pycache"
	@echo ""
	@echo "Variables:"
	@echo "  CORE_REF, PLUGINS_REF (default 25.7) e.g. make gen-all CORE_REF=25.7 PLUGINS_REF=25.7"
	@echo "  CORE (alias for CORE_REF/PLUGINS_REF) e.g. make bump CORE=25.7"
	@echo ""
	@echo "Examples:"
	@echo "  make bump CORE=25.7"
	@echo "  make gen-all CORE_REF=25.7 PLUGINS_REF=25.7"
	@echo "  make gen-wrappers && make verify"

gen-spec:
	@mkdir -p $(SRC_UTILS)
	$(PYTHON) $(TOOLS_DIR)/generate_spec.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --output $(SRC_JSON)
	@jq .meta $(SRC_JSON) 2>/dev/null || python3 -c "import json,pathlib; print(json.loads(pathlib.Path('$(SRC_JSON)').read_text()).get('meta'))"

gen-models:
	@mkdir -p $(SRC_UTILS)
	@if [ -d /tmp/opnsense-spec/core ] && [ -d /tmp/opnsense-spec/plugins ]; then \
		echo "Using cached clones /tmp/opnsense-spec/core and /tmp/opnsense-spec/plugins"; \
		$(PYTHON) $(TOOLS_DIR)/generate_models.py --core /tmp/opnsense-spec/core --plugins /tmp/opnsense-spec/plugins --output $(SRC_MODELS_JSON); \
	else \
		$(PYTHON) $(TOOLS_DIR)/generate_models.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --output $(SRC_MODELS_JSON); \
	fi
	@echo "Wrote $(SRC_MODELS_JSON)"

gen-wrappers:
	$(PYTHON) $(TOOLS_DIR)/generate_wrappers.py

bump:
	$(PYTHON) $(TOOLS_DIR)/generate_spec.py --core-ref $(CORE) --plugins-ref $(CORE) --output $(SRC_JSON)
	cp $(SRC_JSON) $(TOOLS_DIR)/controllers.json
	$(PYTHON) $(TOOLS_DIR)/generate_wrappers.py
	PYTHONPATH=src $(PYTHON) $(TOOLS_DIR)/verify_import.py

sync:
	$(PYTHON) $(TOOLS_DIR)/sync_extmods.py --copy

verify:
	PYTHONPATH=src $(PYTHON) $(TOOLS_DIR)/verify_import.py

test:
	PYTHONPATH=src $(PYTHON) -m pytest tests/unit -q

lint:
	$(PYTHON) -m ruff check src tests tools || ruff check src tests tools

gen-all:
ifeq ($(DRY),1)
	$(PYTHON) $(TOOLS_DIR)/generate_all.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --dry-run $(ARGS)
else
	$(PYTHON) $(TOOLS_DIR)/generate_all.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) $(ARGS)
endif

clean:
	rm -rf /tmp/opnsense-spec tools/tmp __pycache__ src/__pycache__ .pytest_cache .nox build dist *.egg-info src/*.egg-info
	rm -rf src/saltext/opnsense/__pycache__ src/saltext/opnsense/modules/__pycache__ src/saltext/opnsense/states/__pycache__ src/saltext/opnsense/utils/__pycache__
	rm -rf src/saltext/opnsense/proxy/__pycache__ src/saltext/opnsense/grains/__pycache__ tests/__pycache__ tests/unit/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleaned caches. Generated wrappers/json kept."
