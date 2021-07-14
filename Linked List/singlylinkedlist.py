"""
class Node:
    def __init__(self,value =None):
        self.value = value
        self.next = Node
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

"""
class Node:
    def __init__(self,value =None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insertion in sll
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                try:
                    tempNode = self.head
                    index =0
                    while index < location-1:
                        tempNode = tempNode.next
                        index +=1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                except :
                    
                    print("no such loaction "+ str(location))
    #traversal                    
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node  = self.head
            while node is not None:
                print(node.value)
                node = node.next
            
    #search
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "the list does not exist"
        else:
            index = 0
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                        return "value is : " + str(node.value) + " it is present at : "+ str(index)
                node= node.next
                index+=1
            return "The value does not exist in this list"    
    #delete node 
    def deleteNode(self,location):
        if self.head is None:
            print("the SLL does not exists")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    n = self.head
                    while n is not None:
                        if n.next == self.tail:
                            break
                        n = n.next
                    n.next = None
                    self.tail = n
            else:
                try:
                    index = 0 
                    n = self.head
                    while index<location-1:
                        n = n.next
                        index +=1
                    n1 = n.next      
                    n.next = n1.next 
                except:
                    print("no such location : " + str(location))

                    
    #delete entire list
    def deleteEntireSLL(self):
        if self.head is None:
            print("the sll does not exits")
        else:
            self.head = None
            self.tail = None
                        
        
s = SLinkedList()
s.insertSLL(1,1)
s.insertSLL(2,1)
s.insertSLL(3,1)
s.insertSLL(4,1)


print([node.value for node in s])
s.deleteNode(4)
s.traverseSLL()
s.searchSLL(3)
s.deleteEntireSLL()
print([node.value for node in s])