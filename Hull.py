#  File: Hull.py

#  Description: Creates a convex hull using Graham's Scan

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return ((q.x - p.x) * (r.y - p.y)) - ((q.y - p.y) * (r.x - p.x))
  #right = negative / left = positive / 0 = collinear

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  #Create an empty list upperHull that will store the vertices in the upper hull.
  upperHull = list()

  # Append the first two points p_1 and p_2 in order into the upperHull.
  upperHull.append(sorted_points[0])
  upperHull.append(sorted_points[1])
  #For i going from 3 to n 
    #Append p_i to upperHull.
    #While upperHull contains three or more points and the last three
    #points in upperHull do not make a right turn do (refer to the
    #notes below on determinants for right and left interpretations)
    #Delete the middle of the last three points from upperHull
  for i in range(2, len(sorted_points)):
    upperHull.append(sorted_points[i])
    while len(upperHull) >= 3 and det(upperHull[len(upperHull) - 3], upperHull[len(upperHull) - 2], upperHull[len(upperHull) - 1]) > 0:
      upperHull.remove(upperHull[len(upperHull) - 2])

  # Create an empty list lowerHull that will store the vertices
      #in the lower hull.
  lowerHull = list()
  # Append the last two points p_n and p_n-1 in order into lowerHull with p_n as the first point.
  lowerHull.append(sorted_points[len(sorted_points) - 1])
  lowerHull.append(sorted_points[len(sorted_points) - 2])

  #For i going from n - 2 downto 1
    #Append p_i to lowerHull
    #While lowerHull contains three or more points and the last three
    #points in the lowerHull do not make a right turn do
    #Delete the middle of the last three points from lowerHull
  for i in range(len(sorted_points) - 3, -1, -1):
    #print(sorted_points[i])
    lowerHull.append(sorted_points[i])
    while len(lowerHull) >= 3 and det(lowerHull[len(lowerHull) - 3], lowerHull[len(lowerHull) - 2], lowerHull[len(lowerHull) - 1]) > 0:
      lowerHull.remove(lowerHull[len(lowerHull) - 2])

  #Remove the first and last points for lowerHull to avoid duplication
      #with points in the upper hull.
  lowerHull.pop(0)
  lowerHull.pop(len(lowerHull) - 1)

  #Append the points in the lowerHull to the points in the upperHull 
      #and call those points the convexHull
  for point in lowerHull:
    upperHull.append(point)

  #Return the convexHull.
  return upperHull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  det = 0.0
  
  for i in range(len(convex_poly)):
    if i == len(convex_poly) - 1:
      det += convex_poly[i].x * convex_poly[0].y
      det -= convex_poly[i].y * convex_poly[0].x
    else: 
      det += convex_poly[i].x * convex_poly[i + 1].y
      det -= convex_poly[i].y * convex_poly[i + 1].x

  return 0.5 * abs(det)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases
    a = Point(0, 0)
    b = Point(0, 5)
    c = Point(5, 5)
    d = Point(5, 0)
    e = Point(1, 3)
    f = Point(6, 0)
    assert det(a, d, f) == 0
    return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int(line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append(Point (x, y))

  # sort the list according to x-coordinates
  points_list = sorted(points_list)

  # print the sorted list of Point objects

  # get the convex hull
  convexHull = convex_hull(points_list)
  # run your test cases
  test_cases()
  # print your results to standard output

  # print the convex hull
  print('Convex Hull')
  for vertex in convexHull:
      print(vertex)

  # get the area of the convex hull
  convexArea = area_poly(convexHull)

  # print the area of the convex hull
  print()
  print('Area of Convex Hull = ' + str(convexArea))

if __name__ == "__main__":
  main()
