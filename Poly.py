#  File: Poly.py

#  Description: This program computes polynomials using linked lists

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):

      new = Link(coeff, exp)

      # if the list is empty
      if self.first == None:
          self.first = new
      
      # if the new link is greater than the list
      elif new.exp >= self.first.exp:
          new.next = self.first
          self.first = new
      else:
          currNode = self.first

          # traverse through the linked list until an element smaller than the inserted element is found 
          while currNode.exp > new.exp:
              previous = currNode
              currNode = currNode.next
              # if it should be inserted at the end
              if currNode == None:
                  previous.next = new
                  return 
          previous.next = new
          new.next = currNode
 
  # ensures that the linked lists don't have values of 0
  def cleaner(self):
      new = LinkedList()
      currNode = self.first
      
      # traverses through list and adds element to new list if the element is not equal to 0
      while currNode:
          if currNode.coeff != 0:
              new.insert_in_order(currNode.coeff, currNode.exp)
          currNode = currNode.next 
      return new 

  # takes in the overall sum, adds self (linked list) to that sum
  def addHelper (self, added):

      currNode = self.first
      # traverses through self 
      while currNode:
        copyCurrNode = added.first
        # traverses through added
        while copyCurrNode:
            # if it's already in added, add the numbers
          if copyCurrNode.exp == currNode.exp:
              copyCurrNode.coeff = currNode.coeff + copyCurrNode.coeff
              break
           # if it's not in added by definition of ordering
          elif copyCurrNode.exp < currNode.exp:
              added.insert_in_order(currNode.coeff, currNode.exp)
              break
            # if added is done traversing
          elif copyCurrNode.next == None:
              added.insert_in_order(currNode.coeff, currNode.exp)
          copyCurrNode = copyCurrNode.next

        currNode = currNode.next
  
  # add polynomial p to this polynomial and return the sum
  def add (self, p):
      if self.first == None:
          return p

      # initializes added with a value of 0 so the function can begin running
      # kind of live recursion helper functions that have a wrapper with 0 as an initial value
      added = LinkedList()
      added.insert_in_order(0,0)

      self.addHelper(added)

      p.addHelper(added)

      return added.cleaner()

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):

      # creates overall product linked list
      product = LinkedList()
      currNode = self.first
      # traverses through self
      while currNode:
        pCurrNode = p.first
        # traverses through p
        while pCurrNode:
            # creates temp linked list with currNode * pCurrNode
            temp = LinkedList()
            temp.insert_in_order(currNode.coeff*pCurrNode.coeff, currNode.exp+pCurrNode.exp)
            # adds it to product
            product = product.add(temp)
            pCurrNode = pCurrNode.next
        currNode = currNode.next

      return product.cleaner()
      
  # create a string representation of the polynomial
  def __str__ (self):
      
      s = ""
      currNode = self.first
      # traverses through self
      while currNode:
          # if it's the last one
          if currNode.next == None:
              s += "(" + str(currNode.coeff) + ", " + str(currNode.exp) + ")"
          # other scenarios
          else:
              s += "(" + str(currNode.coeff) + ", " + str(currNode.exp) + ") + "
          currNode = currNode.next
      
      return s

def main():
  # read data from file poly.in from stdin
  n = int(sys.stdin.readline())

  # create polynomial p
  polyP = LinkedList()
  for i in range(n):
      a = sys.stdin.readline().split(" ")
      polyP.insert_in_order(int(a[0]), int(a[1]))

  sys.stdin.readline()
  # create polynomial q
  m = int(sys.stdin.readline())
  polyQ = LinkedList()
  for i in range(m):
      a = sys.stdin.readline().split(" ")
      polyQ.insert_in_order(int(a[0]), int(a[1]))

  # get sum of p and q and print sum
  print(polyP.add(polyQ))

  # get product of p and q and print product
  print(polyP.mult(polyQ))

if __name__ == "__main__":
  main()
