i = 0
while i < 25:
    print(i)
    i+=5

for j in 'hello world':
    if j == 'w':
        continue
    if j == 'q':
        break
    print(j*2, end ='')
else:
    print("no break happened")
    print("no 'q' in word")
    


