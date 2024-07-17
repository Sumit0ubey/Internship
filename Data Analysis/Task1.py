"""
TASK 1: Understanding Python Data Types -
    Description: This task involves understanding the basic data types in Python Such as lists, dictionaries, and sets.
"""

# Understanding Lists - 

print(f"{' '*10} -- list -- \n")

Random_data = ['jimmiy', 19, True, 9.54]
print("One dimension list --->", Random_data)

student_marks = [["Roa", 86], ["Rajput", 87], ['Rajmin', 88]]
print('Two dimension list ---->', student_marks)

# Adding data in the list using append and insert
student_marks.append(['Raju', 98])  # it adds the element to the end of the list
student_marks.insert(1, ["Rua", 86])  # it adds the element to the specified place 
print(student_marks)

# sorting, and working on the list
student_marks.sort()  # By defualt sort function sort the data in ascending order
print("In Ascending order: ", student_marks)
student_marks.sort(reverse=True) # This way sort function sorts the data in the descending order
print("In descending order: ", student_marks)
student_marks.reverse()  # This reverse the order of the list
print("In Reverse order: ", student_marks)
print(student_marks.count(['Roa', 86]))  # it counts the number of times the specified data is there in the list
print(student_marks.index(['Raju', 98]))  # it returns the index of the specified value in the list

# deleting and removing the data in the list
student_marks.remove(['Raju', 98])  # it deletes the data that is specified from the list
student_marks.pop() # it deletes the data randomly from the list at any position
print(student_marks)
print("By Doing this we can say that list are 'Mutable', 'Ordered', 'Changeable'.")
print()

# Understanding sets - 
print(f'{" "*10} -- set --')
Random_data_1 = {45, 78, 32, 78, 2.01}
Random_data_2 = Random_data_1.copy()
print('Set ----> ', Random_data_2)

Random_data_2.discard(78) #  This deletes the Specified value that is provided. not raise an error if not exists in set
Random_data_2.remove(45)  #  This deletes the specified value that is provided. but will raise an error if not exists in set
Random_data_2.pop()  # This will delete the random value from the set.
print(Random_data_2)
Random_data_2.clear()  # This delets the all value that are present in the set
print(Random_data_2)

Random_data_2.add('Task1')  # This lets as add value in the set
Random_data_2.update(Random_data)  # This lets as add whole set, list, in the set
Random_data = set(Random_data)  #  This lets as convert list, tuple, dictionary to set
print(Random_data_2)

print("Set also provides various set operations from the set theory like union, difference, intersection etc.")
union_set = Random_data_2.union(Random_data_1)
diffference_set = Random_data_2.difference(Random_data)
intersection_set = Random_data_2.intersection(Random_data)
print("\n Union Set on Random_data_2 and Random_data_1 ----> ", union_set, "\n", "Difference set on Random_data_2 and Random_data ----> ", diffference_set, "\n", "Intersection set on Random_data_2 and Random_data ----->", intersection_set)
print("By Doing this we can say that set are 'Unordered', 'Unchangeable'.")
print()

# Uderstanding Dictionary - 
print(f"{" "*10} -- Dictionary -- ")
student_marks = {"Roa": 97, "Rua": 95, "Raj": 99, "Romi": 98}
print("Dicitonary ----> ", student_marks)
print(student_marks["Roa"]) # By specifing the name of the key in square braket we can get the value.
print(student_marks.get('Rua'))  # This do the same thing as the above
print(student_marks.keys())  # This gives the list of keys in the given dictionary
print(student_marks.values()) # This gives the values in the list of given dictionary 
print(student_marks.items())  # This gives the tuple of keys and their values for the given dictionary

student_marks['Rajek'] = 100  # This way we can add new data or update the information about the existing keys.
student_marks['Rajek'] = 97
print(student_marks)
print("By Doing this we can say that dictionary are 'Ordered', 'changeable', 'Non-duplicate'.")
