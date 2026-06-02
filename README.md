# 🚀 Dev-Workflow

Welcome to my central engineering hub. This repository tracks my continuous cycle of **learning** foundational concepts, **building** systems from scratch, and **contributing** back to the open-source ecosystem.

---

## 🧭 My Flywheel Status

| Pillar | Focus Area | Current Target / Project | Status |
| :--- | :--- | :--- | :--- |
| **1. Learn** | System Design & Networking | High-availability architectures | 📖 In Progress |
| **2. Build** | Systems Programming | Building a Redis-clone from scratch in Go | 🛠️ Coding |
| **3. Contribute**| Open-Source Ecosystem | Fixing good-first-issues in `Django` | 🚀 2 PRs Merged |

---

## 🧠 1. Learn (Knowledge Base)
This section documents my deep-dives into core computer science concepts. I believe the best way to learn is to explain it simply to others.
* [System Design Notes](./1-Learn/system-design/) - Sharding, Load Balancers, and CAP Theorem.
* [My Learning Resources](./1-Learn/resources.md) - Curated roadmaps and books I am following.

## 🛠️ 2. Build (From Scratch)
Production frameworks hide the hard parts. Here, I strip away the magic and build clones of popular tools to understand how they work under the hood.
* **[Mini HTTP Server](./2-Build/mini-http-server/)**: A raw TCP socket-based server handling HTTP/1.1 requests.
* **[Custom Key-Value DB](./2-Build/custom-db/)**: A lightweight, disk-backed storage engine.

## 🤝 3. Contribute (Open Source Log)
Actively giving back to the software that runs the world. 

### 🏆 Merged Pull Requests
* **[Django PR #12345](https://github.com/django/django/pull/12345)**: Fixed a memory leak in the test runner.
* **[FastAPI PR #6789](https://github.com/tiangolo/fastapi/pull/6789)**: Improved documentation clarity for WebSocket endpoints.

# Mini HTTP Server from Scratch

A lightweight, raw TCP network socket server built using standard Python to explore low-level network programming.

## 🛠️ How it Works
* **Transport Layer:** Utilizes raw TCP sockets (`socket.AF_INET`, `socket.SOCK_STREAM`) to handle network data streams.
* **Application Layer:** Manually parses HTTP/1.1 request strings and serializes raw string responses into encoded binary data byte blocks (`utf-8`).

## 🚀 How to Run
1. Execute the server script: `python3 server.py`
2. Open your browser and navigate to `http://127.0.0.1:8080`


Dev-Workflow/
├── README.md                 # The dashboard of your entire developer journey
├── LICENSE                   # Open-source license (e.g., MIT)
│
├── 1-Learn/                  # Phase 1: Conceptual Knowledge
│   ├── system-design/        # Notes on scaling, databases, caching
│   ├── languages/            # Deep dives into Python, Go, TypeScript, etc.
│   └── resources.md          # Links to favorite roadmaps, books, and articles
│
├── 2-Build/                  # Phase 2: From Scratch Projects
│   ├── mini-http-server/     # A web server built using raw sockets
│   ├── custom-db/            # A simple key-value store 
│   └── README.md             # Index of your custom builds and their statuses
│
└── 3-Contribute/             # Phase 3: Real-World Open Source
    ├── tracked-issues/       # Notes/clones of issues you are currently solving
    └── contribution-log.md   # Markdown table tracking your merged Pull Requests
