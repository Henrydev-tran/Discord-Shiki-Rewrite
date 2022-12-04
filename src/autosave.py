from app.Game import _vbase__game, _vlabyrinth__game, _vspiral__game, _vempty_labyrinth__game, _vempty_spiral__game
from scripts.interactable import _vbase__character, _vcharacter, _venemy__char, _vempty__character, _vempty__enemy
from app.variables import *
import json
import copy
import asyncio

async def login(id):
    userdata = None

    json_object = None

    file = open("json/users.json", "r")
    json_object = json.load(file)
    file.close()

    try:
        userdata = json_object[str(id)]
    except:
        # notes
        # 0 - currency
        # 1 - items
        # 2 - level
        # 3 - xp
        # 4 - abyss floor and chamber
        # 5 - party

        aether_v = copy.deepcopy(aether)
        amber_v = copy.deepcopy(amber)
        lisa_v = copy.deepcopy(lisa)
        kaeya_v = copy.deepcopy(kaeya)

        party_json = [aether_v._vconvert__json(), amber_v._vconvert__json(), lisa_v._vconvert__json(), kaeya_v._vconvert__json()]

        json_object[str(id)] = ["0", [], "0", "0", ["0", "1"], party_json]
        file = open("json/users.json", "w")
        json.dump(json_object, file)
        file.close()

    file = open("json/users.json", "r")
    json_object = json.load(file)

    file.close()
    return json_object[str(id)]

def check_game(id):
    file = open("json/games.json", "r")
    json_data = json.load(file)

    game_data = True

    try:
        data = json_data[str(id)]
    except:
        game_data = False

    return game_data

def get_game(id):
    valid = check_game(id)

    if not valid:
        return 0

    file = open("json/games.json", "r")
    json_data = json.load(file)

    game_data = json_data[str(id)]

    if game_data["type"] == "spiral abyss":
        empty = _vempty_spiral__game()

        return empty._vconvert_from__json(game_data)

    if game_data["type"] == "labyrinth warriors":
        empty = _vempty_labyrinth__game()

        return empty._vconvert_from__json(game_data)

def save_spiral(game: _vspiral__game, id):
    file = open("json/games.json", "r")
    json_data = json.load(file)
    json_data[str(id)] = game._vconvert__json()
    file.close()
    file1 = open("json/games.json", "w")
    json.dump(json_data, file1)
    file1.close()

def save_labyrinth(game: _vlabyrinth__game, id):
    file = open("json/games.json", "r")
    json_data = json.load(file)
    json_data[str(id)] = game._vconvert__json()
    file.close()
    file1 = open("json/games.json", "w")
    json.dump(json_data, file1)
    file1.close()