from binarytree import BinTree

def addValue(tree, value):
    tvalue = tree.getItem()
    if tvalue >= value:
        if tree.getLeft() == None:
            tree.setLeft(BinTree(value))
        else:
            addValue(tree.getLeft(), value)
    else:
        if tree.getRight() == None:
            tree.setRight(BinTree(value))
        else:
            addValue(tree.getRight(), value)

def searchValue(tree, value):
    flag = False
    if tree != None:
        tvalue = tree.getItem()
    else:
        if tvalue == value:
            flag = True
        else:
            if not tree.isLeaf():
                if tvalue >= value:
                    if tree.getLeft != None:
                        flag = searchValue(tree.getLeft(), value)
                else:
                    if tree.getRight != None:
                        flag = searchValue(tree.getRight(), value)
    return flag
