import json

with open("Account details.json") as file:
    data = json.load(file)

for account in data:
    print(account[])
