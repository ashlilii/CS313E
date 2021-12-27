#  File: TestLinkedList.py

#  Description: Linked List class 

class Link (object):
  def __init__(self, data):
    self.next = None
    self.data = data

  def __str__(self):
    return str(self.data)

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.head = None
    self.tail = None
    self.length = 0

  # get number of links 
  def get_num_links (self):
    return self.length

  # add an item at the beginning of the list
  def insert_first (self, data): 
    new = Link(data)
    if self.length == 0:
      self.head = new
      self.tail = new
    else:
      new.next = self.head
      self.head = new
    self.length += 1 

  # add an item at the end of a list
  def insert_last (self, data): 
    new = Link(data)
    if self.length == 0:
      self.head = new
      self.tail = new 
    else:
      self.tail.next = new
      self.tail = new 
    self.length += 1

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    new = Link(data)
    if self.length == 0:
      self.head = new
      self.tail = new
    # if it's first
    elif self.head.data >= new.data:
        self.insert_first(new.data)
    # if it's last 
    elif self.tail.data <= new.data:
        self.insert_last(new.data)
    # if it's in between 
    else:
      currNode = self.head
      while currNode.data < new.data:
        previous = currNode
        currNode = currNode.next
      new.next = currNode
      previous.next = new 
    self.length +=1    

  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    if self.length == 0:
      return None
    else:
      currNode = self.head
      while currNode:
        if currNode.data == data:
          return currNode
        currNode = currNode.next
    return None 

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    if self.length == 0:
      return None
    else:
      currNode = self.head
      while currNode:
        if currNode.data == data:
          return currNode
        elif currNode.data > data:
          return None 
        currNode = currNode.next
    return None 

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    if self.length == 0:
      return None
    # if the head is the link
    elif self.head.data == data:
      a = self.head
      self.head = self.head.next
      self.length -= 1 
      return a
    else:
      currNode = self.head
      previous = self.head 
      while currNode:
        # if the current node is the data 
        if currNode.data == data:
          self.length -= 1
          previous.next = currNode.next
          return currNode
        previous = currNode
        currNode = currNode.next
    return None 

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    if self.length == 0:
      return ""
    else:
      # set up for the head
      s = ""
      s += str(self.head) + "  "
      c = 1
      currNode = self.head.next
      while currNode:
        s += str(currNode) + "  "
        c += 1
        # every 10 characters 
        if c == 10:
          s += "\n"
          c = 0
        currNode = currNode.next
      return s 

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    new = LinkedList()
    # if it's empty 
    if self.length == 0:
      return new
    currNode = self.head
    while currNode:
      new.insert_last(currNode.data)
      currNode = currNode.next
    return new

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self):
    new = LinkedList()
    # if it's empty 
    if self.length == 0:
      return new
    currNode = self.head
    while currNode:
      new.insert_first(currNode.data)
      currNode = currNode.next
    return new

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    new = LinkedList()
    # if it's empty 
    if self.length == 0:
      return new
    currNode = self.head
    while currNode:
      new.insert_in_order(currNode.data)
      currNode = currNode.next
    return new

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    # if it's 0 or 1 long
    if self.length <= 1:
      return True
    previous = self.head
    currNode = self.head.next
    while currNode:
      # if it's not ascending 
      if currNode.data <= previous.data:
        return False
      previous = currNode
      currNode = currNode.next
    return True
    
  # Return True if a list is empty or False otherwise
  def is_empty (self):
    return self.length == 0

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    new = LinkedList()
    currNode = self.head
    # adds first list
    while currNode:
      new.insert_in_order(currNode.data)
      currNode = currNode.next
    currNode = other.head
    # adds second list
    while currNode:
      new.insert_in_order(currNode.data)
      currNode = currNode.next
    return new 

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    # if they're both empty 
    if self.length == 0 and other.length == 0:
      return True
    s_current = self.head
    other_current = other.head

    while s_current:
      # if it's different
      if s_current.data != other_current.data:
        return False
      s_current = s_current.next
      other_current = other_current.next
      # if one of them ends 
      if s_current.next == None or other_current == None:
        if s_current.next == None and other_current.next == None:
          return True
        return False 
    return True 

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    new = LinkedList()
    l = []
    if self.length == 0:
      return new
    # if it's length 1
    elif self.length == 1:
      new.insert_last(self.head)
      return new
    else:
      currNode = self.head
      while currNode:
        # if it's not a duplicate
        if currNode.data not in l:
          l.append(currNode.data)
          new.insert_last(currNode.data)
        currNode = currNode.next
    return new 

def main():

  # will be using print statements instead of assert as allowed by piazza note #647

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  a = LinkedList()
  for i in range(15):
    a.insert_first(i)
  print(a)

  # Test method insert_last()
  a.insert_last(42)
  print(a)

  # Test method insert_in_order()
  a.insert_in_order(23)
  print(a)

  # Test method get_num_links()
  print(a.get_num_links())

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there
  print(a.find_unordered(23))
  print(a.find_unordered(24)) 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there
  a = a.sort_list()
  print(a.find_ordered(14))
  print(a.find_ordered(36))

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  a.delete_link(13)
  print(a)
  a.delete_link(37)
  print(a)

  # Test method copy_list()
  b = a.copy_list()
  print(b)

  # Test method reverse_list()
  c = a.reverse_list()
  print(c)

  # Test method sort_list()
  d = c.sort_list()
  print(d)

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print(d.is_sorted())
  print(c.is_sorted())

  # Test method is_empty()
  e = LinkedList()
  print(e)
  print(d)

  # Test method merge_list()
  o = LinkedList()
  for i in range(10):
    o.insert_last(i)
  p = LinkedList()
  for i in range(10,20):
    p.insert_list(i)
  m = o.merge_list(p)
  print(m)

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  g = b.copy_list()
  print(g.is_equal(b))

  # Test remove_duplicates()
  o = LinkedList()
  for i in range(10):
    o.insert_last(i)
  for i in range(8,20):
    o.insert_list(i)
  z = o.remove_duplicates()
  print(z)

  return 

if __name__ == "__main__":
  main()
