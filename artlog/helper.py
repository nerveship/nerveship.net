# Initialize variables
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

categories = ["Type", "Title", "Creator", "Release", "Completion", "Rating"] 

# Collects input for each category and adds it to a list
def collect_user_input(categories):
    answers = []
    for category in categories:
        title = category + ": "
        while True:
            answer = input(title)
            if answer.strip():
                answers.append(answer)
                break
            else:
                print("Input cannot be empty. Please provide a valid response.")
    return answers

# Generates the correctly formatted HTML
def format_html(answers):
    if len(answers) != len(categories):
        raise ValueError("The number of answers provided does not match the expected number of categories.")
    
    html_string = "<tr>\n"
    for answer in answers:
        html_string += "    <td>" + answer + "</td>\n"
    html_string += "</tr>"
    return html_string

# Generates the formatted tweet
def format_tweet(answers):
    article = "An" if answers[0].lower() in ["anime", "album"] else "A"
    release_year = "unknown"
    if len(answers[3]) >= 4 and answers[3][-4:].isdigit():
        release_year = answers[3][-4:]
    
    tweet = (f"-------------\n"
             f"Artlog add! {answers[1]} - {article} {answers[0].lower()} by {answers[2]}, "
             f"released in {release_year}.\nRated: {answers[5]}.\n"
             f"https://www.nerveship.net/artlog/")
    return tweet

# Main flow
answers = collect_user_input(categories)
html_output = format_html(answers)
tweet_output = format_tweet(answers)

print(html_output)
print(tweet_output)
