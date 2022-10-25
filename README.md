# Parallelism Vs. Concurrency in Python

Simple demonstrator for the difference between using processes and threads (parallel and concurrent, respectively) in Python.

## Running the tests
To run the concurrency test:
```sh
make run-concurrency-test
```

To run the parallelism test:
```sh
make run-parallelism-test
```

The important time to keep an eye on is labeled "real".

The task workload is determined by the number of iterations done, and can be set via the variable LOOP_RUNS in the Makefile. Similarly, the amount of tasks spawned is controlled by the variable TASK_COUNT, and the maximum amount of tasks allowed to run at the same time is controlled by the variable MAX_WORKERS.


