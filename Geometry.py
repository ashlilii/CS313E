#  File: Geometry.py

#  Description: Geometric shapes and appropriate functions

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return math.sqrt((self.x - other.x) ** 2.0 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x, y, z)
        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Radius: ' + str(self.radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return 4.0 * math.pi * self.radius ** 2

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return 4 / 3 * math.pi * self.radius ** 3

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        return Point.distance(p, self.center) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        for n in range(3):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = other.center.x
            elif n == 1:
                selfAxis = self.center.y
                otherAxis = other.center.y
            else:
                selfAxis = self.center.z
                otherAxis = other.center.z

            if (selfAxis - self.radius < otherAxis - other.radius < selfAxis + self.radius) is True:
                if (selfAxis - self.radius < otherAxis + other.radius < selfAxis + self.radius) is False:
                    return False
            else:
                return False

        return True

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        #top surface of cube
        cubeX = a_cube.center.x
        cubeY = a_cube.center.y
        cubeZ = a_cube.center.z
        halfSide = a_cube.side / 2

        top1 = self.center.distance(Point((cubeX + halfSide), (cubeY + halfSide), (cubeZ + a_cube.side / 2)))
        top2 = self.center.distance(Point((cubeX - halfSide), (cubeY + halfSide), (cubeZ + a_cube.side / 2)))
        top3 = self.center.distance(Point((cubeX + halfSide), (cubeY - halfSide), (cubeZ + a_cube.side / 2)))
        top4 = self.center.distance(Point((cubeX - halfSide), (cubeY - halfSide), (cubeZ + a_cube.side / 2)))

        bot1 = self.center.distance(Point((cubeX + halfSide), (cubeY + halfSide), (cubeZ - a_cube.side / 2)))
        bot2 = self.center.distance(Point((cubeX - halfSide), (cubeY + halfSide), (cubeZ - a_cube.side / 2)))
        bot3 = self.center.distance(Point((cubeX + halfSide), (cubeY - halfSide), (cubeZ - a_cube.side / 2)))
        bot4 = self.center.distance(Point((cubeX - halfSide), (cubeY - halfSide), (cubeZ - a_cube.side / 2)))

        if top1 > self.radius or top2 > self.radius or top3 > self.radius or top4 > self.radius:
            return False
        if bot1 > self.radius or bot2 > self.radius or bot3 > self.radius or bot4 > self.radius:
            return False

        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        #box method
        #top surface of box
        cylX = a_cyl.center.x
        cylY = a_cyl.center.y
        cylZ = a_cyl.center.z
        halfSide = a_cyl.radius

        top1 = Point((cylX + halfSide), (cylX + halfSide), (cylZ + a_cyl.height / 2))
        top2 = Point((cylX - halfSide), (cylY + halfSide), (cylZ + a_cyl.height / 2))
        top3 = Point((cylX + halfSide), (cylY - halfSide), (cylZ + a_cyl.height / 2))
        top4 = Point((cylX - halfSide), (cylY - halfSide), (cylZ + a_cyl.height / 2))

        bot1 = Point((cylX + halfSide), (cylY + halfSide), (cylZ - a_cyl.height / 2))
        bot2 = Point((cylX - halfSide), (cylY + halfSide), (cylZ - a_cyl.height / 2))
        bot3 = Point((cylX + halfSide), (cylY - halfSide), (cylZ - a_cyl.height / 2))
        bot4 = Point((cylX - halfSide), (cylY - halfSide), (cylZ - a_cyl.height / 2))

        if (self.is_inside_point(top1) == False) or (self.is_inside_point(top2) == False) or (self.is_inside_point(top3) == False) or (self.is_inside_point(top4) == False):
            return False
        if (self.is_inside_point(bot1) == False) or (self.is_inside_point(bot2) == False) or (self.is_inside_point(bot3) == False) or (self.is_inside_point(bot4) == False):
            return False

        return True

        #checking x and y
        for n in range(2):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = a_cyl.center.x
            else:
                selfAxis = self.center.y
                otherAxis = a_cyl.center.y

            if (selfAxis - self.radius < otherAxis - a_cyl.radius < selfAxis + self.radius) is False:
                if (selfAxis - self.radius < otherAxis + a_cyl.radius < selfAxis + self.radius) is False:
                    return False

        #checking z values for box
        if (self.center.z - self.radius < a_cyl.center.z - a_cyl.height / 2 < self.center.z + self.radius) is True:
            if (self.center.z - self.radius < a_cyl.center.z + a_cyl.height / 2 < self.center.z + self.radius) is False:
                return False
        else:
            return False

        return True

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        #when sphere is inside the other return false
        if self.is_inside_sphere(other) == True:
            print(self.is_inside_sphere(other))
            return False

        #checking if distance - radius is less)
        return self.center.distance(other.center) <= self.radius +  other.radius

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        if self.is_inside_cube(a_cube) == True:
            return False

        cubeEdge = math.hypot(math.hypot(a_cube.side / 2, a_cube.side / 2), a_cube.side / 2)

        return self.center.distance(a_cube.center) <= self.radius + cubeEdge

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        sideLength = math.hypot(self.radius / 2, self.radius / 2)

        return Cube(self.center.x, self.center.y, self.center.z, sideLength)

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x, y, z)
        self.side = float(side)

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Side: ' + str(self.side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        edgeValue = self.side / 2

        #checking x value
        if (self.center.x - edgeValue < p.x < self.center.x + edgeValue) is False:
            return False
        #checking y value
        if (self.center.y - edgeValue < p.y < self.center.y + edgeValue) is False:
            return False
        #checking z value
        if (self.center.z - edgeValue < p.z < self.center.z + edgeValue) is False:
            return False

        return True

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        edgeValue = self.side / 2

        edgeValue = self.side / 2

        for n in range(3):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = a_sphere.center.x
            elif n == 1:
                selfAxis = self.center.y
                otherAxis = a_sphere.center.y
            else:
                selfAxis = self.center.z
                otherAxis = a_sphere.center.z

            if (selfAxis - edgeValue < otherAxis - a_sphere.radius < selfAxis + edgeValue) is True:
                if (selfAxis - edgeValue < otherAxis + a_sphere.radius < selfAxis + edgeValue) is False:
                    return False
            else:
                return False

        return True

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        edgeValue = self.side / 2
        otherSideHalf = other.side / 2

        for n in range(3):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = other.center.x
            elif n == 1:
                selfAxis = self.center.y
                otherAxis = other.center.y
            else:
                selfAxis = self.center.z
                otherAxis = other.center.z

            if (selfAxis - edgeValue < otherAxis - otherSideHalf < selfAxis + edgeValue) is True:
                if (selfAxis - edgeValue < otherAxis + otherSideHalf < selfAxis + edgeValue) is False:
                    return False
            else:
                return False

        return True

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        #checking x and y valuies
        for n in range(2):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = a_cyl.center.x
            else:
                selfAxis = self.center.y
                otherAxis = a_cyl.center.y

            if (selfAxis - self.side / 2 < otherAxis - a_cyl.radius < selfAxis + self.side / 2) is True:
                if (selfAxis - self.side / 2 < otherAxis + a_cyl.radius < selfAxis + self.side / 2) is False:
                    return False
            else:
                return False

        #checking z values for box
        if (self.center.z - self.side / 2 < a_cyl.center.z - a_cyl.height < self.center.z + self.side / 2) is True:
            if (self.center.z - self.side / 2 < a_cyl.center.z + a_cyl.height < self.center.z + self.side / 2) is False:
                return False
        else:
            return False

        return True

    def cubeCorners(self):
        #top surface of cube
        cubeX = self.center.x
        cubeY = self.center.y
        cubeZ = self.center.z
        halfSide = self.side / 2
        corners = []

        corners.append(Point((cubeX + halfSide), (cubeY + halfSide), (cubeZ + halfSide)))
        corners.append(Point((cubeX - halfSide), (cubeY + halfSide), (cubeZ + halfSide)))
        corners.append(Point((cubeX + halfSide), (cubeY - halfSide), (cubeZ + halfSide)))
        corners.append(Point((cubeX - halfSide), (cubeY - halfSide), (cubeZ + halfSide)))

        corners.append(Point((cubeX + halfSide), (cubeY + halfSide), (cubeZ - halfSide)))
        corners.append(Point((cubeX - halfSide), (cubeY + halfSide), (cubeZ - halfSide)))
        corners.append(Point((cubeX + halfSide), (cubeY - halfSide), (cubeZ - halfSide)))
        corners.append(Point((cubeX - halfSide), (cubeY - halfSide), (cubeZ - halfSide)))

        return corners

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        #checking if cube is inside the other
        if self.is_inside_cube(other) == True or other.is_inside_cube(self) == True:
            return False
        
        #top surface of cube
        otherCorners = other.cubeCorners()
        selfCorners = self.cubeCorners()

        for corner in otherCorners:
            if self.is_inside_point(corner) == True:
                return True

        for cornerSelf in selfCorners:
            if other.is_inside_point(cornerSelf) == True:
                return True
        return False

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        if self.does_intersect_cube(other) == False:
            return 0

        xLength = float()
        yLength = float()
        zLength = float()

        #finding x length of created cube
        if self.center.x - self.side / 2 < other.center.x - other.side / 2 < self.center.x + self.side / 2 == True:
            xLength = abs((other.center.x - other.side / 2) - (self.center.x + self.side / 2))
        else:
            xLength = abs((other.center.x + other.side / 2) - (self.center.x - self.side / 2))
        
        #finding y length of intersecting cube
        if self.center.y - self.side / 2 < other.center.y - other.side / 2 < self.center.y - self.side / 2 == True:
            yLength = abs((other.center.y - other.side / 2) - (self.center.y + self.side / 2))
        else:
            yLength = abs((other.center.y + other.side / 2) - (self.center.y - self.side / 2))

        #finding z length of intersecting cube
        if self.center.z - self.side / 2 < other.center.z - other.side / 2 < self.center.y - self.side / 2 == True:
            zLength = abs((other.center.z - other.side / 2) - (self.center.z + self.side / 2))
        else:
            zLength = abs((other.center.z + other.side / 2) - (self.center.z - self.side / 2))

        return xLength * yLength * zLength

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x, y, z)
        self.radius = float(radius)
        self.height = float(height)

    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Radius: ' + str(self.radius) + ', Height: ' + str(self.height)

    #gets cylinder corners
    def cylinderCorners(self):
        corners = []
        cylX = self.center.x
        cylY = self.center.y
        cylZ = self.center.z
        halfSide = self.radius

        corners.append(Point((cylX + halfSide), (cylX + halfSide), (cylZ + self.height / 2)))
        corners.append(Point((cylX - halfSide), (cylY + halfSide), (cylZ + self.height / 2)))
        corners.append(Point((cylX + halfSide), (cylY - halfSide), (cylZ + self.height / 2)))
        corners.append(Point((cylX - halfSide), (cylY - halfSide), (cylZ + self.height / 2)))

        corners.append(Point((cylX + halfSide), (cylY + halfSide), (cylZ - self.height / 2)))
        corners.append(Point((cylX - halfSide), (cylY + halfSide), (cylZ - self.height / 2)))
        corners.append(Point((cylX + halfSide), (cylY - halfSide), (cylZ - self.height / 2)))
        corners.append(Point((cylX - halfSide), (cylY - halfSide), (cylZ - self.height / 2)))
        return corners

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        return math.pi * self.height * self.radius ** 2

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        #checking z value
        if (self.center.z - self.height / 2 < p.z < self.center.z + self.height / 2) is False:
            return False

        #finding diagnol distance from point to center of cylinder
        return self.radius > math.hypot((p.x - self.center.x), (p.y - self.center.y))

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        #checking x and y valuies
        for n in range(2):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = a_sphere.center.x
            else:
                selfAxis = self.center.y
                otherAxis = a_sphere.center.y

            if (selfAxis - self.radius < otherAxis - a_sphere.radius < selfAxis + self.radius) is True:
                if (selfAxis - self.radius < otherAxis + a_sphere.radius < selfAxis + self.radius) is False:
                    return False
            else:
                return False

        #checking z values for box
        if (self.center.z - self.height < a_sphere.center.z - a_sphere.radius < self.center.z + self.height) is True:
            if (self.center.z - self.height < a_sphere.center.z + a_sphere.radius < self.center.z + self.height) is False:
                return False
        else:
            return False

        return True

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        #checking x and y valuies
        for n in range(2):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = a_cube.center.x
            else:
                selfAxis = self.center.y
                otherAxis = a_cube.center.y

            if (selfAxis - self.radius < otherAxis - a_cube.side / 2 < selfAxis + self.radius) is True:
                if (selfAxis - self.radius < otherAxis + a_cube.side / 2 < selfAxis + self.radius) is False:
                    return False
            else:
                return False

        #checking z values for box
        if (self.center.z - self.height / 2 < a_cube.center.z - a_cube.side / 2 < self.center.z + self.height / 2) is True:
            if (self.center.z - self.height / 2 < a_cube.center.z + a_cube.side / 2 < self.center.z + self.height / 2) is False:
                return False
        else:
            return False

        return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        #checking x and y valuies
        for n in range(2):
            if n == 0:
                selfAxis = self.center.x
                otherAxis = other.center.x
            else:
                selfAxis = self.center.y
                otherAxis = other.center.y

            if (selfAxis - self.radius < otherAxis - other.radius < selfAxis + self.radius) is True:
                if (selfAxis - self.radius < otherAxis + other.radius < selfAxis + self.radius) is False:
                    return False
            else:
                return False

        #checking z values for box
        if (self.center.z - self.height / 2 < other.center.z - other.height / 2 < self.center.z + self.height / 2) is True:
            if (self.center.z - self.height / 2 < other.center.z + other.height / 2 < self.center.z + self.height / 2) is False:
                return False
        else:
            return False

        return True

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        #not doing box method
        if self.is_inside_cylinder(other) == True:
            return False
        if other.is_inside_cylinder(self) == True:
            return False

        if math.hypot((self.center.x - other.center.x), (self.center.y - other.center.y)) < self.radius + other.radius:
            if (self.center.z + self.height / 2 > other.center.z - other.height / 2) == True:
                return True
            if (self.center.z - self.height / 2 > other.center.z + other.height / 2) == True:
                return True
        else:
            return False

        return False

        #not doing box method
        

