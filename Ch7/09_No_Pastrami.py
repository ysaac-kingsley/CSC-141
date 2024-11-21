sandwhich_orders = ['blt', 'pastrami', 'italian', 'pastrami', 'chicken', 'beef', 'pastrami']
finished_sandwhiches = []

print('The deli has run out of Pastrami!\n')
for t in sandwhich_orders:
    if t == 'pastrami':
        sandwhich_orders.remove(t)

for s in sandwhich_orders:
    print(f"I just made a {s} sandwhich!")
    finished_sandwhiches.append(s)
print('\n')

for n in finished_sandwhiches:
    print(f"{n} sandwhich")
print('\n')