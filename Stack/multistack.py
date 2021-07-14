#1. Three in One

class MultiStack:
    def __init__(self,stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize*self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def print(self):
        print(self.custList)    

    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty( self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else: 
            return False

    def indexOfTop(self,stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1 


    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "the stack is full"
        else:
            self.sizes[stacknum] +=1
            self.custList[self.indexOfTop(stacknum)] = item


    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "the stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)] 
            self.custList[self.indexOfTop(stacknum)] =  0
            self.sizes[stacknum] -= 1     
            return value       


    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "the stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)] 
    
            return value       



c = MultiStack(5)
c.push(22,1)
c.push(221,1)
c.push(212,1)
c.push(2211,1)
c.push(222,2)
c.push(2221,2)
c.push(21221,2)
c.push(221111,2)
c.push(3,0)
print(c.peek(1))
print(c.peek(2))
c.print()
