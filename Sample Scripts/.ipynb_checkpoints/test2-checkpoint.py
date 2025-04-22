import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def unused_function():
    print("This function is never used.")

print(distance(0, 0, 3, 4))
