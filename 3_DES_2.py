from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, DES.block_size)
    return plaintext.decode()

message = input("Enter the message to encrypt: ")
key = get_random_bytes(8) #Example=8bytekey

if len(key) != 8:
    print("Error: Key must be exactly 8 bytes long!")
else:
    ciphertext = des_encrypt(message, key)
    print("Encrypted (Ciphertext):", ciphertext)

    decrypted_message = des_decrypt(ciphertext, key)
    print("Decrypted (Original Message):", decrypted_message)
