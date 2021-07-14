#prime numbers two factors
#approach one  O(n)
#approach two : base case + hint : O(1)-->O(root(n))
from math import sqrt

def approach1(n):
    divcnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            divcnt+=1
    if divcnt == 2:
        return True
    else:
        return False

def approach2(n):
    if n == 0 or n  == 1:
        return False
    if n ==2 or n ==3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5,int(sqrt(n))+1):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True        




for _ in range(int(input())):
    n = int(input())
    
    print(approach1(n))
    
    print(approach2(n))