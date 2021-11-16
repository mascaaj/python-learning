# Examples of python builtin hash table - dictionary

d = {'name': 'Kevin', 'age': 34, 'gender': 'male'}

print(d['age'])
print(d['name'])

print(d.items())

print(d.keys())

for key, value in d.items():
    print(value)

d.clear()

print(d.keys())
