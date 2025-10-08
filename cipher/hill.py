import numpy as np

# Convert character to number (A=0, B=1, ..., Z=25)
def char_to_num(char):
    return ord(char.upper()) - ord('A')

# Convert number to character
def num_to_char(num):
    return chr((num % 26) + ord('A'))

# Pad plaintext with X if length is odd
def pad_text(text, size):
    while len(text) % size != 0:
        text += 'X'
    return text

# Hill Cipher Encryption
def hill_encrypt(plaintext, key_matrix):
    size = key_matrix.shape[0]
    plaintext = pad_text(plaintext.upper().replace(" ", ""), size)
    
    ciphertext = ""
    for i in range(0, len(plaintext), size):
        block = [char_to_num(c) for c in plaintext[i:i+size]]
        result = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(num_to_char(int(num)) for num in result)
    return ciphertext

# Hill Cipher Decryption
def hill_decrypt(ciphertext, key_matrix):
    size = key_matrix.shape[0]
    
    # Find inverse of key matrix mod 26
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)  # modular inverse
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjugate) % 26
    
    plaintext = ""
    for i in range(0, len(ciphertext), size):
        block = [char_to_num(c) for c in ciphertext[i:i+size]]
        result = np.dot(inv_matrix, block) % 26
        plaintext += ''.join(num_to_char(int(num)) for num in result)
    return plaintext


def main():
    # Example key matrix (must be invertible mod 26)
    key_matrix = np.array([[3, 3],
                           [2, 5]])
    
    plaintext = "HELLO"
    ciphertext = hill_encrypt(plaintext, key_matrix)
    decrypted = hill_decrypt(ciphertext, key_matrix)
    
    print("Plaintext :", plaintext)
    print("Encrypted :", ciphertext)
    print("Decrypted :", decrypted)


if __name__ == "__main__":
    main()
