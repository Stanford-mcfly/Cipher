def gen_playfair_matrix(key):
    key = key.upper().replace("J","I")
    matrix=[]
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    for i in key:
        if i not in matrix:
            matrix.append(i)
    for i in alphabets:
        if i not in matrix:
            matrix.append(i)
            
    return [matrix[i:i+5] for i in range(0,25,5)]
    
def prepared_text(text):
    text = text.upper().replace("J", "I").replace(" ","")
    prepared=""
    i=0
    while i<len(text):
        prepared+=text[i]
        if i+1 < len(text):
            if(text[i]==text[i+1]):
                prepared+='X'
            else:
                prepared+=text[i+1]
                i=i+1
                
        i=i+1
    if len(prepared)%2!=0:
        prepared+='X'

    return prepared
    
def find_pos(mat, a):
    for i,row in enumerate(mat):
        for j, char in enumerate(row):
            if char == a:
                return i,j
    return None
    
def encrypt(key, text):
    mat = gen_playfair_matrix(key)
    plaintext = prepared_text(text)
    ciphertext=""
    for i in range(0, len(plaintext), 2):
        a,b = plaintext[i], plaintext[i+1]
        row_a, coln_a = find_pos(mat,a)
        row_b, coln_b = find_pos(mat,b)
        if row_a == row_b:
            ciphertext+= mat[row_a][(coln_a+1)%5]
            ciphertext+= mat[row_b][(coln_b+1)%5]
        elif coln_a == coln_b:
            ciphertext+= mat[(row_a+1)%5][coln_a]
            ciphertext+= mat[(row_b+1)%5][coln_b]
        else:
            ciphertext+= mat[row_a][coln_b]
            ciphertext+= mat[row_b][coln_a]
        
    return ciphertext
    
def decrypt(key, text):
    mat = gen_playfair_matrix(key)
    plaintext = prepared_text(text)
    ciphertext=""
    for i in range(0, len(plaintext), 2):
        a,b = plaintext[i], plaintext[i+1]
        row_a, coln_a = find_pos(mat,a)
        row_b, coln_b = find_pos(mat,b)
        if row_a == row_b:
            ciphertext+= mat[row_a][(coln_a-1)%5]
            ciphertext+= mat[row_b][(coln_b-1)%5]
        elif coln_a == coln_b:
            ciphertext+= mat[(row_a-1)%5][coln_a]
            ciphertext+= mat[(row_b-1)%5][coln_b]
        else:
            ciphertext+= mat[row_a][coln_b]
            ciphertext+= mat[row_b][coln_a]
        
    return ciphertext

def main():
    encrypted_text = encrypt("Monarchy","instrumentsx")
    print(encrypted_text)
    decrypted_text = decrypt("Monarchy", encrypted_text)
    print(decrypted_text)

if __name__ == "__main__":
    main()
            

        
            
        