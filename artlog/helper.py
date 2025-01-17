import os

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Recommendation"] 
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
    article = "An" if answers[0].lower() in ['anime', 'album'] else "A"
    print("Artlog add! " + answers[1] + " - " + article + " " + answers[0].lower()  + " made by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nDo I Recommend it? " + answers[5] + ".")
    print("https://www.nerveship.net/artlog/")

get_input(categories)
format_html()
format_tweet()  