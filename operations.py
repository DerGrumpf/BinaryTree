from binarytree import BinTree

def addValue(tree, value):
    tvalue = tree.getItem()
    if tvalue >= value:
        if tree.getLeft() == None:
            tree.setLeft(value)
        else:
            addValue(tree.getLeft(), value)
    else:
        if tree.getRight() == None:
            tree.setRight(value)
        else:
            addValue(tree.getRight(), value)
