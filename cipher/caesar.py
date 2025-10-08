def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((ord(char) - base+shift) % 26) + base)
            
        else: 
            result += char
            
    
    return result 
            
def main():
    result = encrypt("reva", 3)
    print(result)
    plain = encrypt(result,26-3)
    print(plain)

if __name__ == "__main__":
    main()