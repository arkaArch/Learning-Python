for index, word in enumerate("Hello"):
    print(index, word)

enumerate_variable = enumerate("Hello")
print(enumerate_variable)   # Shows the object and it's address

enumerate_list = list(enumerate("Hello"))
print(enumerate_list)    # [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# The 'enumerate("Hello")' is same as '[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]'
for index, word in [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]:
    print(index, word)



# In Python, variables defined within a for loop or a while loop are not strictly limited to the scope of that loop
# block. They remain accessible and retain their last assigned value after the loop has finished executing, provided
# they were assigned a value within the loop.
# This behavior is due to Python's scope rules, which differ from some other languages like C++ or Java. Python does
# not have block-level scope for 'for' or 'while' loops; instead, variables defined within these loops reside in the
# enclosing scope (e.g., the function scope or global scope).
print(f"Value of index outside the scope of loop: {index + 1}")    # 5

