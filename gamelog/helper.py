import fileinput

#Init vars
filename = "nerveship.net\gamelog\index.html"
categories = ["Title", "Developer", "Publisher", "Genre", "Platform", "Release", "Completion", "Rating"]
answers = []

#Gets input for each category and adds it to answers
def get_input(array):
    for i in array:
        title = i + ": "
        answer = input(title)
        answers.append(answer)

#Generates the correctly formatted html
def print_html():
    final_string = "<tr>\n"
    for i in answers:
        final_string += "    <td class=\"fitwidth\">" + i + "</td>\n"
    final_string += "</tr>"
    print(final_string)

get_input(categories)
print_html()