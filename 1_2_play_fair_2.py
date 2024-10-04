import string

def create_matrix(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    alphabet = string.ascii_uppercase.replace('J', '')
    matrix = [c for c in keyword if c in alphabet] + [c for c in alphabet if c not in keyword]
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    digraphs = [(text[i] + (text[i+1] if i+1 < len(text) and text[i] != text[i+1] else 'X')) for i in range(0, len(text), 2)]
    return digraphs

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def process_digraph(digraph, matrix, shift):
    r1, c1 = find_position(matrix, digraph[0])
    r2, c2 = find_position(matrix, digraph[1])
    if r1 == r2:
        return matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
    elif c1 == c2:
        return matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_cipher(text, keyword, mode='encrypt'):
    matrix = create_matrix(keyword)
    digraphs = preprocess_text(text)
    shift = 1 if mode == 'encrypt' else -1
    return ''.join(process_digraph(d, matrix, shift) for d in digraphs)

keyword = input("Enter the keyword: ").upper().replace('J', 'I')
plaintext = input("Enter the plaintext to encrypt: ").upper()

encrypted = playfair_cipher(plaintext, keyword, mode='encrypt')
print("Encrypted:", encrypted)

decrypted = playfair_cipher(encrypted, keyword, mode='decrypt')
print("Decrypted:", decrypted)
