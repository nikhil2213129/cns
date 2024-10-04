def encrypt_rail_fence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    direction_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        rail[row][col] = text[i]
        col += 1
        
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    
    ciphertext = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                ciphertext.append(rail[i][j])
    
    return "".join(ciphertext)

def decrypt_rail_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    direction_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    plaintext = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        if rail[row][col] != '*':
            plaintext.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    
    return "".join(plaintext)

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (number of rails): "))

ciphertext = encrypt_rail_fence(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt_rail_fence(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")