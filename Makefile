.PHONY: help
$(VERBOSE).SILENT:

ifndef LOOP_RUNS:
LOOP_RUNS=10_000_000
endif

ifndef MAX_WORKERS:
MAX_WORKERS=4
endif

ifndef TASK_COUNT:
TASK_COUNT=4
endif

# Self-Documented Makefile
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^(\w|-)+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

run-concurrency-test:
	LOOP_RUNS=$(LOOP_RUNS) MAX_WORKERS=$(MAX_WORKERS) TASK_COUNT=$(TASK_COUNT) time python3 concurrency.py

run-parallelism-test:
	LOOP_RUNS=$(LOOP_RUNS) MAX_WORKERS=$(MAX_WORKERS) TASK_COUNT=$(TASK_COUNT) time python3 parallelism.py
