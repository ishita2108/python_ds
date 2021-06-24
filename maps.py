import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day3' in res)))
print('day4 in res: {}'.format(('day4' in res)))

print("------------------------------------------------------")

#map reordering
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}
res1 = collections.ChainMap(dict1, dict2)
print(res1.maps,'\n')
res2 = collections.ChainMap(dict2, dict1)
print(res2.maps,'\n')

print("------------------------------------------------------")

#updating-map
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}
res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
dict2['day4'] = 'Fri'
print(res.maps,'\n')

print("--------------------------------------------------------")

#manipulating-operations
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }
  
# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)
  
# printing chainMap using map
print ("All the ChainMap contents are : ")
print (chain.maps)
  
# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)
  
# printing chainMap using map
print ("Displaying new ChainMap : ")
print (chain1.maps)
  
# displaying value associated with b before reversing
print ("Value associated with b before reversing is : ",end="")
print (chain1['b'])
  
# reversing the ChainMap
chain1.maps = reversed(chain1.maps)
  
# displaying value associated with b after reversing
print ("Value associated with b after reversing is : ",end="")
print (chain1['b'])