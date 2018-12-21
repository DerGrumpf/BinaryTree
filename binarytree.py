class BinTree:
    right = None
    left = None
    value = None

    def __init__(self, value):
        self.value = value

    def isLeaf(self):
        if (self.right == None) and (self.left == None):
            return True
        else:
            return False

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, tree):
        self.left = tree

    def setRight(self, tree):
        self.right = tree

    def getItem(self):
        return self.value

    def setitem(self, value):
        self.value = value
