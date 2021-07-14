class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next 


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head ==  None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node  

    def pop(self):

        if self.isEmpty():
            return "stack is empty"
        else:
            t = self.LinkedList.head.value   
            self.LinkedList.head = self.LinkedList.head.next      
            return t

    def peek(self):

        if self.isEmpty():
            return "stack is empty"
        else:
            t = self.LinkedList.head.value 
            return t


    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())  

print(customStack)