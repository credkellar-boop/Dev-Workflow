# 🔄 Concurrency Models: Asynchronous Programming & Event Loops

Notes on building highly concurrent, non-blocking systems without the memory overhead of multi-threading.

## Threading vs. Asynchrony
* **Multi-threading (Blocking I/O):** One thread per connection. If a thread waits for a database read, it blocks completely. Scales poorly beyond a few thousand concurrent connections due to RAM constraints.
* **Asynchronous (Non-blocking I/O):** A single thread handles thousands of connections. It registers an I/O task and immediately frees itself up to handle other calculations while the OS handles the network wait.

## Core Pillars of Async Python
* `async def`: Declares a specialized execution block known as a **Coroutine**.
* `await`: Explicitly pauses the execution of a coroutine, yielding control back to the Event Loop until the target background operation is finished.

## Connection to My Builds
* My custom load balancer handles traffic by spawning heavy isolation threads. Transitioning to an async socket-selector framework would allow a single thread to handle those exact routing channels simultaneously.
