# Token Bucket Rate Limiter from Scratch

A high-performance, memory-efficient implementation of the Token Bucket rate-limiting algorithm built using standard Python.

## 🛠️ Design Optimizations
* **Lazy Dynamic Refill:** Calculates token replenishment inline on incoming requests using delta epoch timestamps, eliminating the overhead of background processor threads.
* **Thread-Safe Guards:** Employs mutual exclusion primitives (`threading.Lock`) to secure precision token tracking during concurrent asynchronous requests.

## 🚀 Execution
```bash
python3 rate_limiter.py
