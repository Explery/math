def getAvg(x):
    if len(x) == 0:
        return 0
    else:
        total = sum(x)
        average = total/len(x)
        return average

def getExponent(x, y):
    if y == 0:
        return 1    
    else:
        return x**y