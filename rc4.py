def ksa(key):
   
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4(key, text):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    res = []
    for c in text:
        val = ord(c) ^ next(keystream)
        res.append(chr(val))
    return ''.join(res)

# Example usage
key = "secretkey"
plaintext = "HELLO"
ciphertext = rc4(key, plaintext)
print("Ciphertext:", ciphertext.encode())  # show bytes
decrypted = rc4(key, ciphertext)  # RC4 is symmetric
print("Decrypted:", decrypted)
