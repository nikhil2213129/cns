def create_matrix(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = [c for c in keyword if c in alphabet]
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    return digraphs

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def encrypt_digraph(digraph, matrix):
    r1, c1 = find_position(matrix, digraph[0])
    r2, c2 = find_position(matrix, digraph[1])
    
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_digraph(digraph, matrix):
    r1, c1 = find_position(matrix, digraph[0])
    r2, c2 = find_position(matrix, digraph[1])
    
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_cipher(text, keyword, mode='encrypt'):
    matrix = create_matrix(keyword)
    digraphs = preprocess_text(text)
    if mode == 'encrypt':
        return ''.join(encrypt_digraph(d, matrix) for d in digraphs)
    elif mode == 'decrypt':
        return ''.join(decrypt_digraph(d, matrix) for d in digraphs)

keyword = input("Enter the keyword: ").upper().replace('J', 'I')
plaintext = input("Enter the plaintext to encrypt: ").upper()

encrypted = playfair_cipher(plaintext, keyword, mode='encrypt')
print("Encrypted:", encrypted)

decrypted = playfair_cipher(encrypted, keyword, mode='decrypt')
print("Decrypted:", decrypted)
