import random

def prime(n,k):
    if(n <= 1):
        return False
    if(n%2 == 0 or n%3 == 0):
        return False
    d,r = n-1,0
    while(d%2 == 0):
        d//=2
        r+=1
    for _ in range(k):
        if(miller(n,d,r) == False):
            return False
    return True

def miller(n,d,r):
    a = random.randint(2,n-2)
    x = pow(a,d,n)
    if(x == 1 or x == n-1):
        return True
    for _ in range(r-1):
        x = (x*x)%n
        if(x == n-1):
            return True
        if(x == 1):
            return False
    return False
    
def main():
    ans = prime(25,5)
    print(ans)

if(__name__=="__main__"):
    main()