def vig_encrypt(key,text):
    result = ""
    key_index=0
    key_len = len(key)
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index]) - ord('A')
            x = ord(char) - base
            result += chr(((x + shift)% 26)+base)
        else:
            result +=char
        key_index = (key_index+1) % key_len
    return result
    
def vig_decrypt(key,text):
    result = ""
    key_index=0
    key_len = len(key)
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index]) - ord('A')
            x = ord(char) - base
            result += chr(((x - shift)% 26)+base)
        else:
            result +=char
        key_index = (key_index+1)%key_len
    return result
    
def main():
    answer = vig_encrypt("key", "Hello World")
    print(answer)
    answer1 = vig_decrypt("key", answer)
    print(answer1)

if __name__ == "__main__":
    main()