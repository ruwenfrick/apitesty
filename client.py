import requests
import json
import os
import sys

def get_file(url):
    response = requests.get(url)
    return response.json()

def write_file(to_write, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w+") as file:
        json.dump(to_write, file)

if __name__ == "__main__":
    ip = sys.argv[1]
    to_write = get_file(f"http://{ip}/files/1")
    write_file(to_write, os.path.join("rec_files", "1.json"))
