from app.variables import *
import random
import copy
from scripts.interactable import _vempty__character, _vempty__enemy

class _vbase__game:
    def __init__(self, id, login_data, userparty):
        self.enemies = []
        self.userid = id
        self.login_data = login_data
        self.party = userparty

class _vspiral__game(_vbase__game):
    def __init__(self, id, login_data, userparty):
        self.attri = "spiral"
        self.enemies = []
        self.userid = id
        self.login_data = login_data
        self.party = userparty
        self.chamber = self.login_data[4][1]
        self.floor = self.login_data[4][0]
        self.buffs = None

    def generate_enemies(self):
        for i in range(15):
            index = random.randint(0,(len(enemiespossible)-1))
            o = copy.deepcopy(enemiespossible[index])

            # Apply buffs to enemies
            o.char.atk += (o.char.atk * ((self.floor / (8 / self.chamber))))
            o.char.defs += (o.char.defs * ((self.floor / (8 / self.chamber))))
            o.char.hp += (o.char.hp * ((self.floor / (8 / self.chamber))))
            o.char.phys = o.char.atk / 4
            o.char.elemental = (o.char.atk / 4) * 3

            self.enemies.append(o)

    # def generate_party(self):
    #     gotten = []
    #     while len(self.party) < 4:
    #         index = random.randint(0, len(allcharacters)-1)
    #        char = allcharacters[index]
    #        if index in gotten:
    #            continue
    #        self.party.append(copy.deepcopy(char))
    #        gotten.append(index)

    def _vconvert__json(self):
        # Create the game data dict
        _vgame__data = {}

        _vgame__data[str(self.userid)] = {
            "attri": "challenge",
            "user": f"{str(self.userid)}",
            "floor/chamber": [self.floor, self.chamber],
            "enemies": [], 
            "type": "spiral abyss",
            "delete_when_done": "true"
        }

        # Get JSONable version of party
        _vparty__jsonable = []
        for i in self.party:
            _vparty__jsonable.append(self.party[i]._vconvert__json())

        # Get JSONable version of enemies
        _venemies__jsonable = []
        for i in self.enemies:
            _venemies__jsonable.append(self.enemies[i]._vconvert__json())
        
        _vgame__data["party"] = _vparty__jsonable
        _vgame__data["enemies"] = _venemies__jsonable

        return _vgame__data

    def _vconvert_from__json(self, json):
        if not json["attri"] == "challenge" or not json["type"] == "spiral abyss":
            return 1

        self.userid = int(json["user"])

        for i in json["enemies"]:
            empty = _vempty__enemy()

            self.enemies.append(empty._vconvert_from__json(i))

        self.floor = json["floor/chamber"][0]
        self.chamber = json["floor/chamber"][1]
    

class _vlabyrinth__game(_vbase__game):
    def __init__(self, difficulty, id, login_data, userparty):
        self.attri = "labyrinth"
        self.enemies = []
        self.userid = id
        self.login_data = login_data
        self.party = userparty
        self.buffs = None
        self.difficulty = difficulty

    def generate_enemies(self):
        for i in range(15):
            index = random.randint(0,(len(enemiespossible)-1))
            o = copy.deepcopy(enemiespossible[index])

            # Apply buffs to enemies
            o.char.atk += (o.char.atk * ((self.floor / (8 / self.chamber))))
            o.char.defs += (o.char.defs * ((self.floor / (8 / self.chamber))))
            o.char.hp += (o.char.hp * ((self.floor / (8 / self.chamber))))
            o.char.phys = o.char.atk / 4
            o.char.elemental = (o.char.atk / 4) * 3

            self.enemies.append(o)

    def _vconvert__json(self):
        pass

    # def generate_party(self):
    #    gotten = []
    #    while len(self.party) < 4:
    #        index = random.randint(0, len(allcharacters)-1)
    #        char = allcharacters[index]
    #        if index in gotten:
    #            continue
    #        self.party.append(copy.deepcopy(char))
    #        gotten.append(index)

def _vempty_labyrinth__game():
    return _vlabyrinth__game(0, [], [])

def _vempty_spiral__game():
    return _vlabyrinth__game(0, [], [])