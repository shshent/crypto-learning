from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

# Ye aapka wala hi data hai jo abhi upar bana tha
target_enc = bytes.fromhex("742673286594976a6f793b80e578f5677606acf7a6388edcb9eb0e15832add9")
target_iv = bytes.fromhex("d0d91621c7cc0e95ebc7dca80836f289")

for i in range(1000):
    guess = f"greencity{i}"
    key = hashlib.sha256(guess.encode()).digest()
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=target_iv)
        msg = unpad(cipher.decrypt(target_enc), 16).decode()
        print(f"FOUND! Password is {guess} -> Message: {msg}")
        break
    except:
        pass

print("Brute force khatam")