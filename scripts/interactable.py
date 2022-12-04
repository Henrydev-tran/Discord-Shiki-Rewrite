import scripts.addons.rando as rando

def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1", "True")

class _vbase__character:
    def __init__(self, hp, atk, defs, critdmg, critrate, skill, ult, element, name, heal, responsetime = 0):
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.phys = atk / 4
        self.elemental = (atk / 4) * 3
        self.critdmg = critdmg
        self.critrate = critrate
        self.skill = skill
        self.ult = ult
        self.element = element
        self.name = name
        self.heal = heal
        self.reptime = responsetime
        self.infused = None
    ultavail = False
    afflicted = None

class _vcharacter:
    skillused = 0
    skillon = True
    def __init__(self, base: _vbase__character, role, skillcooldown=5, ultthreshold=5):
        self.base = base
        self.role = role
        self.char = base
        self.threshold = ultthreshold
        self.skillcooldown = skillcooldown
    def take_dmg(self, enemie_dmg):
        self.char.hp -= (enemie_dmg - self.char.defs / 2)
    def attack(self):
        total = self.char.phys * 1.5
        sett = []
        if rando.rando(self.char.critrate):
            total *= (self.char.critdmg / 100)
            sett.append(total)
            sett.append(True)
        else:
            sett.append(total)
            sett.append(False)
        return sett

    def skill(self):
        if self.skillused < self.threshold:
            self.skillused += 1
        total = (self.char.atk * (self.char.skill / 100))
        sett = []
        if rando.rando(self.char.critrate):
            total *= (self.char.critdmg / 100)
            sett.append(total)
            sett.append(True)
        else:
            sett.append(total)
            sett.append(False)
        sett.append(self.char.element)
        return sett

    def ult(self):
        self.skillused = 0
        total = (self.char.atk * (self.char.ult / 100))
        sett = []
        if rando.rando(self.char.critrate):
            total *= (self.char.critdmg / 100)
            sett.append(total)
            sett.append(True)
        else:
            sett.append(total)
            sett.append(False)
        sett.append(self.char.element)
        return sett

    def heal(self, chars):
        for i in range(len(chars)):
            chars[i].char.hp += self.char.heal

    def _vconvert__json(self):
        if self.char.infused == None:
            infused = "None"

        _vcharacter__data = {
            "attri": "character",
            "name": self.char.name,
            "role": self.role,
            "element": self.char.element,
            "spec_stats": {
                "skill_dmg": self.char.skill,
                "ult_dmg": self.char.ult,
                "healing_count": self.char.heal,
                "elemental_atk": self.char.elemental,
                "physical_atk": self.char.phys
            }, 
            "stats": {
                "hp": self.char.hp,
                "def": self.char.defs,
                "atk": self.char.atk,
                "crit_dmg": self.char.critdmg,
                "crit_rate": self.char.critrate
            },
            "character_abilities": {
                "skill_on": str(self.skillon),
                "ult_available": str(self.char.ultavail),
                "infused": infused
            }
        }

        return _vcharacter__data

    def _vconvert_from__json(self, jsondata):
        e = jsondata

        if e['attri'] != "character":
            return 1

        self.char.name = e["name"]
        self.role = e["role"]
        self.char.element = e["element"]

        self.char.skill = int(e["spec_stats"]["skill_dmg"])
        self.char.ult = int(e["spec_stats"]["ult_dmg"])
        self.char.heal = int(e["spec_stats"]["healing_count"])
        self.char.elemental = int(e["spec_stats"]["elemental_atk"])
        self.char.phys = int(e["spec_stats"]["physical_atk"])

        self.char.hp = int(e["stats"]["hp"])
        self.char.defs = int(e["stats"]["def"])
        self.char.atk = int(e["stats"]["def"])
        self.char.critdmg = int(e["stats"]["crit_dmg"])
        self.char.critrate = int(e["stats"]["crit_rate"])

        self.skillon = str2bool(e["character_abilities"]["skill_on"])
        self.char.ultavail = str2bool(e["character_abilities"]["ult_available"])
        self.char.infused = e["character_abilities"]["infused"]



class _venemy__char:
    def __init__(self, base: _vbase__character, haveshields=False):
        self.base = base
        self.char = base
        self.haveshields = haveshields
    def attack(self):
        return self.char.atk
    def take_dmg(self, dmg, empt):
        if not empt:
            self.char.hp -= (dmg - self.char.defs / 2)
        if empt:
            self.char.hp -= dmg

    def _vconvert__json(self):
        infused = self.char.infused

        if infused == None:
            infused = "None"

        _venemy__data = {
            "attri": "enemy",
            "name": self.char.name,
            "element": self.char.element,
            "spec_stats": {
                "have_shields": self.haveshields
            }, 
            "stats": {
                "hp": self.char.hp,
                "def": self.char.defs,
                "atk": self.char.atk,
                "crit_dmg": self.char.critdmg,
                "crit_rate": self.char.critrate
            },
            "enemy_abilities": {
                "infused": infused,
                "response_time": self.char.reptime,
            }
        }

        return _venemy__data

    def _vconvert_from__json(self, jsondata):
        e = jsondata

        if e['attri'] != "enemy":
            return 1

        self.char.name = e["name"]
        self.char.element = e["element"]

        self.haveshields = e["spec_stats"]["have_shields"]

        self.char.hp = int(e["stats"]["hp"])
        self.char.defs = int(e["stats"]["def"])
        self.char.atk = int(e["stats"]["def"])
        self.char.critdmg = int(e["stats"]["crit_dmg"])
        self.char.critrate = int(e["stats"]["crit_rate"])

        self.char.infused = e["character_abilities"]["infused"]
        self.char.reptime = e["character_abilities"]["response_time"]
        
def _vempty__character():
    return _vcharacter(_vbase__character(0, 0, 0, 0, 0, 0, 0, 'element', 'name', 0), "placeholder")
def _vempty__enemy():
    return _venemy__char(_vbase__character(0, 0, 0, 0, 0, 0, 0, 'element', 'name', 0, 0))