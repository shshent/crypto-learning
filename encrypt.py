# pip install pycryptodome - ye ho chuka hai tumhara

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

# 1. Password se key banao
password = "greencity123"
key = hashlib.sha256(password.encode()).digest()

# 2. Message encrypt karo
message = "Player Score: 9999"
cipher = AES.new(key, AES.MODE_CBC)
encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))

print(f"Encrypted: {encrypted.hex()}")
print(f"IV: {cipher.iv.hex()}")

# 3. Decrypt karo
cipher2 = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
decrypted = unpad(cipher2.decrypt(encrypted), AES.block_size)
print(f"Decrypted: {decrypted.decode()}")