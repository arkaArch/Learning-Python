#- The Python zip() function is a built-in utility that takes multiple iterables (like lists, tuples, strings, or even
#- dictionaries) as input and combines their corresponding elements into an iterator of tuples. Each tuple contains
#- elements from the same position across the input iterables.
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))      # [(1, 'a'), (2, 'b'), (3, 'c')]


# Purpose: This program will create three text files with various name which contain different texts.
contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process were well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()
