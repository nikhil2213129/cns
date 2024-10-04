def encrypt_rail_fence(text, key):
    rail = [[] for _ in range(key)]
    row, direction_down = 0, True

    for char in text:
        rail[row].append(char)
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        row += 1 if direction_down else -1
    
    return ''.join([''.join(r) for r in rail])

def decrypt_rail_fence(cipher, key):
    rail_pattern = ['\n'] * len(cipher)
    row, direction_down = 0, True

    for i in range(len(cipher)):
        rail_pattern[i] = row
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        row += 1 if direction_down else -1
    
    rail = ['' for _ in range(len(cipher))]
    index = 0
    for r in range(key):
        for i in range(len(cipher)):
            if rail_pattern[i] == r:
                rail[i] = cipher[index]
                index += 1

    row, direction_down, result = 0, True, []
    for i in range(len(cipher)):
        result.append(rail[i])
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        row += 1 if direction_down else -1
    
    return ''.join(result)

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (number of rails): "))

ciphertext = encrypt_rail_fence(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt_rail_fence(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
