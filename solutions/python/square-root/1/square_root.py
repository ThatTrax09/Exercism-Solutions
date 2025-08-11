def square_root(number):
    guess = 1
    while int(guess)**2 != number:
        guess = (guess + number/guess)/2
    return int(guess)
