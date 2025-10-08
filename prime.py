def prime_check(n):
    if n<=1:
        return False
    if n<=3:
        return True
    
    if n%2==0 or n%3==0:
        return True
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def main():

    print(prime_check(23))

if __name__=="__main__":
    main()