import base64
import json
import hmac
import hashlib
import time

class MiniJWTEngine:
    def __init__(self, secret_key):
        self.secret_key = secret_key.encode('utf-8')

    def _base64url_encode(self, data: bytes) -> str:
        """Encodes bytes to standard Base64URL string (stripping padding and slashes)."""
        return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

    def _base64url_decode(self, data: str) -> bytes:
        """Decodes a Base64URL string back to bytes, re-adding required padding."""
        rem = len(data) % 4
        if rem > 0:
            data += '=' * (4 - rem)
        return base64.urlsafe_b64decode(data.encode('utf-8'))

    def generate_token(self, user_id, roles, ttl_seconds=3600):
        """Constructs a cryptographically signed stateless token string."""
        # 1. Create Header
        header = {"alg": "HS256", "typ": "JWT"}
        encoded_header = self._base64url_encode(json.dumps(header).encode('utf-8'))

        # 2. Create Payload with Claims
        payload = {
            "user_id": user_id,
            "roles": roles,
            "exp": int(time.time()) + ttl_seconds
        }
        encoded_payload = self._base64url_encode(json.dumps(payload).encode('utf-8'))

        # 3. Compile Signature via HMAC-SHA256
        signature_base = f"{encoded_header}.{encoded_payload}".encode('utf-8')
        raw_signature = hmac.new(self.secret_key, signature_base, hashlib.sha256).digest()
        encoded_signature = self._base64url_encode(raw_signature)

        # 4. Return token string format
        return f"{encoded_header}.{encoded_payload}.{encoded_signature}"

    def verify_token(self, token: str):
        """Validates token signatures and expiration status. Returns payload or None."""
        try:
            parts = token.split('.')
            if len(parts) != 3:
                print("❌ Authentication Error: Invalid token segment structure.")
                return None

            encoded_header, encoded_payload, encoded_signature = parts

            # 1. Regenerate Signature to verify data authenticity
            signature_base = f"{encoded_header}.{encoded_payload}".encode('utf-8')
            expected_signature = hmac.new(self.secret_key, signature_base, hashlib.sha256).digest()
            decoded_signature = self._base64url_decode(encoded_signature)

            # Use constant-time comparison to thwart timing side-channel attacks
            if not hmac.compare_digest(expected_signature, decoded_signature):
                print("🚨 SECURITY WARNING: Cryptographic signature mismatch! Data tampered.")
                return None

            # 2. Check Expiration Claims Window
            payload = json.loads(self._base64url_decode(encoded_payload).decode('utf-8'))
            if time.time() > payload.get('exp', 0):
                print("⏰ Authentication Error: Token signature valid, but session has expired.")
                return None

            print(f"🟢 Token verified successfully! Access granted for user: {payload['user_id']}")
            return payload

        except Exception as e:
            print(f"❌ Verification Exception: {e}")
            return None

# Validation pipeline verification sequence
if __name__ == "__main__":
    # Internal cluster private key
    SERVER_SECRET = "super_secure_cluster_passphrase_123"
    engine = MiniJWTEngine(SERVER_SECRET)

    print("--- Simulating Legitimate Token Generation ---")
    valid_token = engine.generate_token(user_id="dev_user_404", roles=["admin", "developer"])
    print(f"Generated Token:\n{valid_token}\n")

    print("--- Validating Legitimate Token Access ---")
    engine.verify_token(valid_token)

    print("\n--- Simulating Man-In-The-Middle Attack (Payload Tampering) ---")
    # Attacker decodes the plain text payload part, modifies roles to inject root clearance
    token_parts = valid_token.split('.')
    tampered_payload = {"user_id": "dev_user_404", "roles": ["root_system_operator"], "exp": int(time.time()) + 5000}
    encoded_tampered_payload = engine._base64url_encode(json.dumps(tampered_payload).encode('utf-8'))
    
    # Reassemble token using original header and signature, but swapped payload
    malicious_token = f"{token_parts[0]}.{encoded_tampered_payload}.{token_parts[2]}"
    
    print(f"Malicious Token:\n{malicious_token}\n")
    engine.verify_token(malicious_token)
