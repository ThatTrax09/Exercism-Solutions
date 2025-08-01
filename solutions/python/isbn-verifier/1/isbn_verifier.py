def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    ct = 10
    sum_digs = 0
    for dig in isbn:
        if dig == 'X':
            if ct == 1:
                sum_digs += ct * 10
            else:
                return False
        elif dig.isnumeric():
            sum_digs += ct * int(dig)
        else:
            return False
        ct -= 1
    return sum_digs % 11 == 0
