# Custom Asynchronous Message Broker & Task Queue

A bare-metal event-driven microservice pattern implementation built using standard Python primitives to demonstrate async task delegation.

## 🛠️ System Design Specifications
* **FIFO Broker Architecture:** Employs thread-safe atomic collection blocks (`queue.Queue`) to safely pipeline JSON transaction objects across system boundaries.
* **Horizontal Consumer Scaling:** Multi-threaded worker abstraction engines consume events concurrently, showcasing how real clusters scale throughput under intense traffic bursts without degrading client performance.

## 🚀 Execution
```bash
python3 worker_queue.py
