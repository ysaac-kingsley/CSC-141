q1 = input('Which of these rental cars would you like?\nSubaru\nToyota\nLexus\n')

if q1.title() == 'Subaru':
    print('Let me see if I can find you a Subaru!')
elif q1.title() == 'Toyota':
    print('Let me see if I can find you a Toyota!')
elif q1.title() == 'Lexus':
    print('Let me see if I can find you a Lexus!')
else:
    print('That is not one of our options.')