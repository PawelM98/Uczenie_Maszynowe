import requests
import json
from urllib import request
import time

def download_images():
    response = requests.get("https://picsum.photos/v2/list")
    if response.status_code != 200:
        raise AttributeError('GET /tasks/ {}'.format(response.status_code))
    data = json.loads(response.text)

    pictures=[]
    for s in data:
        pictures.append(s['download_url']+".jpg")
    return pictures

def saveImages(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))

def main():
    images = download_images()
    for image in images:
        saveImages(image)

start_time = time.time()
main()
duration_synch = time.time() - start_time
print(f"Time taken to download images synchronously:: {duration_synch}")