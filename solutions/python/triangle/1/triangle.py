def valid_triangle(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
        return False
    return True
    
def equilateral(sides):
    if valid_triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
        return False
    return False

def isosceles(sides):
    if valid_triangle(sides):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        return False
    return False

def scalene(sides):
    if valid_triangle(sides):
        if sides[0] != sides[1] != sides[2] != sides[0]:
            return True
        return False
    return False
