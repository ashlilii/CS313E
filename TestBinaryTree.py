#  File: TestBinaryTree.py

#  Description: This program implements 4 functions that test a binary tree

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
    # self.parent = None
    # self.visited = False

  def __str__ (self):
    s = ''
    return s

class Tree (object):
  def __init__ (self):
    self.root = None
    # self.size = 0

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
                current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # Returns true if two binary trees are similar
  def is_similar (self, pNode): 
      return self.similar_helper(self.root, pNode, pNode.root)

  # takes in two trees and a specific node
  def similar_helper(self, aNode, p, pNode):
      # if aNode exists
      if aNode:
          # if pNode doesn't exist or if their data isn't equal
          if pNode == None or aNode.data != pNode.data:
              return False
          # if we can keep going down the tree, go down
          return self.similar_helper(aNode.lChild, p, pNode.lChild) and self.similar_helper(aNode.rChild, p, pNode.rChild)
      # if aNode doesn't exist, return the existence of pNode to confirm that the trees are equal
      return pNode == None          

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
      l = []
      self.level_helper(level, 0, self.root, l)
      return l
  
  # takes a specified, level, the level you're on, the current node, and the list you're appending
  def level_helper(self, level, start, aNode, l):
      if aNode:
          # if on the level, append the node
          if start == level:
              l.append(aNode)
          # otherwise, keep going down
          else:
              self.level_helper(level, start + 1, aNode.lChild, l)
              self.level_helper(level, start + 1, aNode.rChild, l)
      
  # Returns the height of the tree
  def get_height (self): 
    return self.height_helper(self.root, -1)
  
  # takes in the current node and the current height
  def height_helper(self, aNode, height):
    # if the node exists, add one to height and keep going
    if aNode:
      # return the max height of each tree
      return max(self.height_helper(aNode.lChild, height + 1), self.height_helper(aNode.rChild, height + 1))
    # if the branch is done, return its height
    return height 
      

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    return self.num_helper(self.root)
  
  def num_helper(self, aNode):
    # if the node exists, add to the count
    if aNode:
      return 1 + self.num_helper(aNode.lChild) + self.num_helper(aNode.rChild)
    # if it doesn't exist, return 0
    return 0

def main():
    # Create three trees - two are the same and the third is different
    line = "50 30 70 10 40 60 80 7 25 38 47 58 65 77 96"
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    line = "50 30 70 10 40 60 80 7 25 38 47 58 65 77 96"
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)

    line = "58 77 65 30 38 50 7 25 47 96 80 10 60 70 40"
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)

    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    print(tree1.is_similar(tree3))

    # Print the various levels of two of the trees that are different
    print(tree1.get_level(0))
    print(tree1.get_level(1))
    print(tree1.get_level(2))
    print(tree1.get_level(3))
    print(tree3.get_level(0))
    print(tree3.get_level(1))
    print(tree3.get_level(2))
    print(tree3.get_level(3))
    print(tree3.get_level(4))
    print(tree3.get_level(5))

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
    print(tree3.num_nodes())

if __name__ == "__main__":
  main()
