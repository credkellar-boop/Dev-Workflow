# Asynchronous HTTP Server from Scratch

A high-concurrency, single-threaded web server built using Python's native `asyncio` architecture to process incoming non-blocking I/O network streams.

## 🛠️ Performance Architecture
* **Single-Thread Concurrency:** Uses an event loop interface instead of resource-heavy operating system thread pools, keeping the memory footprint ultra-low.
* **Coroutines & Event Delegation:** Leverages explicit `async/await` syntax to suspend active transaction states on network reads/writes, allowing context switches without blocking the execution core.

## 🚀 Execution
```bash
python3 async_server.py
