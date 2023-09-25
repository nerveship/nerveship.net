categories = ["Title", "Developer", "Publisher", "Genre", "Platform", "Release", "Completion", "Rating"]
answers = []

def get_input(array):
    for i in array:
        title = i + ": "
        answer = input(title)
        answers.append(answer)

def print_html():
    print("<tr>")
    for i in answers:
        print("    <td class=\"fitwidth\">" + i + "</td>")
    print("</tr>")

get_input(categories)

print_html()