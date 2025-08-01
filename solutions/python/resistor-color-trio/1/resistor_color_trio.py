COLORS = {'black': 0,
'brown': 1,
'red': 2,
'orange': 3,
'yellow': 4,
'green': 5,
'blue': 6,
'violet': 7,
'grey': 8,
'white': 9}

def label(colors):
    ans = str(COLORS[colors[0]])+str(COLORS[colors[1]])+('0' * COLORS[colors[2]])
    print(ans)
    if ans.startswith('0'):
        ans = ans[1:]
    prefix = ''
    if int(ans) >= 1000000000 and int(ans) % 1000000000 == 0:
        ans = str(int(ans) // 1000000000)
        prefix = 'giga'
    elif int(ans) >= 1000000 and int(ans) % 1000000 == 0:
        ans = str(int(ans) // 1000000)
        prefix = 'mega'
    elif int(ans) >= 1000 and int(ans) % 1000 == 0:
        ans= str(int(ans) // 1000)
        prefix = 'kilo'
    return ans+' '+prefix+'ohms'
