def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a 

def euler(n):
    result=1
    for i in range(2,n):
        if gcd(i,n)==1:
            result+=1
    return result 

def main():
    answer = euler(10)
    print(answer)