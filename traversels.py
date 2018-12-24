from binarytree import BinTree

def postOrder(tree, callback):
    if tree.getLeft():
        postOrder(tree.getLeft(), callback)

    if tree.getRight():
        postOrder(tree.getRight(), callback)

    callback(tree.getItem())

def preOrder(tree, callback):
    callback(tree.getItem())

    if tree.getLeft():
        preOrder(tree.getLeft(), callback)

    if tree.getRight():
        preOrder(tree.getRight(), callback)

def inOrder(tree, callback):
    if tree.getLeft():
        inOrder(tree.getLeft(), callback)

    callback(tree.getItem())

    if tree.getRight():
        inOrder(tree.getRight(), callback)
