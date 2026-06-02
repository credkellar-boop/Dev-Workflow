# 🔐 Security Architecture: Stateless Authentication & JWTs

Notes on securing distributed microservices using cryptographically signed, stateless tokens.

## Session-Based vs. Token-Based Authentication
* **Session-Based (Stateful):** Server generates a random session identifier, saves it in a central database or memory cache (like Redis), and sends it to the client. Forces an external network I/O lookup on every incoming user request.
* **Token-Based (Stateless):** Server signs a user data payload using a private cryptographic key and returns it to the client. Any service in the cluster can independently decrypt and verify the signature in $O(1)$ CPU time without an external database check.

## Anatomy of a JSON Web Token
A JWT is composed of three Base64URL-encoded strings separated by periods:
1. `Header`: Declares the token signing algorithm (e.g., `HS256`).
2. `Payload`: Holds target user claims (e.g., `user_id`, `roles`, `exp` timestamp).
3. `Signature`: Constructed by hashing the combined header, payload, and a server-side secret key to prevent client tampering.

## Next-Level Build Idea
* *Goal:* Implement a raw JWT generator and validation parser inside `2-Build/` from scratch—manually encoding headers, compiling claims, and generating cryptographic HMAC signatures using Python's standard `hashlib` library.
