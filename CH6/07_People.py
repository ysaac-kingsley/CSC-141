person_0 = {'fname' : "John", 'lname' : 'Smith', 'age' : '24', 'city' : 'Reading'}
person_1 = {'fname' :  'Ysaac', 'lname': 'Kingsley', 'age' : '19', 'city': 'Reading'}
person_2 ={'fname' : 'Chance', 'lname' : 'Hoard', 'age':'20', 'city':'Reading'}

people = [person_0, person_1, person_2]

for k in people:
    fullname = f"{k['fname']} {k['lname']}"
    age = f"{k['age']}"
    location = f"{k['city']}"
    print('Full Name: ' + fullname + '\nAge: ' + age + '\nCity: ' + location)
    print('\n')