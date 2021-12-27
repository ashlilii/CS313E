#  File: Chess.py

#  Description: Program solves the "Eight Queens Problem" for any square board size (1 to 12)

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  # count is added as a new variable
  def recursive_solve (self, col, count):
    if (col == self.n):
      # adds 0 to an empty list and continues to add if there is a solution
      count.append('0')
      return True
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursive_solve(col + 1, count)):
            pass
          self.board[i][col] = '*'
      return False

  # if the problem has a solution, append a 0 to "count" list as a counter
  def solve (self):
    count = []
    self.recursive_solve(0, count)
    return (len(count))

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  num_solutions = game.solve()
  
  # print the number of solutions
  print(num_solutions)
 
if __name__ == "__main__":
  main()
