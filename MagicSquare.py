#  File: MagicSquare.py

#  Description: Program creates a magic n-by-n square based on inputs given.

import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    #creating square
    magicSquare = []
    for i in range(n):
        magicSquare.append([0] * (n))

    #creating 1 in the middle of the bottom
    x = n - 1
    y = n // 2
    magicSquare[x][y] = 1
    x, y = x + 1, y + 1

    #creating rest of square

    for i in range(2, n ** 2 + 1):
        #checking if position on outer edge
        if x == n:
            x = 0
        if y == n:
            y = 0

        #checking if position is already taken
        if magicSquare[x][y] != 0:
            x, y = x - 2, y - 1

        #updating position
        magicSquare[x][y] = i
        x, y = x + 1, y + 1

    return magicSquare
# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    for list in magic_square:
        print(' '.join(map(str, list)))
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square (magic_square):
    total = sum(magic_square[0])

    #rows
    for row in magic_square:
        if sum(row) != total:
            return False

    #columns
    for y in range(len(magic_square)):
        ctotal = 0
        for row in magic_square:
            ctotal += row[y]
        
        if ctotal != total:
            return False

    #diagnol
    leftTotal = 0
    rightTotal = 0

    for pos in range(len(magic_square)):
        leftTotal += magic_square[pos][pos]
        rightTotal += magic_square[pos][len(magic_square) - pos - 1]

    if (rightTotal or leftTotal) != total:
        return False
    return True
# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers (square, n):
    #get position of number
    x = 0
    y = 0
    doesExist = False
    for i, list in enumerate(square):
        try:
            if list.index(n) != -1:
                x = i
                y = list.index(n)
                doesExist = True
                break
        except ValueError:
            pass
        
    if doesExist == False:
        return 0

    #calculating
    #checking if bottom is there
    if x == len(square) - 1:
        #check bottom right
        if y == len(square) - 1:
            return square[x][y - 1] + square[x - 1][y - 1] + square[x - 1][y]
        #check bottom left
        if y == 0:
            return square[x - 1][y] + square[x - 1][y + 1] + square[x][y + 1]

        return square[x - 1][y] + square[x - 1][y + 1] + square[x][y + 1] + square[x][y - 1] + square[x - 1][y - 1]
        
    #if number is at top
    if x == 0:
        #check top right
        if y == len(square) - 1:
            return square[x + 1][y - 1] + square[x + 1][y] + square[x][y - 1]
        #check top left
        if y == 0:
            return square[x + 1][y] + square[x + 1][y + 1] + square[x][y + 1]

        return square[x + 1][y] + square[x + 1][y + 1] + square[x][y + 1] + square[x + 1][y - 1] + square[x][y - 1]

    #if on right side
    if y == len(square) - 1:
        return square[x][y - 1] + square[x - 1][y - 1] + square[x - 1][y] + square[x + 1][y - 1] + square[x + 1][y]
    
    #if on left side
    if y == 0:
        return square[x + 1][y] + square[x + 1][y + 1] + square[x][y + 1] + square[x - 1][y] + square[x - 1][y + 1]
    
    return square[x + 1][y] + square[x + 1][y + 1] + square[x][y + 1] + square[x - 1][y] + square[x - 1][y + 1] + square[x - 1][y - 1] + square[x + 1][y - 1] + square[x][y - 1]
        
def main():
  # read the input file from stdin
    length = int(sys.stdin.readline())
    checkNumbers = list()
    for line in sys.stdin:
        checkNumbers.append(int(line.strip()))

  # create the magic square
    sq = make_square(length)
  # print the sum of the adjacent numbers 
    for num in checkNumbers:
        print(sum_adjacent_numbers(sq, num))
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
