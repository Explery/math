# For same base
# x = base, y = first exponnent, z = second exponnent
def getProductExp(x, y, z):
    return x**(y+z)

# For same exponent, difference base
# x = first base, y = second base, z = exponent
def getProductBase(x, y, z):
    return (x+y)**z

# For same base
# x = base, y = first exponnent, z = second exponnent
def getQuotientExp(x, y, z):
    return x**(y-z)

# For same exponent, difference base
# x = first base, y = second base, z = exponent
def getQuotientBase(x, y, z):
    return (x/y)**z

# Example for this
# image = (x)**(y)**(z)
def getPowerofPower(x, y, z):
    return x**(y*z)

# Every number that exponent by zero will equal 1
def getZeroExponent(x):
    return x**0

def getNegativeExponent(x, y):
    return (1/x)**y
