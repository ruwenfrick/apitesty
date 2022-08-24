import requests
import json
import os.path as path

def get_file(url):
    response = requests.get(url)
    return response.json()

def write_file(to_write, path):
    with open(path, "w+") as file:
        json.dump(to_write, file)

if __name__ == "__main__":
    to_write = get_file("https://apitesty.azurewebsites.net/files/1")
    write_file(to_write, path.join("rec_files", "1.json"))
