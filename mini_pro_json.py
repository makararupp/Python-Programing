import json

contacts ={'Alex':'123-456','Sara':'789-012'}

# Save to json
with open("contacts.json", 'w') as file:
    json.dump(contacts,file);

# Load from JSON file
with open("contacts.json", "r") as file:
    loaded = json.load(file)
    print(loaded)