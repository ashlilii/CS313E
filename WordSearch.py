#  File: WordSearch.py

#  Description: Solves a word search given in an input file by providing all the indices for the start of each word

#  Student Name: Ashley Lee

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 09/03/2021

#  Date Last Modified: 09/03/2021

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
	# read in lines as the following:
	# First line will have one integer - n, the number of lines in the grid and the number of characters in each line.
	# There will be a single blank line.
	# There will be n lines, where each line will have n characters, all in upper case, separated by a space.
	# There will be a single blank line.
	# There will be a single integer k, denoting the number of words that follow.
	# There will be k lines. Each line will contain a single word in all uppercase.
	rows = int(input())
	input()
	word_grid = []
	for i in range(rows):
		word_grid.append(input().strip().replace(" ", ""))
	input()
	word_count = int(input())
	word_list = []
	for i in range(word_count):
		word_list.append(input().strip())
	return word_grid, word_list

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word(grid, word):
	# iterate through every letter on the grid
	row_col_count = len(grid)
	for i in range(row_col_count):
		for j in range(row_col_count):
			# if the letter matches the start of our word, 
			# 	call the recursive method for each of the 8 directions
			if word[0] == grid[i][j]:
				found = (check_matching_word(word, grid, row_col_count, i, j, 0, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 1, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 2, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 3, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 4, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 5, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 6, 0) or
					check_matching_word(word, grid, row_col_count, i, j, 7, 0))
				if found:
					# if the word is found, return the row and col as a tuple
					return (i + 1, j + 1)
	# if no matching word is found, return the tuple as (0,0)
	return (0,0)

# A recursive function that will search in a single direction until it no longer matches the word
#		or the word is found
# Input: string representing the word to search
#				 a 2-D list representing the grid of letters
#				 the number of rows or number of columns (since they are equal for this problem)
#				 the row and col indices to search at
#				 the direction that the word is currently being search in (0-7)
#				 the current number of matching letters found
# Output: returns True if the word is found in the search
#									False if the word is not found starting at that row and column
def check_matching_word(word, grid, row_col_count, row, col, dir, letter_count):
	# base cases:
	#		row or col are out of bounds
	#		the letter on the grid doesn't match the next letter in the word
	#		the entire word has been found
	if (row < 0 or col < 0 or 
			row >= row_col_count or col >= row_col_count or 
			grid[row][col] != word[letter_count]):
		return False
	letter_count += 1	# increment letter count once a new matching letter is found
	if len(word) == letter_count:
		return True

	# call the recursive method again until a base case is hit
	if dir == 0:
		return check_matching_word(word, grid, row_col_count, row - 1, col, dir, letter_count)
	elif dir == 1:
		return check_matching_word(word, grid, row_col_count, row - 1, col + 1, dir, letter_count)
	elif dir == 2:
		return check_matching_word(word, grid, row_col_count, row, col + 1, dir, letter_count)
	elif dir == 3:
		return check_matching_word(word, grid, row_col_count, row + 1, col + 1, dir, letter_count)
	elif dir == 4:
		return check_matching_word(word, grid, row_col_count, row + 1, col, dir, letter_count)
	elif dir == 5:
		return check_matching_word(word, grid, row_col_count, row + 1, col - 1, dir, letter_count)
	elif dir == 6:
		return check_matching_word(word, grid, row_col_count, row, col - 1, dir, letter_count)
	else:
		return check_matching_word(word, grid, row_col_count, row - 1, col - 1, dir, letter_count)
	

def main():
  # read the input file from stdin
	word_grid, word_list = read_input()

  # find each word and print its location
	for word in word_list:
		location = find_word (word_grid, word)
		print(word + ": " + str(location))

if __name__ == "__main__":
  main()
