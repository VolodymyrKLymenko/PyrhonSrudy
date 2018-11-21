f = open ('text.txt') # params of file https://itproger.com/course/python/14

print (f.read (1))

for line in f:
    print (line)

f.write ('Hi it')
f.close ()