x = input('What is your age?\n')
x = int(x)

if x <= 3:
    print('Your ticket is free!')
elif x > 3 and x <= 12:
    print('Your ticket is $10!')
elif x >12:
    print('Your ticket is $15!')
