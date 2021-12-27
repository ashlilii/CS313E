#  File: Reducible.py

#  Description: Program finds longest English word that can still be a word by reducing
#  one letter at a time

import sys

def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  return const - (hash_word(s, const))

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    idx = hash_word(s, len(hash_table))
    if hash_table[idx] == '':
        hash_table[idx] = s
    else:
        index = 1
        step = step_size(s, 7)
        new_index = (idx + index * step) % len(hash_table)
        while (hash_table[new_index]):
            new_index = (idx + index * step) % len(hash_table)
            index += 1
        hash_table[new_index] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    idx = hash_word(s, len(hash_table))
    if (hash_table[idx] == s):
        return True
    else:
        index = 1
        step = step_size(s, 7)
        new_index = (idx + index * step) % len(hash_table)
        while (hash_table[new_index] and hash_table[new_index] != s):
            new_index = (idx + index * step) % len(hash_table)
            index += 1
        if (hash_table[new_index] == s):
            return True
        else:
            return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def substrings(s):
    sub = []
    word_s = len(s)
    for i in range(word_s):
        sub.append(s[:i] + s[i+1:])
    return sub

def is_reducible(s, hash_table, hash_memo):
    original = False
    if(len(s) == 1 and (s == 'a' or s == 'o' or s == 'i')):
        if find_word(s, hash_memo) is False:
            insert_word(s, hash_memo)
        return True
    if find_word(s, hash_memo) is True:
        return True
    else:
        for sub in substrings(s):
            if find_word(sub, hash_table) is False \
               and (sub != 'i' and sub != 'o' and sub != 'a'):
                continue
            elif is_reducible(sub, hash_table, hash_memo) is True:
                if find_word(s, hash_memo) is False:
                    insert_word(s, hash_memo)
                original = True
        return original
  
  
# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  maxlen = 1
  longest_list = []
  
  for word in string_list:
    if len(word) > maxlen:
      maxlen = len(word)

  for word in string_list:
    if len(word) == maxlen:
      longest_list.append(word)

  return longest_list

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  word_count = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  big_prime = word_count * 2 + 1

  while not is_prime(big_prime):
    big_prime += 2

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  hash_list = ["" for i in range(big_prime)]

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)
  
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  M = int(0.2 * word_count)
  while not(is_prime(M)):
    M += 1

  # populate the hash_memo with M blank strings
  hash_memo = ["" for i in range(M)]

  insert_word("a", hash_memo)
  insert_word("i", hash_memo)
  insert_word("o", hash_memo)

  # create and empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.

  reducible_words = [word for word in word_list if is_reducible(word, hash_list, hash_memo) is True]

  # find the largest reducible words in reducible_words
  reduced = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  reduced.sort()

  # one word per line
  for word in reduced:
    print(word)

if __name__ == "__main__":
  main()
