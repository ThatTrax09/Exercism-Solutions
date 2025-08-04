def commands(binary_str):
    flag = True
    if binary_str[0] == '1':
        flag = False
    binary_str = binary_str[1:]
    actions = ['jump', 'close your eyes', 'double blink', 'wink']
    ans = []
    for i, bit in enumerate(binary_str):
        if bit == '1':
            ans.append(actions[i])
    if flag:
        ans = list(reversed(ans))
    return ans
    
