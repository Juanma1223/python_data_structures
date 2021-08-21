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

class Tree:
    root = None

    def __init__(self,value): 
        newNode = Node(value)
        self.root = newNode