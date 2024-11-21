#Use a codditional test in the while statement to stop the loop.
x = 1
while True:
    if x == 1:
        print('Test')
    elif x == 3:
        break
    x += 1

#Use an active variable to control how long the loop runs.

y = ''
while y == '':
    if y == '':     
        print('Test')
        y = 's'

#Use a break statement to exit a loop when a user enters a quit value

while True:
    z = input('Enter exit to break loop.\n')
    if z.lower() == 'exit':
        break
    else:
        print('ha!')