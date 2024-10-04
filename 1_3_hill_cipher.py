def createMatrix(size):
    return [[0] * size for _ in range(size)]

def getKeyMatrix(key, size, keyMatrix):
    k = 0
    for i in range(size):
        for j in range(size):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector, keyMatrix, size, cipherMatrix):
    for i in range(size):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(size):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key, size):
    keyMatrix = createMatrix(size)
    messageVector = [[0] for _ in range(size)]
    cipherMatrix = [[0] for _ in range(size)]
    getKeyMatrix(key, size, keyMatrix)
    for i in range(size):
        messageVector[i][0] = ord(message[i]) % 65
    encrypt(messageVector, keyMatrix, size, cipherMatrix)
    CipherText = []
    for i in range(size):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    print("Ciphertext: ", "".join(CipherText))

size = int(input("Enter the size of the matrix (e.g., 3 for 3x3): "))
message = input(f"Enter the {size}-letter Plaintext: ").upper()
key = input(f"Enter the {size*size}-letter key: ").upper()
HillCipher(message, key, size)