from binarytree import BinTree

global order
order = []

def postOrder(tree):
    if tree.getLeft() != None:
        postOrder(tree.getLeft())

    if tree.getRight() != None:
        postOrder(tree.getRight())

    save.add(tree.getItem())

def preOrder(tree):
    save.add(tree.getItem())

    if tree.getLeft() != None:
        preOrder(tree.getLeft())

    if tree.getRight() != None:
        preOrder(tree.getRight())

def inOrder(tree):
    if tree.getLeft() != None:
        inOrder(tree.getLeft())

    save.add(tree.getItem())

    if tree.getRight() != None:
        inOrder(tree.getRight())
