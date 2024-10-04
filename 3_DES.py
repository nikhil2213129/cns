from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_DES(key, message):
    des = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message)
    encrypted_message = des.encrypt(padded_message.encode('utf-8'))
    return binascii.hexlify(encrypted_message).decode('utf-8')

def decrypt_DES(key, encrypted_message):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_message = des.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted_message.decode('utf-8').rstrip()

key = get_random_bytes(8)
message = input("Enter a Message: ")
print(f"Original Message: {message}")
encrypted_message = encrypt_DES(key, message)
print(f"Encrypted Message (Hex): {encrypted_message}")
decrypted_message = decrypt_DES(key, encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
