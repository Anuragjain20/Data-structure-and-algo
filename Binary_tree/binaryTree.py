import queuelinkedlist as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        



newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrdertraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrdertraversal(rootNode.leftChild)
    preOrdertraversal(rootNode.rightChild) 

preOrdertraversal(newBT)     


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


print("--------------------------------------\n -----------------------------")
inOrderTraversal(newBT)



def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("--------------------------------------\n -----------------------------")
postOrderTraversal(newBT)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)           

print("-------------------------------------- \n -----------------------------")
levelOrderTraversal(newBT)


def searchBT(rootNode,nodevalue):
    if not rootNode:
        return " the bt does not exists"
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()     
            if root.value.data == nodevalue:
                return "Success"
            if(root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)                
        return "Unsuccess"
print('************************\n***********')
print(searchBT(newBT,"Tea"))  
print(searchBT(newBT,"T"))  


def insertNode(rootNode,newNode):
    if not rootNode :
        rootNode = newNode
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()     
            if(root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return


            if(root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)            
            else:
                root.value.rightChild = newNode
                return
print("||||||||||||||||||||||||||||||||||||||||||||||")
newnode = TreeNode("Cola")
newnode1 = TreeNode("Col")

insertNode(newBT,newnode)
insertNode(newBT,newnode1)
levelOrderTraversal(newBT)
preOrdertraversal(newBT)             


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if(root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)         
        deepestNode = root.value
        return deepestNode       

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.value  is dNode:
                root.value = None
            if root.value.rightChild :
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                else:    
                    customqueue.enqueue(root.value.rightChild)         
            if root.value.leftChild :
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                else:    
                    customqueue.enqueue(root.value.leftChild)         

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "root node does not exist"
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "deleted" 
            if(root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)                    
        return "failed"

print("===========")

deleteNodeBT(newBT,"Tea")
levelOrderTraversal(newBT)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

deleteBT(newBT)
levelOrderTraversal(newBT)    
