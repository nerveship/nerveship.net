import os
from datetime import date, timedelta, datetime

#init vars
categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 
answers = []

#gets input for each category and adds it to answers
def get_input(array):
    today = date.today()
    yesterday = today - timedelta(days=1)

    for i in array:
        title = i + ": "
        answer = input(title)

        # Lazy shit that just lets me automatically format the date if it 
        # was today or yesterday, rather than typing it out 
        if i == "Completion":
            if answer.strip().lower() == "tday":
                answer = today.strftime("%b %#d, %Y")
            elif answer.strip().lower() == "yday":
                answer = yesterday.strftime("%b %#d, %Y")
            else:
                try:
                    parsed = datetime.strptime(answer.strip(), "%d/%m/%Y")
                    answer = parsed.strftime("%b %#d, %Y")
                except ValueError:
                    print("Couldn't parse date, keeping as-is:", answer)
        
        # Takes the 04/02/75 formatted date and puts it into words
        if i == "Release":
            try:
                parsed = datetime.strptime(answer.strip(), "%d/%m/%Y")
                # This stops it putting in 2060. It hasn't fucking happened yet.
                if parsed.year > date.today().year:
                    parsed = parsed.replace(year=parsed.year-100)

                answer = parsed.strftime("%b %#d, %Y")
            except ValueError:
                print("Couldn't parse date, keeping as-is:", answer)
        
        # Automatically formats the star rating
        if i == "Rating":
            complete = answer.strip() + "/5"

            answer = complete

        answers.append(answer)

def format_html(answers):
    # This is for the funny indent stuff, it kind of looks like shit but. 
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
    # Makes it more natural sounding depending on the type
    article = "" 

    art_type = ""

    if answers[0].lower() in ['anime', 'music']:
        article = "An"
    else:
        article = "A"
    
    # Asks what type of music it is before continuing
    if answers[0].lower() in ['music']:
        print("What type of musical release?")
        art_type = input()
    else:
        art_type = answers[0]
    
    # Prints the tweet out
    print("-------------")
    print(answers[1] + " - " + article + " " + art_type + " by " + answers[2] + ", released in " + answers[3][-4:] + "." + "\nRating: " + answers[5])
    print("https://www.nerveship.net/artlog/")

    print("-------------")

def write_to_html():
    html_file = "artlog\index.html" 

    with open(html_file, 'r', encoding="utf8") as file:
        data = file.readlines()
    
    html_string = f"{format_html(answers)}\n"

    entry_point = None
    for i, line in enumerate(data):
        if '<!--Insert table record under here -->' in line:
            entry_point = i + 1
            break

    data.insert(entry_point, html_string)

    with open(html_file, 'w', encoding="utf8") as file:
        file.writelines(data)
    
    print("html string written to " + str(html_file))

get_input(categories)
format_html(answers)
format_tweet()  
write_to_html()