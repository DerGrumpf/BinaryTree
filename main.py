'''Animate Binary tree with kivy'''
__author__ = 'DerGrumpf'

import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.metrics import dp
from kivy.properties import NumericProperty, ListProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

from random import randint

class Node(FloatLayout):
    radius = NumericProperty(dp(50))
    value = 0
    right = None
    left = None

    def __init__(self, x, y, value):
        self.value = value
        super(Node, self).__init__()
        self.x = x - self.radius/2
        self.y = y - self.radius/2


kv = '''
<Node>:
    pos: self.x, self.y
    size_hint: None, None
    width: self.radius
    height: self.width
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Ellipse:
            pos: self.pos
            size: root.size
    Label:
        pos: root.pos
        color: 0,0,0,1
        size: self.texture_size
        text: str(root.value)

<TreeAnimateRoot>:
    Button:
        text: ''
        on_press: root.animate()
'''
Builder.load_string(kv)

class TreeAnimateRoot(FloatLayout):
    def __init__(self):
        super(TreeAnimateRoot, self).__init__()
        self.animate()

    def animate(self):
        self.canvas.clear()
        self.root = Node(Window.size[0]/2, Window.size[1]*.9, randint(45, 50))
        self.add_widget(self.root)
        for i in range(30):
            n = self.addNode(self.root, randint(25,75))
            self.add_widget(n)

    def addNode(self, node, value):
        if node.value >= value:
            if node.left == None:
                node.left = Node(node.x*.9, node.y*.9, value)
                with self.canvas:
                    Color(1,1,1,1)
                    Line(points=(node.x+node.radius/2, node.y+node.radius/2,
                        node.left.x+node.radius/2, node.left.y+node.radius/2))
                return node.left
            else:
                return self.addNode(node.left, value)
        else:
            if node.right == None:
                node.right = Node(node.x*1.2, node.y*.9, value)
                with self.canvas:
                    Color(1,1,1,1)
                    Line(points=(node.x+node.radius/2, node.y+node.radius/2,
                        node.right.x+node.radius/2, node.right.y+node.radius/2))
                return node.right
            else:
                return self.addNode(node.right, value)


class TreeAnimate(App):
    def __init__(self):
        super(TreeAnimate, self).__init__()
    def build(self):
        return TreeAnimateRoot()

if __name__ == '__main__':
    TreeAnimate().run()
