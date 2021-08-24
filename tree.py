class Node:
    parent = None
    children = []
    value = None

    def __init__(self,value,parent=None):
        self.parent = parent
        self.value = value

    def addChild(self,value):
        newNode = Node(value,self)
        self.children.append(newNode)
        newNode.parent = self

    def pathToRoot(self):
        currNode = self
        path = []
        while currNode != None:
            path.append(currNode.value)
            currNode = currNode.parent
        return path

class Tree:
    root = None

    def __init__(self,value): 
        newNode = Node(value)
        self.root = newNode

    
