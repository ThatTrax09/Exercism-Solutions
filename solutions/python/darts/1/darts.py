def score(x, y):
    radius_square = x**2 + y**2
    ans = 0
    if radius_square <= 1:
        ans = 10
    elif radius_square <= 25:
        ans = 5
    elif radius_square <= 100:
        ans = 1
    return ans
    
