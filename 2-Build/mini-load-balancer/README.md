# Custom TCP Load Balancer

A lightweight, concurrency-safe Layer 4 load balancer built from scratch using Python's `socket` and `threading` libraries.

## 🛠️ Features
* **Round Robin Scheduling:** Distributes incoming traffic sequentially across available targets.
* **Multi-threaded Core:** Spins up isolation threads to process concurrent requests seamlessly.

## 🚀 Execution
1. Run target backend servers on ports `8081` and `8082`.
2. Spin up the load balancer: `python3 load_balancer.py`
3. Hit `http://127.0.0.1:8000` to see traffic routing in action.
