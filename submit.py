import requests
import base64
import json
import time
import hmac
import hashlib
import struct

# ─── CONFIGURE THESE ──────────────────────────────────────────────────────────
email    = "mtippanu@student.gitam.edu"
gist_url = "https://gist.github.com/mahesh-tippanu/c01172abd01a92b1951bf104b52a03cf"
# ──────────────────────────────────────────────────────────────────────────────

def generate_totp(email: str) -> str:
    """
    Generate a 10‐digit TOTP using:
      - secret = email + "HENNGECHALLENGE004"
      - HMAC-SHA-512
      - 30s time step
    """
    secret = (email + "HENNGECHALLENGE004").encode()
    timestep = int(time.time() // 30)
    msg      = struct.pack(">Q", timestep)
    digest   = hmac.new(secret, msg, hashlib.sha512).digest()
    offset   = digest[-1] & 0x0F
    code = (
        ((digest[offset]   & 0x7f) << 24) |
        ((digest[offset+1] & 0xff) << 16) |
        ((digest[offset+2] & 0xff) <<  8) |
        ( digest[offset+3] & 0xff)
    )
    return str(code % 10**10).zfill(10)

# Generate a fresh TOTP
totp = generate_totp(email)

# Build the Basic Auth header
auth_str     = f"{email}:{totp}"
auth_encoded = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Content-Type":  "application/json",
    "Authorization": f"Basic {auth_encoded}"
}

payload = {
    "github_url":       gist_url,
    "contact_email":    email,
    "solution_language":"python"
}

# Debug (optional — remove in final run)
# print("Using TOTP:", totp)

# Send the request
resp = requests.post(
    "https://api.challenge.hennge.com/challenges/backend-recursion/004",
    headers=headers,
    data=json.dumps(payload)
)

print("Status Code:", resp.status_code)
print("Response   :", resp.text)
