# crypto-learning

A beginner-friendly project to learn how AES encryption works in Python and why weak passwords are dangerous.

Built while learning about Cryptography - for educational purposes only.

### 📁 Files

- **encrypt.py** - Encrypts a message like `Player Score: 9999` using AES-CBC with a password-derived key.
- **secure_app.py** - Secure version that uses a strong random key and proper IV handling.
- **hack.py** - Demonstrates a brute-force attack on a weak password (`greencity123`). Shows why `greencity123` can be cracked in <1000 tries.

### 🚀 How to Run

1. Install dependency:

2. Run encryption:
 
3. Run the brute-force demo:
   Expected output: `FOUND! Password is greencity123`

### 🧠 What I Learned

- AES needs an even-length hex string - `bytes.fromhex()` will fail if you cut the hex odd.
- Using `hashlib.sha256(password)` to make a key is weak if the password is guessable.
- Always use random IV and strong, non-guessable keys.
- Padding (`pad` / `unpad`) is required for AES-CBC.

### ⚠️ Disclaimer

This project is for learning only. Do not use this code to attack real systems.

---
Created by shshent   
