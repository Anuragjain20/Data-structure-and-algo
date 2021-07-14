class Stack:
    def __init__(self,maxSize):
        self.list = []
        self.maxSize = maxSize
    def __str__(self):
        values = self.list.reverse
        values = [str(x) for x in self.list]
        return "\n".join(values)
    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #  isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # Push
    def push(self,value):
        if self.isFull():
            print("Stack is full")
        else:
            self.list.append(value)  

    # Pop
    def pop(self,value):
        if self.isEmpty():
            return "stack empty"
        else:
            return self.list.pop()

    
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]     
    #  delete
    def delete(self):
        self.list = None





customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)        


