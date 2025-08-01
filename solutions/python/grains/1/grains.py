def square(number):
    if number > 0 and number < 65:
        print(number)
        return 2 ** (number-1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum
