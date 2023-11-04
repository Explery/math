# x = length of side
def getSquare(x):
    return x**2

# x = width, y = height
def getRectangle(x, y):
    return x*y

# x = base, y = height
def getTriangle(x, y):
    return (x*y)/2

# x = large diagonal, y = small diagonal
def getRhombus(x, y):
    return (x*y)/2

# x = large side, y = small side, z = height
def getTrapezoid(x, y ,z):
    return ((x+y)/2)*z

# x = perimeter, y = apothem
def getRegularPolygon(x, y):
    return (x/2)*y