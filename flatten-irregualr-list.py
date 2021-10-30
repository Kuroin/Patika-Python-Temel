lst =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(lst):
    for sublist in lst:
        if type(sublist) is list:
            yield from flatten(sublist)
        else:
            yield sublist

print(list(flatten(lst)))