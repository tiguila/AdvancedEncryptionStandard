# AdvancedEncryptionStandard


## This project aims at using the AES encryption algorithm in Python.


## Objectives
* Encrypt a text file using AES (`encrypt.py`) (Part 1)
* Decrypt the file encrypted in **Part 1** (`decrypt.py`) (Part 2)


## Part 1
* Read a text file
* Generate a 256-bit key
* Save the key to a file, `secret.key`
* Encrypt the content of the file being read using the secret key generated above


## Part 2
* Read the AES key in `secret.key` (step 1)
* Read the encrypted text
* Decrypt the encrypted text using the key in step 1
* Write the decrypted content back to the original file



## Requirements
Install
```python
pip install pycryptodome
```
