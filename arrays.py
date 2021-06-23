from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
 print(x)

# #accessing
print(array1[0])

# #insertion
array1.insert(1,60)
for x in array1:
 print(x)

# #deletion
array1.remove(60)
for x in array1:
 print(x)

del array1[1]
for x in array1:
    print(x)

#searching
print(array1.index(40))
print(array1[2])

# #update
array1[2] = 60
for x in array1:
 print(x)