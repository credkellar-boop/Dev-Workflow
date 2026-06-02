# 🎛️ System Architecture: API Gateways & Reverse Proxies

Notes on centralizing cluster ingress, path-based routing matrix design, and edge-security layers.

## Forward Proxies vs. Reverse Proxies
* **Forward Proxy:** Sits in front of a client and acts on behalf of the user to mask identity or bypass network restrictions (e.g., a VPN).
* **Reverse Proxy:** Sits in front of backend servers and acts on behalf of the infrastructure to balance load, terminate TLS, and obscure internal service typography.

## Core Advantages at the Edge
* **Unified Endpoint Map:** Clients interact with a single host string, eliminating Cross-Origin Resource Sharing (CORS) configurations across scattered port allocations.
* **Edge Security Shielding:** Centralizes token parsing (JWT) and traffic throttling (Rate Limiting) at the entry gate, preventing unauthenticated traffic from wasting downstream compute cycles.
