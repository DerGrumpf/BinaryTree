__author__ = "DerGrumpf"

class BinTree:
    '''Low level Binary Tree implementation'''

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

    def setLeft(self, value):
        if self.left == None:
            self.left = BinTree(value)
        else:
            tree = BinTree(value)
            tree.left = self.left
            self.left = tree

    def setRight(self, value):
        if self.right == None:
            self.right = BinTree(value)
        else:
            tree = BinTree(value)
            tree.right = self.right
            self.right = tree

    def getItem(self):
        return self.value

    def setitem(self, value):
        self.value = value


class BinaryTree:

    '''High level BinaryTree implementation'''

    __postOrderList = []
    __preOrderList  = []
    __inOrderList   = []
    __root = 0

    class Node:
        '''Inner tree node class'''
        right = None
        left = None
        value = None

        def __init__(self, value):
            self.value = value

    def __init__(self, value=0):
        self.__root = self.Node(value)

    def addNodes(self, *data):
        '''Add nodes with more Arguments
        you can use tuples, list or overloaded arguments'''

        check = type(data[0])
        if check == type(tuple()) or check == type(list()):
            temp = data[0]
        else:
            temp = data

        for value in temp:
            self.addNode(value)

    def addNode(self, value):
        '''Add only one node to tree'''
        self.__addNode(self.__root, value)

    def __addNode(self, node, value):
        if node.value >= value:
            if node.left == None:
                node.left = self.Node(value)

            else:
                self.__addNode(node.left, value)
        else:
            if node.right == None:
                node.right = self.Node(value)

            else:
                self.__addNode(node.right, value)

    def postOrder(self):
        '''Post Order traversel implementation'''
        del self.__postOrderList[:]
        self.__postOrder(self.__root)

    def __postOrder(self, node):
        if node.left:
            self.__postOrder(node.left)

        if node.right:
            self.__postOrder(node.right)

        self.__postOrderList.append(node.value)

    def getPostOrder(self):
        '''Get a list with the post order traversel of the tree'''
        self.postOrder()
        return self.__postOrderList

    def preOrder(self):
        '''Pre Order traversel implementation'''
        del self.__preOrderList[:]
        self.__preOrder(self.__root)

    def __preOrder(self, node):
        self.__preOrderList.append(node.value)

        if node.left:
            self.__preOrder(node.left)

        if node.right:
            self.__preOrder(node.right)

    def getPreOrder(self):
        '''Get a list with the pre order traversel of the tree'''
        self.preOrder()
        return self.__preOrderList

    def inOrder(self):
        '''In Order traversel implementation'''
        del self.__inOrderList[:]
        self.__inOrder(self.__root)

    def __inOrder(self, node):
        if node.left:
            self.__inOrder(node.left)

        self.__inOrderList.append(node.value)

        if node.right:
            self.__inOrder(node.right)

    def getInOrder(self):
        '''Get a list with the in order traversel of the tree'''
        self.inOrder()
        return self.__inOrderList
