# List are mutable that is you can change a list item:
filenames = ["1.Beautiful_Day.txt", "2.Immature_Bird.txt", "3.Sunday_Afternoon.txt"]
filenames[1] = "2.Immature_Sky.txt"
print(filenames)

# Now if I want to replace '.' with ')' in the 'filenames' list:
i = 0
for filename in filenames:
    filenames[i] = filename.replace('.', ')', 1)
    # Here we use replace() method since strings are immutable
    # So we can't do filename[1] = '-'
    i += 1

print(filenames)

# We can use negative indexing in list like:
for j in range(-3, 0):
    print(filenames[j])

# We can also slice the list, let's slice the list with second and third item:
sliced_filenames = filenames[1:3]
print(sliced_filenames)

# We can also sort a list like
names = ["Arka", "Chaitali", "Arabinda", "Rumu"]
names.sort()
print(names)

# To see all the available methods in string go to python console and type 'dir(list)'
# It'll return all the available methods in list
# To know about a specific method type 'help(list.method_name)' like 'help(list.sort)'


# Tuples are immutable list
colors_tuple = ("red", "blue", "green")
# colors_tuple[2] = "black"     gives a TypeError: 'tuple' object does not support item assignment


# You have to use as many variables as there are items in the internal tuples or lists.
# In the example below, we iterate using three variables:
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)

# Note that the enumerate function always produces a sequence of tuples each containing two items.
# Therefore, when using enumerate, you have to use two variables, not less, not more.