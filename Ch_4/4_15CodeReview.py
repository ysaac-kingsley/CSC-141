#Program 1
names = ['Chance', 'Fisher', 'John']
message = 'Greetings from Austria '

print(message + names[0] + '!')
print(message + names[1] + '!')
print(message + names[2] + '!')

#Program 2
fname = "   John"
mname = "F.   "
lname = "  Kennedy  "

print(fname + mname+ lname)
print(fname.lstrip() + "\n" + mname.rstrip() + "\n" + lname.strip())

#program 3
buffet = ("pizza", 'sushi', 'burgers', 'fries', 'water')

for food in buffet:
    print(food)

'''
Added this code to add red ruler at 80th character.
    "editor.rulers": [
        {"column": 80, "color": "#ff000000"}
    ]
'''