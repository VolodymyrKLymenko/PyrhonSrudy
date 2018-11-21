x = 100
y = 0

try:
    res = x / y
except ZeroDivisionError:
    res = 0

print (res)

try:
    inp = int (input ()) 
except ValueError:
    print ('Not a number')
    inp = 100
else:
    print ("All right")
    inp = 90
finally:
    print (inp)