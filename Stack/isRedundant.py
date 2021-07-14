from stackUsingLL import Stack

def isRedundant(sj):
    s = Stack()

    for ch in sj:

        if ch == ')':

            top = s.top()
            s.pop()

            flag = True

            while top != '(':

                if top  in '+-/*':
                    flag = False

                top = s.top()
                s.pop()

            if flag == True:
                return True
        else:
            s.push(ch)                       
    return False


Str = "((a+b))"
print(isRedundant(Str))

Str = "(a+(b)/c)"
print(isRedundant(Str))

Str = "(a+b*(c-d))"
print(isRedundant(Str))