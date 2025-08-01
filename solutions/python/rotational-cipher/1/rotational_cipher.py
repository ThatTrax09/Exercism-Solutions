import string
def rotate(text, key):
    return ' '.join([''.join([chr((ord(letter) - ord('A') +key)%26 + ord('A')) if letter.isupper() else chr((ord(letter) - ord('a') +key)%26 + ord('a')) if letter.islower() else letter for letter in word]) for word in text.split(' ')])
