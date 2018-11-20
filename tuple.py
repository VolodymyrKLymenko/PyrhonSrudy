# kort cannot be modified
# use lesser memory

a = (43, 56, 100, 'd')
b = [43, 56, 100, 'd']

print (a.__sizeof__())
print (b.__sizeof__())

#Couse error
#a[0] = '5555'
#Work OK
b[0] = 'agasg'

#Tuple
c = tuple("afsasfasfafasf")
print (c)
d = ("asfaf", "asfaf", 51235)
print (d)
print (d.count (51235))
