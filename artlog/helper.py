#define the categories of information to collect from the user
categories = ["Type", "Title", "Creator", "Release", "Completion", "Recommended"] 

#collects input for each category and adds it to a list
def collect_user_input(categories):
    """
    Prompts the user to input information for each category.
    Ensures that no input is left empty.
    """
    answers = []
    for category in categories:
        title = category + ": "
        while True:
            answer = input(title)
            if answer.strip():  #ensure the input is not empty or just whitespace
                answers.append(answer)
                break
            else:
                print("Input cannot be empty. Please provide a valid response.")
    return answers

#generates the correctly formatted HTML
def format_html(answers):
    html_string = "<tr>\n"
    for i, answer in enumerate(answers):
        if i == len(answers) - 1:  #check if it's the last iteration
            html_string += '    <td class="alnright">' + answer + "</td>\n"
        else:
            html_string += "    <td>" + answer + "</td>\n"
    html_string += "</tr>"
    return html_string


#generates the formatted tweet
def format_tweet(answers):
    article = "An" if answers[0].lower() in ["anime"] else "A"
    release_year = "unknown"
    #extract the last 4 characters of the release information if they represent a year
    if len(answers[3]) >= 4 and answers[3][-4:].isdigit():
        release_year = answers[3][-4:]
    
    tweet = (f"-------------\n"
             f"{answers[1]} - {article} {answers[0].lower()} by {answers[2]}, "
             f"released in {release_year}.\nDo I recommend it? {answers[5]}.\n"
             f"https://www.nerveship.net/artlog/")
    return tweet

#main flow of the script
answers = collect_user_input(categories)  #collects user input for each category
html_output = format_html(answers)  #formats the input into HTML
tweet_output = format_tweet(answers)  #formats the input into a tweet

#print the outputs
print(html_output)
print(tweet_output)
