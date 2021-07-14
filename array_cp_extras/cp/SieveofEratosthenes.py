#generating all prime numbers upto n
from math import sqrt
def genPrimes(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    for i in range(2,int(sqrt(n))+1):
        if prime[i] == True:
            for j in range(i*i,n+1,i):
                prime[j] = False

    for i in range(0,len(prime)):
        if prime[i] == True:
            print(i,end=" ")

genPrimes(11)                        

#o(root(n))