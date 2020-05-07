def division():
    '''prompt to divide any ways'''


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


division()
