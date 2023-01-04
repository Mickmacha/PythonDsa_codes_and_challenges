##Binary search trees
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        #if the root is empty, then the data is the root
        if not self.root:
            self.root = Node(data) 
        else:
            self.insertNode(data, self.root)
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data) 
    
    def returnMinValue(self):
        if self.root:
            return self.returnMin(self.root)
    def returnMin(self, node):
        if node.leftChild:
            return self.returnMin(node.leftChild)
        return node.data
    
    def returnMaxValue(self):
        if self.root:
            return self.returnMax(self.root)
    def returnMax(self, node):
        if node.rightChild:
            return self.returnMax(node.rightChild)
        return node.data

    def traversal(self):
        if self.root:
            self.traverseInOrder(self.root)
    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)