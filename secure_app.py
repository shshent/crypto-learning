from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Sahi tarika: Key random banao, hardcode mat karo
key = get_random_bytes(32) # 32 byte = AES-256
print(f"SECRET KEY (ye Keystore me save hoti hai): {key.hex()}")

# Ab score lock karo
message = "Player Score: 9999"
cipher = AES.new(key, AES.MODE_CBC)
ct = cipher.encrypt(pad(message.encode(), 16))
print(f"Encrypted Score: {ct.hex()}")
print(f"IV: {cipher.iv.hex()}")
# Real app me: ct + iv phone me save, key Keystore me save