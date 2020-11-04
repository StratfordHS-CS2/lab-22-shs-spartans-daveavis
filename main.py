num = int(input('Enter a number: '))

for x in range(num + 1):
    if x % 3 == 0 and x % 4 == 0:
        print('SHS Spartans')
    elif x % 3 == 0:
        print('SHS')
    elif x % 4 == 0:
        print('Spartans')
    else:
        print(x)
