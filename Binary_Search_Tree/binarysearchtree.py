import queuelinkedlist as queue
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue  <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)         
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)                  


newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,60)
insertNode(newBST,33)
insertNode(newBST,72)
insertNode(newBST,61)
insertNode(newBST,2)
insertNode(newBST,73)
insertNode(newBST,16)
insertNode(newBST,123)
def preOrdertraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrdertraversal(rootNode.leftChild)
    preOrdertraversal(rootNode.rightChild) 

preOrdertraversal(newBST)     


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


print("--------------------------------------\n -----------------------------")
inOrderTraversal(newBST)



def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("--------------------------------------\n -----------------------------")
postOrderTraversal(newBST)


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
levelOrderTraversal(newBST)


def searchNode(rootNode,nodevalue):
    if rootNode.data == nodevalue:
        print("the value is found")
    elif nodevalue < rootNode.data:
        if rootNode.leftChild.data == nodevalue:
            print("the value is found")
        else:
            searchNode(rootNode.leftChild,nodevalue)
    else:
        if rootNode.rightChild.data == nodevalue:
            print("the value is found")
        else:
            searchNode(rootNode.rightChild,nodevalue)                       

searchNode(newBST,72)


def minValueNode(bstNode):
    current = bstNode
    while(current.leftChild is not None):
        current  = current.leftChild
    return current

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode 
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return  temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChlid
            rootNode =None
            return temp

        temp = minValueNode(rootNode.rightChild)   
        rootNode.data = temp.data
        rootNode.rightChild =  deleteNode(rootNode.rightChild,temp.data)
        
    return rootNode    
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

deleteNode(newBST,60)
levelOrderTraversal(newBST)
