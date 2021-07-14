class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children
    def __str__(self,level = 0):  
        ret = " "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret     

    def addChild(self,TreeNode):
        self.children.append(TreeNode)    



tree = TreeNode("drinks",[])
cold = TreeNode("cold",[])
hot = TreeNode("Hot",[])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("Tea",[])
coffee = TreeNode("Coffee",[])
cola = TreeNode("cola",[])
fanta = TreeNode("fanta",[])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)
