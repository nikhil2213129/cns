def caesar_cipher_encrypt(plaintext, shift):
    cipher_text = ''
    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if char.isupper():
            plaintext += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

plaintext = input("Enter the Plaintext: ")
shift = int(input("Enter the shift value: "))

# Encryption
ciphertext = caesar_cipher_encrypt(plaintext, shift)
print("Cipher Text = " + ciphertext)

# Decryption
decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
print("Decrypted Text = " + decrypted_text)