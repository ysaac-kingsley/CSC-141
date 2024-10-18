p1 = {'species':'cat', 'owner':'John'}
p2 = {'species':'dog', 'owner':'Ysaac'}
p3 = {'species':'fish', 'owner':'Chance'}
pets = [p1,p2,p3]

for p in pets:
    species = f"{p['species']}"
    owner = f"{p['owner']}"
    print("Kind of animal: " + species.title() + '\nOwner: ' + owner)
    print('\n')