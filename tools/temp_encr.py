import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode


def derive_key(password: str, salt: bytes, iterations: int = 200_000) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=iterations,
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt(plaintext: str, password: str) -> bytes:
    salt = os.urandom(16)  # store this with ciphertext
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # unique per encryption
    ct = aesgcm.encrypt(nonce, plaintext, None)
    # package = salt | nonce | ct
    return salt + nonce + ct


def decrypt(package: str, password: str) -> bytes:
    salt, nonce, ct = package[:16], package[16:28], package[28:]
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ct, None)


pw = "Strong passphrase here"
data = "secret message"
encrypted = encrypt(pw, data)
decrypted = decrypt(pw, blob)
print(f"[INFO] ENcrypted data: {encrypted}")
print(f"[INFO] DEcrypted data: {decrypted}")
