class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    #Add an __eq__ method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    #Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words
    def __repr__(self):
        return "Coordinate(%d,%d)" % (self.x, self.y)
    
c1 = Coordinate(1, -8)
c2 = Coordinate(1, -8)


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Define an intersect method that returns a new intSet containing elements that appear in both sets. """
        newIntSet = intSet()
        for item in self.vals:
            if item in other.vals:
                newIntSet.insert(item)
        return newIntSet
    
    def __len__(self):
        return len(self.vals)

s1 = intSet()
s1.insert(2)
s1.insert(3)

s2 = intSet()
s2.insert(4)
s2.insert(5)
s2.insert(2)

print(len(s1))

print(s1.intersect(s2))