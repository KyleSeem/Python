#Part 1: Create a program that outputs items in list below as regular names

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for data in students:
    print data['first_name'], data['last_name']

#Part 2: Create a program that prints the dictionary below in the following format:
# 1 - MICHAEL JORDAN - 13 (end # is character count in name)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
    x = 1 #acts as a placeholder for index
    print key #students or instructors
    for value in data:
        print x, '-', value['first_name'].upper(), value['last_name'].upper(), '-', len(value['first_name'])+len(value['last_name'])
        x = x+1 #increase count for next index
