import os

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 
answers = []
final_string = ''

#gets input for each category and adds it to answers
def get_input(array):
    for i in array:
        title = i + ": "
        answer = input(title)
        answers.append(answer)

#generates the correctly formatted html
def format_html():
    final_string = "<tr>\n"
    for i in answers:
        final_string += "    <td>" + i + "</td>\n"
    final_string += "</tr>"
    print(final_string)

def format_tweet():
    print("-------------")
    if answers[0].lower() == "anime":
        print("Artlog add! " + answers[1] + " - An " + answers[0].lower()  + " made by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nRated: " + answers[5] + ".")
    else:
        print("Artlog add! " + answers[1] + " - A " + answers[0].lower()  + " made by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nRated: " + answers[5] + ".")
    print("https://www.nerveship.net/artlog/")

get_input(categories)
os.system('cls') #clears screen
format_html()
format_tweet()