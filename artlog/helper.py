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

def format_html(answers):
    base_indent = " " * 3  
    base_offset = " " * 15  

    tr_indent = base_offset  
    td_indent = base_offset + base_indent  

    final_string = f"{tr_indent}<tr>\n"
    total_answers = len(answers)

    for index, i in enumerate(answers):
        if index == total_answers - 1:
            final_string += f"{td_indent}<td class=\"alnright\">{i}</td>\n"
        else:
            final_string += f"{td_indent}<td>{i}</td>\n"

    final_string += f"{tr_indent}</tr>"
    return final_string



def format_tweet():
    print("-------------")

    article = "" 
    if answers[0].lower() in ['anime', 'album']:
        article = "An"
    elif answers[0].lower() in ['music']:
        article = ""
    else:
        article = "A"

    print(answers[1] + " - " + article + " " + answers[0].lower()  + " by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nRating: " + answers[5])
    print("https://www.nerveship.net/artlog/")

def write_to_html():
    html_file = "artlog\\index.html"  

    with open(html_file, 'r', encoding="utf8") as file:
        data = file.readlines()
    
    html_string = f"{format_html(answers)}\n"

    data.insert(49, html_string)

    with open(html_file, 'w', encoding="utf8") as file:
        file.writelines(data)
    
    print("html string written to " + str(html_file))


get_input(categories)
format_html(answers)
format_tweet()  
write_to_html()