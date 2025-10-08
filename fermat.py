def fermat(p,a):
    if p<=1:
        raise ValueError("Error")
    if a%p ==0:
        return 0
    
    return pow(a,p-1,p)

def main():
    ans = fermat(13,6)
    print(ans)
    
if __name__=="__main__":
    main()
        