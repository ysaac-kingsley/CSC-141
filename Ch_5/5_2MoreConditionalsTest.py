fruit = ['apple', 'banana', 'orange', 'plantane']
numbers = [1,4,8,12]
num = [1,2,3,4,5]

print('Is fruit[1] == banana. I predict true.')
print( fruit[1] == 'banana')
print('Is fruit[1] == Banana. I predict False.')
print( fruit[1] == 'Banana')

print("Is fruit[2].lower() == orange. I predict True")
print(fruit[2].lower() == 'orange')
print("Is fruit[2].upper() == orange. I predict False")
print(fruit[2].upper() == 'orange')

print('Is numbers[0] == numebrs[2]. I predict false.')
print(numbers[0] == numbers[2])
print('Is numbers[0] == num[0]. I predict True.')
print(numbers[0] == num[0])
print('Is numbers[0] <= numbers[2]. I predict True')
print(numbers[0] <= numbers[2])
print('Is numbers[3] >= num[2]. I predict True')
print(numbers[3] >= num[2])
print('Is numbers[2] < num[2]. I predict false')
print(numbers[2] < num[2])
print('Is numbers[2] > num[2]. I predict False')
print(numbers[0] > num[2])