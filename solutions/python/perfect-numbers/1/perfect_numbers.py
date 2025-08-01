def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = sum([i for i in range(1, number) if number % i == 0])
    ans = ''
    if aliquot == number:
        ans = 'perfect'
    elif aliquot < number:
        ans = 'deficient'
    else:
        ans = 'abundant'
    return ans
        
        
