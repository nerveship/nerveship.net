import os

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 
answers = []

#gets input for each category and adds it to answers
def get_input(array):
    for i in array:
        title = i + ": "
        answer = input(title)
        answers.append(answer)

#generates the correctly formatted html
def format_html():
    final_string = "\t\t\t\t\t\t\t\t\t<tr>\n"
    total_answers = len(answers)
    
    for index, i in enumerate(answers):
        if index == total_answers - 1: #check if it's the last item
            final_string += f"\t\t\t\t\t\t\t\t\t\t    <td class=\"alnright\">{i}</td>\n" #the \t's add tab indents, idk it looks stupid as fuck but it works
        else:
            final_string += f"\t\t\t\t\t\t\t\t\t\t    <td>{i}</td>\n"
    
    final_string += "\t\t\t\t\t\t\t\t\t</tr>"
    return final_string


def format_tweet():
    print("-------------")
    article = "An" if answers[0].lower() in ['anime', 'album'] else "A"
    print(answers[1] + " - " + article + " " + answers[0].lower()  + " by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nRating: " + answers[5])
    print("https://www.nerveship.net/artlog/")

def write_to_html():
    html_file = "artlog\index.html"  

    
    with open(html_file, 'r', encoding="utf8") as file:
        data = file.readlines()
    
    
    html_string = f"{format_html()}\n"

   
    data.insert(43, html_string)

   
    with open(html_file, 'w', encoding="utf8") as file:
        file.writelines(data)
    
    print("html string written to " + str(html_file))

get_input(categories)
format_html()
format_tweet()  
write_to_html()