
if 1:
    print("true\n")
    print("again")

if 0:
    print("false")

num = input('Enter your name: ')

if num == 'test':
    print("true: ", num)

if num != 'test':
    print("Not a test")

if int(num) > 0:
    if int(num) < 20:
        print('in [0, 20]')
    else:
        print('larger then 20')
elif int(num) < -10:
    print('lesser then -10')

name = input ()
A = 'YES' if name != "Test" else "No"
print(A)

