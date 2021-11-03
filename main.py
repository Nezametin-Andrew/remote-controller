import os
import time
from threading import Thread
import webbrowser
import requests



PORT = 8888
HOST = "0.0.0.0"

remote_server = {
    "host": "http://0.0.0.0:5000",
}


def install(installer):
    ...

def download(url):
    ...

def open_web(url: str, params: int):
    webbrowser.open(url=url, new=params)


command = {
    "open_web": open_web,
}


def main_loop():
    while True:
        try:
            if r := requests.get(remote_server['host']).json():
                command[r['command']](*r['params'])
            exit()
        except Exception as e:
            print(e)
            time.sleep(5)


if __name__ == "__main__":
    main_loop()