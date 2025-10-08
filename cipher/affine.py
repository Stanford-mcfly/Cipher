def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def affine_decrypt(a,b,text):
    inverse = mod_inverse(a)
    result = ""
    for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                x = ord(char) - base
                result += chr((inverse * (x-b) % 26)+base)
            else:
                result+=char

    return result

def affine_encryt(a,b,text):
    if gcd(a,26) != 1:
        raise ValueError("a and 26 are not coprime")
    
    result=""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            result += chr(((a*x+b) % 26)+base)
        else:
            result+=char

    return result

def mod_inverse(a):
    for i in range(26):
        if(a*i)%26 == 1:
            return i
    raise ValueError("Mod inverse ila da venna")

def main():
    encrypted_msg = affine_encryt(7,14,"reva")
    print(encrypted_msg)
    decrypted_msg = affine_decrypt(7,14,encrypted_msg)
    print(decrypted_msg)

if __name__ == "__main__":
    main()