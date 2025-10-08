import random
def power(a,b,m):
    return pow(a,b,m)

def diffiehellman(g,p):
    # Alice's private key
    a = random.randint(2,p-2)
    # Bob's private key  
    b = random.randint(2,p-2)
    
    # Public keys (these are exchanged publicly)
    A = power(g,a,p)  # Alice's public key: g^a mod p
    B = power(g,b,p)  # Bob's public key: g^b mod p
    
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")
    print(f"Alice's public key (A): {A}")
    print(f"Bob's public key (B): {B}")
    
    # Shared secret calculation
    # Alice computes: B^a mod p = (g^b)^a mod p = g^(ab) mod p
    shared_secret_alice = power(B, a, p)
    
    # Bob computes: A^b mod p = (g^a)^b mod p = g^(ab) mod p  
    shared_secret_bob = power(A, b, p)
    
    print(f"Alice's computed shared secret: {shared_secret_alice}")
    print(f"Bob's computed shared secret: {shared_secret_bob}")
    print(f"Secrets match: {shared_secret_alice == shared_secret_bob}")
    
    return shared_secret_alice


def main():
    diffiehellman(5,23)

if __name__ == "__main__":
    main()