def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if (start > stop and step > 0) or (start < stop and step < 0):
        return []

##    result = []
##    i = start
##    if step > 0:
##        while i < stop:
##            result.append(i)
##            i += step
##    else:
##        while i > stop:
##            result.append(i)
##            i += step
##
##    return result
    
    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step


a = my_range(15, 2, -2)

for num in my_range(15, 2, -2):
    print(num)
