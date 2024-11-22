def make_shirt(sign='I love Python', size='LARGE'):
    print(f"The shirt size is {size.upper()}.")
    print(f"It will have a puff print in the middle that says \"{sign}\".")

make_shirt()
print('\n')
make_shirt(size='medium')
print('\n')
make_shirt(sign = 'I hate Python!!', size = 'small')