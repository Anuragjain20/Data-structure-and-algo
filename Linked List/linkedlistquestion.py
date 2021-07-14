from LINKEDLISTINTER import LinkedList

def removeDups(ll):
    if ll.head is None:
        return 
    else:
        currNode = ll.head
        visited = set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll


def removeDups1(ll):
    if ll.head is None:
        return 
    else:
        currNode = ll.head
        
        while currNode:
            runner = currNode
            while runner.next:
                if runner.next.value ==  currNode.value :
                    runner.next = runner.next.next
                else:
                    runner = runner.next       
            currNode = currNode.next
        return ll.head



cusromLL = LinkedList()
cusromLL.generate(10,0,99)
print(cusromLL)
removeDups1(cusromLL)
print(cusromLL)


#2

def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1    


print("||||||||||||||||||||||||||||||||||||||||||")
cusrLL = LinkedList()
cusrLL.generate(10,0,99)
print(cusrLL)
print(nthToLast(cusrLL,3))
print(cusrLL)



#3 . partition
def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        
        
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

print("---------------------")
s = LinkedList()
s.generate(20,0,99)
print(s)
partition(s,40)
print(s)



#4. addition
def sumList(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next            
        ll.add(int(result % 10))
        carry = result/10

    return ll    

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print("=========================================")
print(llA)
print(llB)
print(sumList(llA,llB))



#5. intersection
from LINKEDLISTINTER import Node

def intersection(llA,llB):
    if llA.tail is  not llB.tail :
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA


    diff = len(longer) - len(shorter)

    longerNode  = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode =   shorterNode.next 
        longerNode = longerNode.next 

    return longerNode     

#Helper
def addSameNode(llA,llB,value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()    
llA.generate(3,0,10)
llB = LinkedList()  
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)

print("**********************")
print(llA)
print(llB)
print(intersection(llA,llB))















