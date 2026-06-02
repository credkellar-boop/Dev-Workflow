# 📨 System Design: Message Queues & Event-Driven Architecture

Notes on scaling systems horizontally using asynchronous task delegation and message brokers.

## Synchronous vs. Asynchronous Communication
* **Synchronous (HTTP/gRPC):** Client sends a request and must wait blocking on the line until the server processes the data and sends a response back. High coupling.
* **Asynchronous (Message Broker):** Client drops a message payload into a queue and immediately returns a success status back to the user. A background worker picks it up later. Temporal decoupling.

## Fundamental Architectural Patterns
1. **Point-to-Point (Queue):** Each message inside the channel is pulled and processed by exactly one worker instance. Ideal for task delegation.
2. **Publish-Subscribe (Pub-Sub):** A single message is broadcasted out to an exchange topic and copied to multiple distinct queues so multiple independent services can consume the exact same event simultaneously.

## Next-Level Build Idea
* *Goal:* Implement a lightweight event-driven publisher and consumer framework inside `2-Build/` using our existing `mini-redis` storage foundation as a localized messaging queue buffer.
