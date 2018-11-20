
l = [] #Empty list

lst = [1, 56, 'q', 2.34, ['s', 't', 'r']]

print(lst)
print(lst[2])

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append (23)
l.append (34)
b = [100, 100]
l.extend (b) # add range
l.insert (1, 3525)
l.append (34)
l.remove (34) # delete first
l.pop (0) # remove last l[0] and return
print(l.index (100)) # return first index of some element
print(l.count (100)) # clunt of specific elemet

l.sort ()
l.reverse ()

print (l)

l.clear ()

print (l)
