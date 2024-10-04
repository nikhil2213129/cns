from sympy import isprime

def is_primitive_root(alpha, q):
    required_set = set(range(1, q))  # Set of integers from 1 to q-1
    return set(pow(alpha, power, q) for power in range(1, q)) == required_set

def find_primitive_root(q):
    if not isprime(q):
        raise ValueError(f"{q} is not a prime number, primitive root does not exist.")
    for alpha in range(2, q):
        if is_primitive_root(alpha, q):
            return alpha
    return None

def diffie_hellman(prime_q, primitive_root, private_a, private_b):
    public_a = pow(primitive_root, private_a, prime_q)
    public_b = pow(primitive_root, private_b, prime_q)
    shared_secret_a = pow(public_b, private_a, prime_q)
    shared_secret_b = pow(public_a, private_b, prime_q)
    return public_a, public_b, shared_secret_a, shared_secret_b


q = int(input("Enter the a Large Prime 'q': "))
alpha = find_primitive_root(q)
x_A = int(input("Enter the a Private key of A': "))
x_B = int(input("Enter the a Private key of B': "))

if x_A >= q or x_B >= q:
    raise ValueError(f"Private keys must be less than {q}")
public_a, public_b, shared_secret_a, shared_secret_b = diffie_hellman(q, alpha, x_A, x_B)

print("Alpha: ", alpha)
print("y_A (Public key of A): ", public_a)
print("y_B (Public key of B): ", public_b)
print(f"Shared Secret computed by A: {shared_secret_a}")
print(f"Shared Secret computed by B: {shared_secret_b}")

if shared_secret_a == shared_secret_b:
    print("Key Exchange successful! Shared Secret is the Same.")
else:
    print("Key Exchange Failed!")
