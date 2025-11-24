# Purpose: This program will add a new member name in member.txt file

#- To update a file(here add names) you have to first open it, read its content and save it into a list
#- then append the new lines(here member) into the list, and then write the whole new list into the file.

# file = open("files/members.txt", 'r')
# members = file.readlines()
# file.close()

with open("files/members.txt", 'r') as file:
    members = file.readlines()  # This will create a member list

new_member = input("Add a new member: ") + "\n"
members.append(new_member)

# file = open("files/members.txt", 'w')
# file.writelines(members)
# file.close()

with open("files/members.txt", 'w') as file:
    file.writelines(members)    # writelines() always need a list as an argument

print("Member added successfully")