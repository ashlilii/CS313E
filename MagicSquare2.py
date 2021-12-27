#  File: MagicSquare.py

#  Description: Prints all possible Magic Squares

import sys

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):

    # declares constants
    n = int(len(a) ** .5)
    constant = int(n * (n**2 + 1) / 2)
    hi = len(a)
    
    # checks each of the rows
    for i in range(n):
        rowc = constant
        for j in range(n):
            rowc -= a[i*n + j]
        if rowc!= 0:
            return False

    # checks each of the columns
    for i in range(n):
        colc = constant 
        for j in range(n):
            colc -= a[j*n + i]
        if colc!= 0:
            return False
    
    # checks the first diagonal 
    s = constant
    for j in range(n):
        s -= a[j*(n-1)+n-1]
    if s != 0:
        return False 

    # checks the last diagonal    
    return (sum(a[0:hi:n+1]) == constant)   

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# function stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):

    # declares a bunch of constants
    n = int(len(a) ** .5)
    constant = int(n * (n**2 + 1) / 2)
    hi = len(a)

    #calls wrapper 
    helper(a, idx, all_magic, n, constant, hi)

# this helper function does most of the actual recursion
# it takes in the 1d list, the index, the magic squares list
# , the length of the grid, the magical constant, and the length
# of the list 
def helper(a, idx, all_magic, n, constant, hi):

  # base case 
  if (idx == hi):
      all_magic.append(a.copy())
  else:
      #checks each row until the last one
      if ((idx + 1) % n == 0 and idx < hi - 1):
        for i in range (idx, hi):

            # gets the sum of each row 
            a[idx], a[i], = a[i], a[idx]
            s = constant
            k = int((idx+1)/n)
            for j in range(n):
                s -= a[j + (k-1)*n]

            #if the sum is equal to the constant, it permutes             
            if s == 0:
                helper(a, idx+1, all_magic, n, constant, hi)
            a[idx], a[i], = a[i], a[idx]

      # check the columns as they are created
      elif n**2 - 2*n <= idx < n**2 - n:
          for i in range(idx, hi):

              # gets the sum of each column
              a[idx], a[i] = a[i], a[idx]
              column = idx % n
              s = 0
              for j in range(n-1):
                  s += a[n * j + column]
              predict = constant - s

              # if the prediction is valid (range and not used so far), it permutes 
              if 1 <= predict <= n**2 and predict not in a[:idx]:
                helper(a, idx+1, all_magic, n, constant, hi)
              a[idx], a[i], = a[i], a[idx]
      
      # checks first diagonal
      elif n**2 - n == idx:

          # gets the sum of the diagonal
          for i in range(idx, hi):
              a[idx], a[i] = a[i], a[idx]
              s = constant
              for j in range(n):
                  s -= a[j*(n-1)+n-1]

              # if the sum equals the constant, it permutes     
              if s == 0:
                  helper(a, idx+1, all_magic, n, constant, hi)
              a[idx], a[i], = a[i], a[idx]

      # final test for magic square (second diagonals and sum of each row)
      elif idx + 1 == hi:
          for i in range(idx, hi):
               a[idx], a[i] = a[i], a[idx]

               # if it is a magic square, it permutes 
               if is_magic(a):
                   helper(a, idx+1, all_magic, n, constant, hi)
               a[idx], a[i] = a[i], a[idx]

      # if all conditions have been met, permutes
      else:
          for i in range (idx, hi):
            a[idx], a[i] = a[i], a[idx]
            helper(a, idx+1, all_magic, n, constant, hi)
            a[idx], a[i] = a[i], a[idx]


def main():
  # read the dimension of the magic square
  line = sys.stdin.readline()   
  line = line.strip()
  n = int(line) 

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  a = list(range(1, n**2+1))

  # generate all magic squares using permutation 
  permute(a, 0, all_magic)

  # print all magic squares
  for square in all_magic:
    print (square)

if __name__ == "__main__":
  main()
