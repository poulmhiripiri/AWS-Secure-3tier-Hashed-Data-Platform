import base64
import hashlib
import hmac
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

ITERATIONS = int(os.getenv("HASH_ITERATIONS", "150000"))
PEPPER = os.getenv("APP_PEPPER", "development-only-pepper-change-me")

# In production this would be RDS. For local demonstration we keep records in memory.
USERS = []


def hash_sensitive_value(value: str) -> str:
    """Return a PBKDF2-HMAC-SHA256 hash with a unique salt and application pepper."""
    if value is None:
        return None

    salt = os.urandom(16)
    material = f"{value}{PEPPER}".encode("utf-8")
    derived_key = hashlib.pbkdf2_hmac("sha256", material, salt, ITERATIONS)
    return "pbkdf2_sha256${}${}${}".format(
        ITERATIONS,
        base64.b64encode(salt).decode("utf-8"),
        base64.b64encode(derived_key).decode("utf-8"),
    )


def verify_sensitive_value(value: str, stored_hash: str) -> bool:
    """Verify a submitted value against a stored PBKDF2 hash using constant-time comparison."""
    algorithm, iterations, salt_b64, hash_b64 = stored_hash.split("$")
    if algorithm != "pbkdf2_sha256":
        raise ValueError("Unsupported hash algorithm")

    salt = base64.b64decode(salt_b64)
    expected_hash = base64.b64decode(hash_b64)
    material = f"{value}{PEPPER}".encode("utf-8")
    calculated_hash = hashlib.pbkdf2_hmac("sha256", material, salt, int(iterations))
    return hmac.compare_digest(calculated_hash, expected_hash)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json(force=True)

    required_fields = ["first_name", "last_name", "email", "password"]
    missing = [field for field in required_fields if not payload.get(field)]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    user = {
        "id": len(USERS) + 1,
        "first_name": payload["first_name"],
        "last_name": payload["last_name"],
        "email": payload["email"],
        "password_hash": hash_sensitive_value(payload.get("password")),
        "national_insurance_number_hash": hash_sensitive_value(payload.get("national_insurance_number")),
        "phone_number_hash": hash_sensitive_value(payload.get("phone_number")),
        "account_reference_hash": hash_sensitive_value(payload.get("account_reference")),
        "fingerprint_template_hash": hash_sensitive_value(payload.get("fingerprint_template")),
        "retina_template_hash": hash_sensitive_value(payload.get("retina_template")),
    }
    USERS.append(user)

    return jsonify({
        "id": user["id"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "message": "User created. Sensitive fields stored as hashes only."
    }), 201


@app.route("/debug/users", methods=["GET"])
def debug_users():
    """Local demo endpoint showing what would be stored in RDS. Remove in production."""
    return jsonify(USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
