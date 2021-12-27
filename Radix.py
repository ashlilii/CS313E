#  File: Radix.py

#  Description: Radix Sort algorithm that sorts integers and lowercase letters

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # queue list is buckets
  queue_list = []
  char_guide = ascii_converter()
  max_length = get_max_length(a)
  
  for x in char_guide:
    queue_list.append(Queue())
  queue_list.append(Queue())

  for i in range(len(a)):
    while (len(a[i]) < max_length):
      a[i] = a[i] + ' '
    

  # goes through each index
  for i in range(max_length):
    for string in a:
      if len(string) == 1:
        index = char_guide[string[0]]
        queue_list[index].enqueue(string)
      elif len(string) > 1:
        if i == (max_length - 1):
          index = char_guide[string[0]]
          queue_list[index].enqueue(string)
        elif len(string) <= i + 1:
          index = char_guide[string[1]]
          queue_list[index].enqueue(string)
        else:
          index = char_guide[string[-(i + 1)]]
          queue_list[index].enqueue(string)

    # empties a for each index and refills it with semi sorted list a      
    a = []
    for queue in queue_list:
      for size in range(queue.size()):
        a.append(queue.dequeue())

  for i in range(len(a)):
    a[i] = a[i].strip()
    
  return a

def get_max_length (a):
  max_character = 0
  for i in a:
    character_count = len(i)
    if character_count > max_character:
      max_character = character_count
  return max_character

def ascii_converter ():
  # 0 - 9 is 48 - 57
  # a - z is 97 - 122
  counter = 0
  dictionary = {}
  # placeholder
  dictionary[' '] = 0

  # numbers
  for i in range(48,58):
    counter += 1
    dictionary[chr(i)] = counter

  # letters
  for i in range(97,123):
    counter += 1
    dictionary[chr(i)] = counter

  return dictionary
  
def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()
