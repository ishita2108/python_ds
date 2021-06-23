tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d")

#The empty tuple is written as two parentheses containing nothing −
tup = ()

# To write a tuple containing a single value you have to include a comma, even though there is only one value −
tup1 = (50,)

# accessing
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#updating

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)

#deleting
tup = ('physics', 'chemistry', 1997, 2000);
print (tup)
del (tup)
print ("After deleting tup : ")
# print (tup) will give error

#repetition
l=('Hi!')
print(l*4)

#length
print(len(l))

#concatenation
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(tup1+tup2)

#membership
print (3 in tup2)

#iteration
tup2 = [1, 2, 3, 4, 5 ]
for x in tup2:
    print(x)
