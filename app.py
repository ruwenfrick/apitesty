from flask import Flask
import re
import os.path as path
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_there(name):
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name
    return content

@app.route("/files/<code>")
def getFile(code):
    match_object = re.match("^[0-9]*$", code)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "default"

    file_path = path.join("files", f"{clean_name}.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
if __name__ == "__main__":
    app.run()
