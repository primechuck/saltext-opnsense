CORE_REF ?= 26.7.3
PLUGINS_REF ?= 26.7.3

gen-spec:
	@mkdir -p src/saltext/opnsense/utils
	python3 tools/generate_spec.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --output src/saltext/opnsense/utils/controllers.json
	@jq .meta src/saltext/opnsense/utils/controllers.json 2>/dev/null || python3 -c "import json,pathlib; print(json.loads(pathlib.Path('src/saltext/opnsense/utils/controllers.json').read_text()).get('meta'))"

gen-models:
	@mkdir -p src/saltext/opnsense/utils
	@if [ -d /tmp/opnsense-spec/core ] && [ -d /tmp/opnsense-spec/plugins ]; then \
		echo "Using cached clones"; \
		python3 tools/generate_models.py --core /tmp/opnsense-spec/core --plugins /tmp/opnsense-spec/plugins --output src/saltext/opnsense/utils/models.json; \
	else \
		python3 tools/generate_models.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --output src/saltext/opnsense/utils/models.json; \
	fi
	@echo "Wrote src/saltext/opnsense/utils/models.json"

gen-wrappers:
	python3 tools/generate_wrappers.py

bump:
	python3 tools/generate_spec.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF) --output src/saltext/opnsense/utils/controllers.json
	python3 tools/generate_wrappers.py
	PYTHONPATH=src python3 tools/verify_import.py

verify:
	PYTHONPATH=src python3 tools/verify_import.py

test:
	pytest tests/unit -q --cov=src/saltext/opnsense --cov-report=term-missing --cov-fail-under=75

lint:
	ruff check src tests tools

docs:
	sphinx-build -b html docs docs/_build/html -W -n

gen-all:
	python3 tools/generate_all.py --core-ref $(CORE_REF) --plugins-ref $(PLUGINS_REF)

clean:
	rm -rf /tmp/opnsense-spec __pycache__ src/__pycache__ .pytest_cache .nox build dist *.egg-info src/*.egg-info
	rm -rf src/saltext/opnsense/__pycache__ src/saltext/opnsense/modules/__pycache__ src/saltext/opnsense/states/__pycache__ src/saltext/opnsense/utils/__pycache__
	rm -rf tests/__pycache__ tests/unit/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleaned caches. Generated wrappers/json kept."
