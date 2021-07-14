#o(root(n))
#24 [1,2,3,4,6,8,24]
from math import sqrt
def fun2(n):
    div2 = set()
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)        



def fun1(n):
    #o(n)
    div1 = []
    for i in range(1,n+1):
        if n%i == 0:
            div1.append(i)
    return div1        


for _ in range(int(input())):
    n = int(input())
    div1 = fun1(n)
    print(*div1)
    div2 = fun2(n)
    print(*div2)
