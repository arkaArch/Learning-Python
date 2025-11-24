# Purpose: This program will read three files from file directory and print the content of each file in console

filenames = ["doc.txt", "presentation.txt", "report.txt"]
for filename in filenames:
    # file = open(f"files/{filename}", "r")
    # content = file.read()
    # file.close()

    #- Sometimes different parts of the codes can interact with each other in a way that, they will change the
    #- content of your file if you have not closed it. So it's good that, once you are done with the file, just
    #- close it.

    #- Now the problem with the upper method, is that you have to exclusively close the file.
    #- And if the program stops before it reaches to 'file.close()' file close will not be executed.
    #- And we will end up with an open file which could cause problems.

    #- So to avoid this we use 'with' statement which address this problem and even if the program stops for
    #- some problems, the file will be closed by this method. So 'with' statement is always recommended over
    #- exclusively close file with file.close()

    with open(f"files/{filename}", "r") as file:
    # - By default open() contains "r"(read argument) so you can write it as
    # with open(f"files/{filename}") as file:
        content = file.read()
    print(content)