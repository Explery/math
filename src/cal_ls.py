def getAvg(x):
    if len(x) == 0:
        return 0
    else:
        return sum(x)/len(x)

def getExponent(x, y):
    if y == 0:
        return 1    
    else:
        return x**y
