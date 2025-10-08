def power(a,b,m):
    return pow(a,b,m)

def mod_inverse(e,phi):
    gcd_val,x,_ = ex_euclid(e,phi)
    if gcd_val != 1:
        raise ValueError("Mod inverse doesn't exist")
    else:
        return x%phi

def ex_euclid(a,b):
    if a==0:
        return b,0,1
    else:
        gcd_val,x1,y1 = ex_euclid(b%a,a)
        x=y1-(b//a)*x1
        y=x1
        return gcd_val,x,y
    
def generate_rs_key(p,q):
    n= p*q
    phi = (p-1)*(q-1)
    e=65537
    d = mod_inverse(e,phi)
    return (e,n), (d,n)
    
def rsa_encrypt(plaintext, pub_key):
    e,n = pub_key
    return [power(ord(char),e,n) for char in plaintext]
    
def rsa_decrypt(plaintext, pri_key):
    d,n = pri_key
    return ''.join(chr(power(char, d, n)) for char in plaintext)

    
def main():
    p=61
    q=53
    pub_key, pri_key = generate_rs_key(p,q)
    encrypted_text= rsa_encrypt("reva", pub_key)
    print(encrypted_text)
    decrypted_text = rsa_decrypt(encrypted_text, pri_key)
    print(decrypted_text)
    
if __name__ == "__main__":
    main()
    