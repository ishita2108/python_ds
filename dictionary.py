#accessing
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#updating
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#deleting
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
# dict.clear();     # remove all entries in dict
# del dict ;        # delete entire dictionary

# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

#key's property-1
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])

#key's immutable property 
dict = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name'])