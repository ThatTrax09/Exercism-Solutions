def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    flat = []
    for list in lists:
        for item in list:
            flat.append(item)
    return flat


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    ct = 0
    for item in list:
        ct += 1
    return ct


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return int(acc)


def foldr(function, list, initial):
    acc = initial
    for item in list[::-1]:
        acc = function(acc, item)
    return acc


def reverse(list):
    for i in range(0, len(list)//2):
        temp = list[i] 
        list[i] = list[len(list) - i - 1]
        list[len(list) - i - 1] = temp
    return list
