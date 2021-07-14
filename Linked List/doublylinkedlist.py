class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None        

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node =node.next


    #creating list
    def createDLL(self,nodevalue):
        node = Node(nodevalue)            
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    #insertion in list
    def insertNode(self,value,location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next  = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail    
                self.tail.next = newNode
                self.tail = newNode
            else:
                try:
                    tempNode  = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index +=1
                    newNode.next = tempNode.next
                    newNode.prev = tempNode
                    tempNode.next.prev = newNode
                    tempNode.next = newNode       
                except:
                    print("no such location")

    #travesal 
    def traverseDLL(self):
        if self.head is None:
            print("list is empty oh ")
        else:
            tempNode = self.head    
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #reverse traversal
    def reverseTraversalDLL(self):
        if self.head is None:
            print("list is empty")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev           

    #search
    def searchDLL(self,value):
        if self.head is None:
            return "list is empty"
        else:
            index = 0
            tempNode = self.head
            while tempNode:
                if(tempNode.value == value):
                    
                    return "hooray value found " + str(value)
                index+=1
                tempNode = tempNode.next         
            return "badluck no such value"

    #delete Node
    def deleteNode(self,location):
        if self.head is None :
            print("oh no nothing to  delete")
        else:
            if location == 0:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None    
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                try:
                    index = 0
                    tempNode = self.head
                    while index< location-1:
                        tempNode = tempNode.next
                        index += 1
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode
                except:
                    print("no such location")
                                
    # Delete entire Doubly Linked List
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
                


dll = DoublyLinkedList()
dll.createDLL(23)
dll.insertNode(3,4)
dll.insertNode(1,2)
dll.insertNode(11,0)
dll.insertNode(12,1)
dll.insertNode(21,0)
dll.insertNode(212,0)
dll.insertNode(2,3)
dll.traverseDLL()
print("------------------------------")
dll.reverseTraversalDLL()
print([l.value for l in dll]) 
dll.deleteNode(4)
#dll.deleteNode(0)
#dll.deleteNode(1)

dll.deleteDLL()
print([l.value for l in dll])        

print(dll.searchDLL(12))
print(dll.searchDLL(2333))


print("-------------------------------------------")
doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,1)
doubyLL.insertNode(6,2)
print([node.value for node in doubyLL]) 
doubyLL.deleteDLL()
print([node.value for node in doubyLL]) 
