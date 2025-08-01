def is_pangram(sentence):
    alphabets = [chr(i + ord('a')) for i in range(26)]
    alpha_count =  dict.fromkeys(alphabets, 0)
    for letter in sentence:
        if letter.lower() in alphabets:
            alpha_count[letter.lower()] += 1
        else:
            continue
    if 0 in alpha_count.values():
        return False
    return True
    
