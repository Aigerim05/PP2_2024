'''
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, otherx, othery):
        distance = math.sqrt((self.x - otherx)**2 + (self.y - othery) ** 2)
        return distance
    
# coord1 = Point(2, 3)
# coord2 = Point(4, 5)

# print(coord1.dist(0, 0))
