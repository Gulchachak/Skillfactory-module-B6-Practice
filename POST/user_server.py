import os
import json

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request


RESOURCES_PATH = "albums/"

def save_artist(albums_list):
    artist = albums_list["artist"]
    album = albums_list["album"]
    filename = "{}-{}.json".format(artist, album)
    if not os.path.exists(RESOURCES_PATH):
        os.makedirs(RESOURCES_PATH)

    with open(filename, "w") as fd:
        json.dump(albums_list, fd)
    return filename


@route("/albums", method="POST")
def albums():
    albums_list = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    resource_path = save_artist(albums_list)
    print("User saved at: ", resource_path)

    return "Данные успешно сохранены"


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)