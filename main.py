import requests
import json

links = []
out_extension = "jpg"
out_dir = "downloads"

with open('links.json') as json_file:
    file = json.load(json_file)
    links = file['links']

for (index, link) in enumerate(links):
    file_name = str(index+1)+"."+out_extension
    file_path = out_dir+"/"+file_name
    print(f"Downloading {link} to the File - {file_name}")
    response = requests.get(link)
    open(file_path, "wb").write(response.content)
