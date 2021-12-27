#  File: ExpressionTree.py

#  Description: This goes through an expression tree. 

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None

    # this function takes in a string and determines whether or not it's a float
    def is_float(self, x):
        try: 
            float(x)
            return True
        except ValueError:
            return False 

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        # sets up the stack and first node
        expr = expr.split()
        stack = Stack()
        self.root = Node()
        currNode = self.root

        # traverses through the expression
        for i in expr:

            # if it's a (
            if i == "(":
                currNode.lChild = Node()
                stack.push(currNode)
                currNode = currNode.lChild
            
            # if it's an operator
            elif i in operators:
                currNode.data = i 
                stack.push(currNode)
                currNode.rChild = Node()
                currNode = currNode.rChild

            # if it's a float
            elif self.is_float(i):
                currNode.data = (i)
                currNode = stack.pop()
            
            # if it's a )
            elif i == ")":
                if not stack.is_empty():
                    currNode = stack.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode:
            return float(eval(str(self.evaluate(aNode.lChild)) + str(aNode.data) + str(self.evaluate(aNode.rChild))))
        else:
            return ""
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode:
            return str(aNode.data) + " " + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
        else:
            return ""

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode:
            return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + str(aNode.data) + " "
        else:
            return "" 

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
