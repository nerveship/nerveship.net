html_file = r"artlog\index.html"

with open(html_file, 'r', encoding="utf-8") as file:
    data = file.readlines()

n = int(input("How many recent entries do you want to grab? "))

results = []
i = 0
while i < len(data):
    line = data[i].strip()
    if line.startswith('<tr>'):
        # check if the next line is a plain <td>something</td> (the type column)
        next_line = data[i+1].strip() if i+1 < len(data) else ''
        if next_line.startswith('<td>') and next_line.endswith('</td>'):
            entry_type = next_line.replace('<td>', '').replace('</td>', '').strip()
            title = data[i+2].replace('<td>', '').replace('</td>', '').strip()
            creator = data[i+3].replace('<td>', '').replace('</td>', '').replace('<br>', ' & ').replace('</br>', '').strip()
            year = data[i+4].replace('<td>', '').replace('</td>', '').strip().split()[-1]
            #rating = data[i+6].replace('<td class="alnright">', '').replace('</td>', '').strip()
            results.append(f"{title} by {creator}, ({year}).")
    i += 1

for entry in results[:n]:
    print(entry)