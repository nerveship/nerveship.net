#Init vars
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
    print("<tr>")
    for i in answers:
        print("    <td class=\"fitwidth\">" + i + "</td>")
    print("</tr>")

get_input(categories)
print_html()