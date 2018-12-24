#Playground

from binarytree import *
from operations import *
from traversels import *

def example1():
    import random
    print('Example1:')
    print()

    t = BinTree(random.randint(1,100))
    for i in range(1,10):
        addValue(t, random.randint(1,100))

    polst = []
    prlst = []
    inlst = []

    def call(value):
        print(value)

    print('Post Order:')
    postOrder(t, call)
    print()

    print('Pre Order:')
    preOrder(t, call)
    print()

    print('In Order:')
    inOrder(t, call)
    print()

def example2():
    from random import randint
    print('Example2:')
    t = BinaryTree(randint(1,100))
    t.addNode(randint(1,100)) #Add one Value
    t.addNodes([randint(1,100) for i in range(3)]) #Add list items
    t.addNodes((randint(1,100), randint(1,100), randint(1,100))) #Add tuple items
    t.addNodes(randint(1,100),randint(1,100)) #Add overloaded arguments
    print('Post Order:', t.getPostOrder())
    print('Pre  Order:', t.getPreOrder())
    print('In   Order:', t.getInOrder())

if __name__ == '__main__':
    example1()
    example2()
