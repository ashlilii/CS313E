#  File: OfficeSpace.py

#  Description: Inputs an office space and outputs the available and conflicting space for each person

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    return abs((rect[0] - rect[2]) * (rect[1] - rect[3]))

#returns boolean if one of the rectangles is inside the other
def doesIntersect(rect1, rect2):
    return rect1[2] > rect2[0] and rect1[0] < rect2[2] and rect1[3] > rect2[1] and rect1[1] < rect2[3]

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    #checking if the rectangles are intersecting
    if doesIntersect(rect1, rect2) == False:
        return (0, 0, 0, 0)

    #getting intersecting rectangle
    xValues = [rect1[0], rect1[2], rect2[0], rect2[2]]
    yValues = [rect1[1], rect1[3], rect2[1], rect2[3]]

    xValues.sort()
    yValues.sort()

    xValues.pop(3)
    yValues.pop(3)
    xValues.pop(0)
    yValues.pop(0)

    return (xValues[0], yValues[0], xValues[1], yValues[1])
        
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    x = len(bldg[0])
    y = len(bldg)
    count = 0

    for i in range(y):
        for n in range(x):
            if bldg[i][n] == 0:
                count += 1
    
    return count

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    x = len(bldg[0])
    y = len(bldg)
    count = 0
    
    for i in range(y):
        for n in range(x):
            if bldg[i][n] != 0 and bldg[i][n] != 1:
                count += 1
    
    return count

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    y = len(bldg)
    count = 0

    for i in range(rect[1], rect[3]):
        for n in range(rect[0], rect[2]):
            if bldg[y - i - 1][n] == 1:
                count += 1
    
    return count


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    #creating the office
    officeGrid = []
    rows = office[3]
    columns = office[2]
    for y in range(rows):
        officeGrid.append([])
        for x in range(columns):
            officeGrid[y].append(0)

    #implementing the cubicles
    for person in cubicles:
        for row in range(person[1], person[3]):
            for column in range(person[0], person[2]):
                officeGrid[rows - row - 1][column] += 1

    return officeGrid

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert area ((0, 0, 1, 1)) == 1
    # write your own test cases
    assert unallocated_space([0, 0, 0], [0, 0, 0], [0, 0, 0]) == 9
    return "all test cases passed"

def main():
  # read the data
    grid = sys.stdin.readline().split()
    temp1 = sys.stdin.readline().split()
    rooms = int(temp1[0])
    office = (0, 0, int(grid[0]), int(grid[1]))
    cubicles = []
    names = []

    #reading different cubicle spaces
    for cubicle in range(rooms):
        temp = sys.stdin.readline().split()
        person = []
        names.append(temp[0])
        person.append(int(temp[1]))
        person.append(int(temp[2]))
        person.append(int(temp[3]))
        person.append(int(temp[4]))
        cubicles.append(person)

  # run your test cases
    officeGrid = request_space(office, cubicles)
  # print the following results after computation

  # compute the total office space
    print("Total", area(office))
  # compute the total unallocated space
    print("Unallocated", unallocated_space(officeGrid))
  # compute the total contested space
    print("Contested", contested_space(officeGrid))
  # compute the uncontested space that each employee gets
    for n, employee in enumerate(names):
        temp = tuple(i for i in cubicles[n])
        print(employee, uncontested_space(officeGrid, temp))

if __name__ == "__main__":
  main()
