items = [
    {"name": "Data Science", "type": "concept"},
    {"name": "Data Analysis", "type": "concept"},
    {"name": "Python", "type": "language"},
    {"name": "R", "type": "language"},
    {"name": "Tableau", "type": "tool"},
    {"name": "Power BI", "type": "tool"},
]

# Grouping items by type using a for loop
grouped = {}
for item in items:
    item_type = item["type"]  # Corrected this line to access the dictionary element
    if item_type not in grouped:
        grouped[item_type] = []
    grouped[item_type].append(item["name"])

print(grouped)
