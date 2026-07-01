# Your first line of Python code
# Sample list containing lists
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

print(f"Original list is {list_of_lists}")

non_empty_list = [val for val in list_of_lists if len(val) > 0]
print(f"Non empty list: {non_empty_list}")

#Adding empty list count
empty_list_count = list_of_lists.count([])
print(f"Number of empty list in list is {empty_list_count}")

#Making a single List of Elements:
New_list = []
for item in non_empty_list:
    for val in item:
        New_list.append(val)

print(f"New list: {New_list}")