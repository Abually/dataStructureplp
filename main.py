my_List=[]
my_List.append(10)
my_List.append(20)
my_List.append(30)
my_List.append(40)
print(my_List)

# Insert 15 at index 1
my_List.insert(1, 15)
print(my_List)

# Extend the list with multiple elements
my_List.extend([50, 60, 70])
print(my_List)

# Remove the last element
my_List.pop(-1)
print(my_List)

# Sort the list
my_List.sort()
print(my_List)

# Find the index of the element 30
print(my_List.index(30))
