# Suppose we have a list of files like:
file_names = ["reload.txt", "remove.txt", "run.txt", "require.txt"]
# Now we want to print the file name without extension
# Here we can use list comprehension like:
file_names_wo_extension = [file_name.strip('.txt') for file_name in file_names]

# The upper line is the short form of codes written bellow:
'''
file_names_wo_extension = []
for file_name in file_names:
    file_name = file_name.strip('\n')
    file_names_wo_extension.append(file_name)
'''

for file_names_wo_extension in file_names_wo_extension:
    print(file_names_wo_extension.capitalize())

