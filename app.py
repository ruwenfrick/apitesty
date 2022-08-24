from flask import Flask
from datetime import datetime
import re
import os.path as path

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/files/<code>")
def getFile(code):
    match_object = re.match("^[0-9]*$", code)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "default.txt"
    file = path.join("files", f"{clean_name}.json")
    return Flask.send_file(file)
    
if __name__ == "__main__":
    app.run()