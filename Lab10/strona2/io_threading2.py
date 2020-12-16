import os
from urllib import request
from imgurpython import ImgurClient
import timeit

import threading
from concurrent.futures import ThreadPoolExecutor

client_secret = "fe7a46c778b3cc772ddef33ff0d6c723875ef6e6"
client_id = "badb0c22f780b1d"

client = ImgurClient(client_id, client_secret)


def download_image(link):
    filename = link.split('/')[3].split('.')[0]
    fileformat = link.split('/')[3].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))
    print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


def main():
    images = client.get_album_images('dWWGK8v')
    for image in images:
        download_image(image.link)


if __name__ == "__main__":
    print("Time taken to download images synchronously: {}".format(timeit.Timer(main).timeit(number=1)))
