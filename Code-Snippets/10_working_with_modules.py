import glob
import csv
import webbrowser

#- The glob module in Python provides functions for finding path names
#- that match a specified pattern, following the rules used by the Unix shell.
filepaths = glob.glob("files/*.txt")

for filepath in filepaths:
    with open(filepath, 'r') as file:
        print(file.read(), "\n")


#- Working with csv files
with open("files/weather.csv", "r") as file:
    data = list(csv.reader(file))
    #- "csv.reader(file)" returns an iterator object. Since we can't access the iterator
    #- directly, we convert it as a list.

for row in data[1:]:
    # Since first item of the list is [Station, Temperature]
    # We slice it from item 1
    print(f"Temperature of {row[0]} is {row[1]} degree Celsius")


#- Working with browser:
user_term = input("Enter the keyword(s) you want to search: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + user_term)
