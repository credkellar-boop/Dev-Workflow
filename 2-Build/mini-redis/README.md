# Mini-Redis Engine from Scratch

A lightweight, high-speed, thread-safe in-memory key-value database built using standard Python.

## 🛠️ Features
* **Thread-Safe Core:** Utilizes mutex synchronization locks (`threading.Lock`) to prevent race conditions during concurrent data operations.
* **TTL Cache Eviction:** Tracks epoch millisecond timestamps to systematically drop stale data tokens on access evaluation.

## 🚀 Execution
```bash
python3 kv_store.py
