import json

def setJsonData(title, content):
    data = {
        "title": title,
        "content": content
    }

    with open('pagecontent.json', 'w') as file:
        json.dump(data, file, indent=4)

def getJsonData():
    with open ('pagecontent.json', 'r') as file:
        return json.load(file)
