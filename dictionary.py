# Four ways to create dictioanry
#first
d = {'test': 1, 'test2': 'test4'}
print (d['test'])
print (d['test2'])
print (d)

#second
d = dict (short='dict', longer='alco')
d['short'] = 234
print (d)
print (d['longer'])
print (d['short'])

d2 = dict ([(23, 34), (56, 87)])
print (d2)

#third
d = dict.fromkeys (['a', 'b', 'c'], 1)
print (d)


#fourth
d = {a : a ** 2 for a in range(7)}
print (d)


#Usage
person = {'name': {'lstName': 'Klymenko',
'firstName': 'Volodymyr'}}

print (person['name']['firstName'])

print (person.values())
person.clear ()

