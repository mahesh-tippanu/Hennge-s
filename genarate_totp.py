import base64, hmac, hashlib, time, struct

def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode()
    timestep = int(time.time() // 30)
    msg = struct.pack(">Q", timestep)
    hmac_digest = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    code = (
        ((hmac_digest[offset] & 0x7f) << 24) |
        ((hmac_digest[offset + 1] & 0xff) << 16) |
        ((hmac_digest[offset + 2] & 0xff) << 8) |
        (hmac_digest[offset + 3] & 0xff)
    )
    return str(code % 10**10).zfill(10)

# --- Replace this with your actual email ---
email = "mtippanu@student.gitam.edu.com"
print("TOTP Password:", generate_totp(email))
