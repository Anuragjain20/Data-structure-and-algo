#tc = O(n**2) sc = O(n)
def sol1(arr,n,k):
    if(n&1): #if array size is odd then return false
        return 0
    visited = [0]*(n) #for storing the elements that have pair formed
    for  i in range(n-1):
        if visited[i]:
            continue

        j =  i+1
        while(j<n):
            if not visited[j]   and  (arr[i] + arr[j])%k == 0:
                visited[j] = 1
                break 
            j = j+1
        if j == n:
            return 0
    print(visited)
    return 1  

#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

#tc = O(n) sc = O(k)
#n = input k = dividing number

def sol2(arr,n,k):
    if n & 1 :
        return 0

    has = [0]*k
    for i in arr:
        r = i%k
        if r< 0 :
            r = r+k
        has[r] += 1

    if has[0] %2 != 0:
        return 0


    for j in range(1,k):
        if has[j] != has[k-j]:
            return 0

    return 1        
        





            







def main():
    arr = [2, 9, 4, 3, 1, 5,4,2]
    k = 6
    n = 6
    print(sol1(arr,n,k))
    print(sol2(arr,n,k))

main()