def main():
  # read data from standard input

  # read the coordinates of the first Point p
    pList = sys.stdin.readline().split()
  # create a Point object 
    p = Point(pList[0], pList[1], pList[2])
  # read the coordinates of the second Point q
    qList = sys.stdin.readline().split()
  # create a Point object
    q = Point(qList[0], qList[1], qList[2])
  # read the coordinates of the center and radius of sphereA
    sphereAList = sys.stdin.readline().split()
  # create a Sphere object 
    sphereA = Sphere(sphereAList[0], sphereAList[1], sphereAList[2], sphereAList[3])
  # read the coordinates of the center and radius of sphereB
    sphereBList = sys.stdin.readline().split()
  # create a Sphere object
    sphereB = Sphere(sphereBList[0], sphereBList[1], sphereBList[2], sphereBList[3])
  # read the coordinates of the center and side of cubeA
    cubeAList = sys.stdin.readline().split()
  # create a Cube object 
    cubeA = Cube(cubeAList[0], cubeAList[1], cubeAList[2], cubeAList[3])
  # read the coordinates of the center and side of cubeB
    cubeBList = sys.stdin.readline().split()
  # create a Cube object 
    cubeB = Cube(cubeBList[0], cubeBList[1], cubeBList[2], cubeBList[3])
  # read the coordinates of the center, radius and height of cylA
    cylAList = sys.stdin.readline().split()
  # create a Cylinder object 
    cylA = Cylinder(cylAList[0], cylAList[1], cylAList[2], cylAList[3], cylAList[4])
  # read the coordinates of the center, radius and height of cylB
    cylBList = sys.stdin.readline().split()
  # create a Cylinder object
    cylB = Cylinder(cylBList[0], cylBList[1], cylBList[2], cylBList[3], cylBList[4])
    #test - printing variables to make sure correct
    #print(p, q, sphereA, sphereB, cubeA, cubeB, cylA, cylB)
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    origin = Point(0, 0, 0)
    if p.distance(origin) > q.distance(Point(0, 0, 0)):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")
  # print if Point p is inside sphereA
    if sphereA.is_inside_point(p) == True:
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")
  # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) == True:
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")
  # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) == True:
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")
  # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) == True:
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")
  # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB) == True:
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")
  # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) == True:
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")
  # print if Point p is inside cubeA
    if cubeA.is_inside_point(p) == True:
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")
  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) == True:
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")
  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) == True:
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")
  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) == True:
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")
  # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB) == True:
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")
  # print if Point p is inside cylA
    if cylA.is_inside_point(p) == True:
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")
  # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA) == True:
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")
  # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA) == True:
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")
  # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB) == True:
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")
  # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB) == True:
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
    main()
    c1 = Cube(2, 1, -3, 4)
    c2 = Cube(3, 2, -4, 3)
    c3 = Cube(3.5, 8.6, 9.0, 4.6)
    c4 = Cube(2.5, 8.7, 4.6, 9.7)
    s1 = Sphere(5, 0, 0, 5)
    s2 = Sphere(0, 0, 0, 1)
    s3 = Sphere(2, 7, 3, 8)
    s4 = Sphere(2, 1, 3, 4)
    s5 = Sphere(-1.0, -2.0, -3.0, 5.0)
    cyl = Cylinder(-2.0, 1.0, -3.0, 5.0, 4.0 )
    cyl1 = Cylinder(1.0, 5.0 ,3.0, 4.0, 2.0  )
    cyl2 = Cylinder(-1.0, 1.0, -3.0 ,5.0 ,2.0)
    cyl3 = Cylinder(4.0 ,2.0, 3.0, 9.0, 7.0)
    cyl4 = Cylinder(2.4, 6.5, 1.3, 6.4, 3.7)
    cyl5 = Cylinder(3.4, 7.6, 4.6, 8.7, 3.4)
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 7)
    

    #print(c3.intersection_volume(c4))
    #print(c3.does_intersect_cube(c4))
    #print(c3.is_inside_cube(c4))

    #print(cyl.does_intersect_cylinder(cyl1))
    #print(s1.does_intersect_cube(c1))
    #print(cyl2.does_intersect_cylinder(cyl3))
    #print(s3.is_inside_cyl(cyl))
