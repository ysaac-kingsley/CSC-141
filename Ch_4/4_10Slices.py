pisa = ['pepparoni', 'cheese', 'pineapple', 'orange']

for pisas in pisa:
    print(pisas)

print('The first three items are: \n')
for pisas in pisa[:3]:
    print(pisas)

print('The middle two are: \n')
for pisas in pisa[2:]:
    print(pisas)

print("The last three items are: \n")
for pisas in pisa[-3:]:
    print(pisas)