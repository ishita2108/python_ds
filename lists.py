#accessing
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
print( "list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#updating
list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001
print ("New value available at index 2 : ")
print (list[2])

#deleting
list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)

#removing
list1.remove(2000)
print(list1)

#appending
list1 = ['physics', 'chemistry', 1997, 2000]
list1.append(23)
print(list1)

#inserting
list1.insert(2,29)
print(list1)

#repetition
l=['Hi!']
print(l*4)

#length
print(len(l))

#concatenation
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
print(list1+list2)

#membership
print (3 in list2)

#iteration
list2 = [1, 2, 3, 4, 5 ]
for x in list2:
    print(x)

