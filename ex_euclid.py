def extended_gcd(a,b):
    if a==0:
        return b,0,1
        
    else:
        gcd_va, x1, y1= extended_gcd(b%a,a)
        x= y1-(b//a)*x1
        y = x1
    return gcd_va, x,y
    
def main():
    gcd,x,y = extended_gcd(45,5)
    print(gcd)
    print(x)
    print(y)
    
if __name__ == "__main__":
    main()