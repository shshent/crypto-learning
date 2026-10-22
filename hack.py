from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# Victim's encrypted data (auto-generated)
real_password = "greencity123"
key_real = hashlib.sha256(real_password.encode()).digest()
iv = get_random_bytes(16)
cipher = AES.new(key_real, AES.MODE_CBC, iv=iv)
encrypted = cipher.encrypt(pad(b"Player Score: 9999", 16))

print(f"Target: {encrypted.hex()}")

# Brute force
for i in range(1000):
    guess = f"greencity{i}"
    key_guess = hashlib.sha256(guess.encode()).digest()
    try:
        c = AES.new(key_guess, AES.MODE_CBC, iv=iv)
        msg = unpad(c.decrypt(encrypted), 16).decode()
        print(f"FOUND! Password is {guess} -> {msg}")
        break
    except:
        pass
