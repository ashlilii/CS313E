#  File: Triangle.py

#  Description: Program finds the greatest path sum starting at the top of the triangle and
#  moving only to adjacent numbers on the row below using exhaustive, greedy, recursive,
#  and dynamic

import sys

from timeit import timeit

def brute_force (grid):
  # sets variables
  unit = 0
  row = 0
  path_sum = 0
  path_sum_list = []
  brute_force_helper(grid, row, unit, path_sum, path_sum_list)
  return max(path_sum_list)

def brute_force_helper (grid, row, unit, path_sum, path_sum_list):
  if row == len(grid):
    # collects all path sums
    path_sum_list.append(path_sum)
    pass
  else:
    brute_force_helper(grid, row + 1, unit, path_sum + grid[row][unit], path_sum_list)
    brute_force_helper(grid, row + 1, unit + 1, path_sum + grid[row][unit], path_sum_list)    
  

# returns the greatest path sum using greedy approach
def greedy (grid):
  index = 0
  path_sum = 0
  for row in grid:
    if len(row) == 1:
      path_sum += row[index]
    # programs choose whichever option is more
    elif row[index] >= row[index + 1]:
      path_sum += row[index]
      index = index
    elif row[index + 1] >= row[index]:
      path_sum += row[index+1]
      index += 1
  return path_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  if len(grid) == 1:
    return grid[0][0]
  else:
    # every iteration makes a smaller triangle
    temp_grid = grid[1:]
    grid1 = [row[0:len(row)-1] for row in temp_grid]
    grid2 = [row[1:]for row in temp_grid]
    return grid[0][0] + max(divide_conquer(grid1),divide_conquer(grid2))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
  # starts from bottom up
  for row in range(len(grid) - 2, -1, -1):
    if row == len(grid) -1:
      pass
    for unit in range(0, len(grid[row]) - 1):
      # program makes second to bottom line to choose which ever option is greater
      if grid[row + 1][unit] >= grid[row + 1][unit + 1]:
        # creates a new bottom line by adding the bottom line to the second line
        grid[row][unit] += grid[row + 1][unit]
      elif grid[row + 1][unit + 1] >= grid[row + 1][unit]:
        grid[row][unit] += grid[row + 1][unit + 1]
  return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''
  
  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is\n" + str(brute_force(grid))\
        + "\n" + "The time taken for exhaustive search in seconds is\n" + str(times) + "\n")

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is\n" + str(greedy(grid))\
        + "\n" + "The time taken for greedy search in seconds is\n" + str(times) + "\n")

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is\n" + str(divide_conquer(grid))\
        + "\n" + "The time taken for recursive search in seconds is\n" + str(times) + "\n")

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through exhaustive search is\n" + str(dynamic_prog(grid))\
        + "\n" + "The time taken for exhaustive search in seconds is\n" + str(times) + "\n")

if __name__ == "__main__":
  main()
