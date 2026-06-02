# 📈 System Performance: Empirical Benchmarking

Notes on measuring code execution speed, tracking resource constraints, and proving algorithmic complexity on physical runtimes.

## Core Metrics to Watch
* **Throughput:** The volume of transactions or operations a system can successfully process within a fixed window (e.g., Requests Per Second).
* **Latency:** The duration of time a single operation takes to complete from invocation to return, typically tracked via high-precision monotonic system timers (`time.perf_counter`).

## Algorithmic Reality Check
* **Theoretical $O(1)$ vs $O(n)$:** A custom hash table uses memory manipulation to jump straight to an index. A list lookup iterates sequentially. As data scales from 100 to 10,000 items, the list latency will spike linearly, while the hash table latency stays flat.
