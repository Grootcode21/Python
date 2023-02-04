my_dictionary = {'Name': 'Zara', 'Age': 12, 'Class': 'Sixth', 'School': 'JetBrains Academy'}
x = {'1': 'Groot', '2': 'Alien', '3': 'Evilbear', '4': 'JetBrains'}
print(my_dictionary)
print(x)

my_dictionary['Age'] = 11  # changing key values
print(my_dictionary)

my_dictionary['Sex'] = 'Female'  # updating dictionary
print(my_dictionary)

del my_dictionary['Name']  # remove entry with the key 'Name'
# del clear()  #remove all entries in dict
print(my_dictionary)

del my_dictionary  # delete entire dictionary
#print(my_dictionary) - gives error because dictionary has been deleted
