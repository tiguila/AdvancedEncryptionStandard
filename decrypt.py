from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import binascii

from Crypto.Cipher import AES

# Read the AES key from the saved file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

input_file = 'hello.txt'  # Replace with your encrypted file name

# Read the encrypted file's content (nonce, tag, and ciphertext)
with open(input_file, 'rb') as encrypted_file:
    nonce = encrypted_file.read(16)  # The nonce is 16 bytes for AES.MODE_EAX
    tag = encrypted_file.read(16)    # The tag is 16 bytes for AES.MODE_EAX
    encrypted_data = encrypted_file.read()

# Create a cipher object for decryption
cipher_decrypt = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Decrypt the data and verify the tag
decrypted_data = cipher_decrypt.decrypt_and_verify(encrypted_data, tag)

# Write the decrypted data back to the same file (hello.txt)
with open(input_file, 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")
