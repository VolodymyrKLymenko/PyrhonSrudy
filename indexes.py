
l = [34, 'sd', 56, 34.34, 555]
print (l[4])
print (l[-1]) # lasr el of list
print (l[-2])

i = 0
while i < 5:
    print (l[i], '  ', end='')
    i+=1
print ()

#Erase list
#item[START:STOP:STEP]

print (l[::2])
print (l[1::])
print (l[:-2:])
