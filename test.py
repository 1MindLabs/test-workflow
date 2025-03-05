import jwt
import time

# Load private key
with open("private-key.pem", "rb") as f:
    private_key = f.read()

# Define payload
payload = {
    "iat": int(time.time()),  # Issued at
    "exp": int(time.time()) + 600,  # Expiration (10 minutes)
    "iss": 1166876,
}

# Generate JWT
jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
print(jwt_token)