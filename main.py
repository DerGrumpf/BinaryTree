from binarytree import BinTree
from operations import *
from traversels import *

import random

def main(i=200, j=900):
    stack = []
    tree = BinTree(random.randint(i, j))

    for i in range(1,5):
        addValue(tree, random.randint(i, j))

    for i in range(5):
        x = random.randint(i, j)
        stack.append(searchValue(tree, x))

    print(stack)

if __name__ == '__main__':
    for i in range(10):
        main(5,5)
