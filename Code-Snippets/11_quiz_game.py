import json

with open("files/questions.json", "r") as file:
    content = file.read()

#- Now content here gives us a string
# print(type(content))

data = json.loads(content)
#- This gives us a list since entire json file looks like [{...}, {...}, {...}].
#- If we arrange the json file into inside a dictionary it returns a dictionary
# print(type(data))

score = 0
for question_set in data:
    #- Print the question
    print(question_set["question"])
    #- print the alternatives
    for index, alternative in enumerate(question_set["alternatives"]):
        print(f"{index + 1}. {alternative}")
    #- Ask the user to give an answer
    user_answer = int(input("Answer: "))
    #- We can inject this value as a new key in the list of dictionary in questions.json as:
    #- `question_set["user_answer"] = user_answer` and use it later
    if user_answer == question_set["correct_answer"]:
        print("The answer is correct.")
        score += 1
    else:
        correct_option = question_set["correct_answer"]
        answers = question_set["alternatives"]
        correct_answer = answers[correct_option - 1]
        print(f"\033[31mCorrect answer is "
              f"{correct_option}-{correct_answer}.\033[0m")
    print()

print(score, "/", len(data))