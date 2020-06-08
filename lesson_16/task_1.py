def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


def my_enumerate1(sequence, start=0):
    for i in range(len(sequence)):
        yield start + i, sequence[i]


def my_enumerate2(sequence, start=0):
    return [(start + i, sequence[i]) for i in range(len(sequence))]    
        
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, season in my_enumerate2(seasons):
    print(i, season)

def my_func():
    print("First block")

    yield 1

    print("Second block")

    yield 2


func = my_func()
next(func)

next(func)

range
