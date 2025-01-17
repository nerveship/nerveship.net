import os

categories = ["Type", "Title", "Creator", "Release", "Completion", "Recommended"]

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

def format_html(answers):
    html_string = "<tr>\n"

    for i, answer in enumerate(answers):
        if i == len(answers) - 1:
            html_string += '    <td class="alnright">' + answer + "</td>\n"
        else:
            html_string += "    <td>" + answer + "</td>\n"

    html_string += "</tr>\n"

    return html_string

def insert_at_line(html_string, file_name="artlog/index.html", line_number=42):
    try:
        if not os.path.exists(file_name):
            print(f"The file '{file_name}' does not exist.")
            return
        
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        while len(lines) < line_number:
            lines.append("\n")
        
        indented_html = "\n".join(["\t" * 9 + line for line in html_string.split("\n") if line.strip() != ""])
        
        lines.insert(line_number - 1, "\n")
        lines.insert(line_number, indented_html + "\n")
        
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(lines)
        
        print(f"HTML entry successfully added at line {line_number} in '{file_name}'")

    except Exception as e:
        print(f"An error occurred while modifying the file: {e}")

answers = collect_user_input(categories)
html_output = format_html(answers)

print("Generated HTML:")
print(html_output)

insert_at_line(html_output, file_name="artlog/index.html", line_number=42)
