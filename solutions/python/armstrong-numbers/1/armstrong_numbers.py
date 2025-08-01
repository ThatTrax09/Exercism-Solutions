def is_armstrong_number(number):
    length = len(str(number))
    sum_armstrong = 0
    number1 = number
    if number < 10:
        return True
    for i in range(length):
        sum_armstrong += (number %(10))** length
        number //= 10
    if sum_armstrong == number1:
        return True
    return False
    
