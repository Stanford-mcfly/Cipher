import math

def encrypt(text, cols):
    clean=""
    for c in text:
        if c.isalpha():
            clean+=c

    n = len(clean)
    rows = math.ceil(n/cols)
    k=0

    arr = [['x' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if(k>=n):
                break
            arr[i][j]= clean[k]
            k+=1

    cipher=""
    for i in range(cols):
        for j in range(rows):
            cipher+= arr[j][i]

    return cipher


def decrypt(cipher, cols):
    
    n = len(cipher)
    rows = math.ceil(n/cols)
    k=0

    arr = [['x' for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        for j in range(rows):
            if(k>=n):
                break
            arr[j][i]= cipher[k]
            k+=1

    plain = ""
    
    for i in range(rows):
        for j in range(cols):
            plain+= arr[i][j]

    return plain




text = input("Enter text: ")
key = input("Enter key: ")
k = len(key)

cipher = encrypt(text,k)
print("Ciphered text: ", cipher)

plain = decrypt(cipher,k)
print("Decrypted text: ", plain)