def response(hey_bob):
    ans = ""
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?'):
        if hey_bob[:-1].replace("'", "").isupper():
            ans = "Calm down, I know what I'm doing!"
        else:
            ans = "Sure."
    elif hey_bob[:-1].isupper():
        ans = "Whoa, chill out!"
    elif hey_bob == '':
        ans = "Fine. Be that way!"
    else:
        ans = "Whatever."
    return ans
    
