from stackUsingLL import Stack

def minimumBracketReversal(s):

    n= len(s)
    if n == 0:
        return 0
    if n%2 != 0:
        return -1     
    
    stack = Stack()

    for i in range(n):
        cur = s[i]

        if cur == '{':
            stack.push(cur)

        else:
            if stack.isEmpty() == False and stack.top() == '{' :
                stack.pop()
            else:
                stack.push(cur)

    count = 0

    while stack.isEmpty() == False:
        c1 = stack.top()
        stack.pop()
        c2 = stack.top()
        stack.pop()

        if c1 == c2:
            count += 1
        else:
            count+=2


    return count


r = '{{{{}}}}{{'
j =  '{{{}}{}{'
e = '{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}' 
p = [r,j,e]
for i in p:
    print(minimumBracketReversal(i))

