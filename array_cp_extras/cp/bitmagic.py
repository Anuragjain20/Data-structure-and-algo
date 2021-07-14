def evenodd(n):
    if n & 1 == 1:
        print("odd")
    else:
        print("even")    

#righthift : >> is divide in power of 2
# leftshift : << is multiply in power of 2
       
#-----------------------------------
# ispowerof 2
# n->input
# True/False -> output
# check if n is a powerof 2
# 512->True 512 = 2**9

def ispowerof2(n):
    if n<=0:
        return False
    x = n    
    y = not (n & (n-1))
    return x and y

def brutecnt(n):
    #O(n)
    s =str(bin(n))[2:]
    return s.count('1')
def cntbits(n):
    #logn
    cnt = 0
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt    

