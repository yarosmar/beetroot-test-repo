def ooops():
    '''IndexError_exception'''


a = ['o', 'o', 'o', 'p', 's']
s = 0

for i in a:  # ітерація по списку a
    s = s + 1

print(a)
print('Sum =', s)

n = input('Enter index: ')
n = int(n)


try:
    print(a[n])
except IndexError:
    print('o-o-o-p-s')
    print('Try again.')



def division():
    '''atempts to divide any ways'''


while True:
    print('\nGive me two numbers, and I\'ll divide them.')
    a = input('First number: ')
    if a == '':
        break
    b = input('Second number: ')

    try:
        answer = int(a) / int(b)
    except ValueError:
        print('You should to enter digits, not letter or symbol!')
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(f'Your answer is: {answer}')
