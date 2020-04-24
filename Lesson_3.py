#Task_1

a = 'helloword'
print(a[:3] + a[-1])

a = 'my'
print(a * 2)

a = ' x'
print(a[0])


#Task_2

num = str(input())

if num.isdigit() == True and len(num) == 10:
    print('Congratulation! Your entered quantity number is correct.')
elif num.isdigit() == False or len(num) != 10:
    print('Sorry! Your entered quantity number isn\'t correct. ')


#Task_3

check_name = input().lower()
name = 'yaroslav fufalko'

if check_name == name:
    print(True)
elif check_name != name:
    print(False) 