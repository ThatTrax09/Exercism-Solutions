def find(search_list, value):
    search_list = list(sorted(search_list))
    lower = 0
    upper = len(search_list) - 1
    ans = -1
    while(lower <= upper):
        middle = (lower + upper)//2
        if search_list[middle] == value:
            ans = middle
            break
        elif search_list[middle] > value:
            upper = middle - 1
        else:
            lower = middle + 1
    if ans == -1:
        raise ValueError("value not in array")
    return ans
