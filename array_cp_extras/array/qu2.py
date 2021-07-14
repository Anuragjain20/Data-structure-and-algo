#Set both elements of a binary array to 0 in a single line


def so(arr):
    arr[0] = arr[1] = arr[not arr[1]]

arr1 = [1,0] 
arr2 = [0,0]
arr3 = [1,1]
arr4 = [0,0]


so(arr1)
so(arr2)
so(arr3)
so(arr4)

print(arr1,arr2,arr3,arr4,sep = "==========")