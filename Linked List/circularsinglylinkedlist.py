"""
class Node:
    def __init__(self,value =None):
        self.value = value
        self.next = None
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    def createCSLL(self,nodeValue): #.............o(1)
        node = Node(nodeValue)
        node.next = node
        self.head =node
        self.tail = node
        return "circular ll is created"

     
    
    
csl = CircularSinglyLinkedList()
csl.createCSLL(2)
print([node.value for  node in csl])

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):  # .............o(1)
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "circular ll is created"

    # insertion of node
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                try:
                    r = self.head
                    index = 0
                    while index < location-1:

                        r = r.next
                        index += 1

                    nextNode = r.next
                    r.next = newNode
                    newNode.next = nextNode

                except:
                    print("no such index to insert")

    # traversal

    def traversalCSLL(self):
        if self.head is None:
            print("no element in  list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    #search
    def searchCSLL(self,nodeValue):
        if self.head == None:
            return "there no not any node you are seacrhing for"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "node does not exists"    

    #delete
    def deleteNode(self,location):
        if self.head == Node:
            print("nothing to delete list empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next  = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                try:
                    tempNode = self.head
                    index = 0
                    while index < location -1:
                        tempNode = tempNode.next
                        index += 1
                    tempnode.next = tempNode.next.next         
                except :
                    print("no such node")
    #delete entire list
    def deleteEntireCLL(self):
        if self.head is None:
            print("the sll does not exits")
        else:
            self.head = None
            self.tail = None                    


cll = CircularSinglyLinkedList()
cll.createCSLL(100)
cll.insertCSLL(1, 0)
cll.insertCSLL(3, 0)
cll.insertCSLL(4, 1)
cll.insertCSLL(2, 44)
print([c.value for c in cll])
cll.traversalCSLL()
print(cll.searchCSLL(3))
cll.deleteNode(1)
print([c.value for c in cll])
