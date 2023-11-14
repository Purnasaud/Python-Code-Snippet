# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

# Outer dictionary to store all student dictionaries (nested dictionaries)
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}

# Get student3's name and mark
print("Student 3 name:", class_six['student3']['name'])
print("Student 3 marks:", class_six['student3']['marks'])

# Iterating outer dictionary
print("\nClass details\n")
for key, value in class_six.items():
    # Iterating through nested dictionary
    # Display each student data
    print(key)
    for nested_key, nested_value in value.items():
        print(nested_key, ':', nested_value)
    print('\n')
