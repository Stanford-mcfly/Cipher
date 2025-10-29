def gen_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            seen.append(c)
    return [seen[i:i+5] for i in range(0, 25, 5)]

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if i + 1 < len(text) and text[i] != text[i+1]:
            result.append(text[i+1])
            i += 2
        else:
            result.append('X')
            i += 1
    if len(result) % 2:
        result.append('X')
    return ''.join(result)

def find_pos(mat, char):
    for i, row in enumerate(mat):
        if char in row:
            return i, row.index(char)

def remove_padding(text):
    # Remove trailing X's
    text = text.rstrip('X')
    # Remove X's between duplicate letters
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if i + 1 < len(text):
            # If current char followed by X and then same char, skip X
            if i + 2 < len(text) and text[i+1] == 'X' and text[i] == text[i+2]:
                i += 2
            else:
                i += 1
        else:
            i += 1
    return ''.join(result)

def playfair(key, text, decrypt=False):
    mat = gen_playfair_matrix(key)
    if not decrypt:
        text = prepare_text(text)
    result = ""
    shift = -1 if decrypt else 1
    
    for i in range(0, len(text), 2):
        r1, c1 = find_pos(mat, text[i])
        r2, c2 = find_pos(mat, text[i+1])
        
        if r1 == r2:  # Same row
            result += mat[r1][(c1 + shift) % 5] + mat[r2][(c2 + shift) % 5]
        elif c1 == c2:  # Same column
            result += mat[(r1 + shift) % 5][c1] + mat[(r2 + shift) % 5][c2]
        else:  # Rectangle
            result += mat[r1][c2] + mat[r2][c1]
    
    if decrypt:
        result = remove_padding(result)
    
    return result

def main():
    encrypted = playfair("Monarchy", "instrumentsx")
    print("Encrypted:", encrypted)
    decrypted = playfair("Monarchy", encrypted, decrypt=True)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()




