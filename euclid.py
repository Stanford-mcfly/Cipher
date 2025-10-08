def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def main():
    answer = gcd(45,5)
    print(answer)

if __name__ == "__main__":
    main()
