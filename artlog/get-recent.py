html_file = r"artlog\index.html"

# Mirror of filter groups
filter_groups = {
    'Film':       ['Film', 'Short Film', 'Documentary'],
    'Music':      ['Music', 'Musical'],
    'Animanga':   ['Anime', 'Manga'],
    'Literature': ['Novel', 'Short Story', 'Poem'],
}

with open(html_file, 'r', encoding="utf-8") as file:
    data = file.readlines()

# Types that aren't in any group get their own menu option
grouped = {t for types in filter_groups.values() for t in types}
other_types = []
for i, line in enumerate(data):
    if line.strip().startswith('<tr>') and i+1 < len(data):
        next_line = data[i+1].strip()
        if next_line.startswith('<td>') and next_line.endswith('</td>'):
            t = next_line.replace('<td>', '').replace('</td>', '').strip()
            if t not in grouped and t not in other_types:
                other_types.append(t)

options = ['All'] + list(filter_groups) + sorted(other_types)
for num, name in enumerate(options, 1):
    print(f"{num}. {name}")

choice = options[int(input("Pick a number: ")) - 1]
n = int(input("How many recent entries do you want to grab? "))

if choice == 'All':
    allowed = None
elif choice in filter_groups:
    allowed = set(filter_groups[choice])
else:
    allowed = {choice}

results = []
i = 0
while i < len(data):
    line = data[i].strip()
    if line.startswith('<tr>'):
        next_line = data[i+1].strip() if i+1 < len(data) else ''
        if next_line.startswith('<td>') and next_line.endswith('</td>'):
            entry_type = next_line.replace('<td>', '').replace('</td>', '').strip()
            if allowed is None or entry_type in allowed:
                title = data[i+2].replace('<td>', '').replace('</td>', '').strip()
                creator = data[i+3].replace('<td>', '').replace('</td>', '').replace('<br>', ' & ').replace('</br>', '').strip()
                year = data[i+4].replace('<td>', '').replace('</td>', '').strip().split()[-1]
                rating = data[i+6].replace('<td class="alnright">', '').replace('</td>', '').strip()
                results.append(f"{title} by {creator} - {year}. \nRated {rating}.\n")
    i += 1

if not results:
    print(f"No entries found for '{choice}'.")

for entry in results[:n]:
    print(entry)
print("<https://www.nerveship.net/artlog/>")