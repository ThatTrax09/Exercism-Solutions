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

TOLERANCES = {
    'grey' : '0.05%',
    'violet' : '0.1%',
    'blue' : '0.25%',
    'green' : '0.5%',
    'brown' : '1%',
    'red' : '2%',
    'gold' : '5%',
    'silver' : '10%'
}

def format_zeros(ans, colors):
    if ans.startswith('0'):
        ans = ans[1:]
    prefix = ''
    if int(ans) >= 1000000000:
        ans = str(int(ans) / 1000000000)
        prefix = 'giga'
    elif int(ans) >= 1000000:
        ans = str(int(ans) / 1000000)
        prefix = 'mega'
    elif int(ans) >= 1000:
        ans= str(int(ans) / 1000)
        prefix = 'kilo'
    if ans.endswith('.0'):
        ans = ans[:-2]
    tolerance = TOLERANCES[colors[-1]]
    return ans+' '+prefix+'ohms ±'+tolerance

def resistor_label(colors):
    if len(colors) == 1:
        return str(COLORS[colors[0]])+' ohms'
    elif len(colors) == 4:
        ans = str(COLORS[colors[0]])+str(COLORS[colors[1]])+('0' * COLORS[colors[2]])
    elif len(colors) == 5:
        ans = str(COLORS[colors[0]])+str(COLORS[colors[1]])+str(COLORS[colors[2]]) + ('0' * COLORS[colors[3]])
    return format_zeros(ans, colors)
        