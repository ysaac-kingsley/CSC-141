respones ={}
polling = True

while polling:
    name = input('\nWhat is your name?\n')
    response = input('If you could visit one place in the world where would it be!\n')

    respones[name] = response
    repeat = input('Would you like another person to respond? yes/no\n')

    if repeat == 'no':
        polling = False

for n, r in respones.items():
    print(f"{n} would like to visit {r}.")