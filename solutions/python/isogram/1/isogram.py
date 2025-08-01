def is_isogram(string):
    string = string.lower().replace(' ', '').replace('-', '')
    if string == "":
        return True
    return sorted(set([letter for letter in string])) == sorted([letter for letter in string])