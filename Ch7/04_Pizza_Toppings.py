message = ''
pizza_toppings = []

while message == '' :
    x = input('Enter as many pizza topings as you want\nEnter exit to end.\n')
    if x == 'exit':
        message = 's'
    else:
        print(f"I\'ll add {x} to your pizza.\n")
        pizza_toppings.append(x)