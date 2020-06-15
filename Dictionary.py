student={'name':'John','age': 25, 'course':['Maths','Physics']}

print(student['name'])

print(student['course'])

#print(student['phone'])  # gives an error as phone does not exist in the dict

print(student.get('age'))

print(student.get('phone'))  # o/p: None

print(student.get('phone','Not Available')) # default value for None

student['phone']='+91-8622345621'

print(student.get('phone','Not Available')) # o/p: +91-8622345621 as phone is updated

student['name']='Jammie' # will update the value at name

print(student)

# for updating multiple values

student.update({'name':'Happy','age':24,'phone':'+91-7623421223'})

print(student)

# for delection of any value

del student['age']

print(student)


# we can also use pop() for the deletion

name=student.pop('name')

print(name)
print(student)


print(len(student)) # number of keys in dict

print(student.values()) # gives only values

print(student.items())  # gives keys with values


# printing keys with loop
for key in student:
    print(key)

    
for key,value in student.items():
    print(key,value)





