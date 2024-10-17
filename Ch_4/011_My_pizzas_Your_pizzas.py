pisa = ['pepparoni', 'cheese', 'pineapple']
pisa2 = pisa[:]

pisa.append('meatball')
pisa2.append('onion')

for pisas in pisa:
    print(f"{pisas.title()}, is a pizza flavor I like!")

for pisas in pisa2:
    print(f"{pisas.title()}, is a pizza flavor my friend likes!")