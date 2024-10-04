import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % phi

p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = mod_inverse(e, phi)

msg = int(input("Enter a message to encrypt (as an integer): "))
print("Message data =", msg)

c = pow(msg, e, n)
print("Encrypted data =", c)

m = pow(c, d, n)
print("Original Message Sent =", m)
