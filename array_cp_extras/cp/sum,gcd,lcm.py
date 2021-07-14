def sum1(n):
    print((n*(n+1))//2)

sum1(10)
print("----------------------------------- \n -----------")
#---------------------

#euclid algo
#t.c = o(log(min(a,b)))
#product = lcm*gcd
def gcd(a,b):
    if b%a == 0:
        return a
    return gcd(b%a,a)

def lcm(a,b):
    prod = a*b
    hcf = gcd(a,b)
    return prod//hcf


def lg():
    t = int(input())
    while t:
        n,m = map(int,input().split())
        print(f"gcd = {gcd(n,m)}  and  lcm = {lcm(n,m)}")
        t = t-1
lg()        

