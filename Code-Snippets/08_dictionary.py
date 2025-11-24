#- Purpose: We check the password strength against three parameter
#- 1. Password length is at least 8.
#- 2. Password contains at least a digit.
#- 3. Password contains at least a capital letter.

password = input("Enter new password: ")
parameters = {}    # dictionary: key-value pair

# Check password length
if len(password) >= 8:
    parameters["length"] = True
else:
    parameters["length"] = False

# Check if password has at least a digit:
digit_present = False
for char in password:
    if char.isdigit():
        digit_present = True
parameters["digit"] = digit_present

# Check if password contains at least a capital letter
uppercase_present = False
for char in password:
    if char.isupper():
        uppercase_present = True
parameters["uppercase"] = uppercase_present

if all(parameters.values()):
    #- all() method checks every boolean value of its argument list and returns True iff all values
    #- are True otherwise returns False
    print("Strong password")
else:
    print("Weak password")