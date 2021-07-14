from stackUsingLL import Stack
def isBalanced(string):
    s = Stack()
    for i in string:
        if i in '[{(':
            s.push(i)
        elif i == ')':
            if s.isEmpty() or s.top() != '(':
                return False 
            s.pop()        
        elif i == '}':
            if s.isEmpty() or s.top() != '{':
                return False     
            s.pop()
        elif i == ']':
            if s.isEmpty() or s.top() != '[':
                return False     
            s.pop()
    if s.isEmpty():
        return True
    return False               






string = input()
ans = isBalanced(string) 
print(ans)   