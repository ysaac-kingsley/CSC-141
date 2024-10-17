my_foods = ['pizza', 'falafel', 'carrot cake']
friendfoods = my_foods[:]

my_foods.append('cannoli')
friendfoods.append('ice cream')

for food in my_foods:
    print("My favorite foods are:")
    print(my_foods)

for food in friendfoods:    
    print("\nMy friend's favorite foods are:")
    print(friendfoods)