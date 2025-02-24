from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

key = get_random_bytes(32)  # 256-bit key

# Save the key to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Create a cipher object using AES in EAX mode
cipher = AES.new(key, AES.MODE_EAX)

input_file = 'hello.txt'  # Replace with your file name

# Read the file's content
with open(input_file, 'rb') as file:
    file_data = file.read()

# Encrypt the file data
ciphertext, tag = cipher.encrypt_and_digest(file_data)

# Write the encrypted data and nonce (for decryption) to the file
with open(input_file, 'wb') as encrypted_file:
    # Save the nonce and the encrypted data
    encrypted_file.write(cipher.nonce)
    encrypted_file.write(tag)
    encrypted_file.write(ciphertext)

print("File encrypted successfully!")

