def leap_year(year):
    ans = False
    if year % 4 == 0:
        ans = True
        if year % 100 == 0:
            if year % 400 == 0:
                ans = True
            else:
                ans = False
    return ans
        
        
