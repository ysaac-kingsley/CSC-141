numPpl = input('How many people are in your dinner party?\n')
numPpl = int(numPpl)

if numPpl > 8:
    print('You will have to wait for a table.')
else:
    print('A table is ready!')