import json

from scripts.interactable import _vbase__character, _vcharacter, _vempty__character, _vempty__enemy, _venemy__char
import asyncio
import os
import random
import math
from scripts.Item import _vitem
from app.variables import *
from threading import Thread
from app.Game import _vbase__game, _vlabyrinth__game, _vspiral__game
import src.logtest as logtest
import src.autosave as autosave
import copy
import threading
from asyncio_ext.cooldown import Cooldown as async_cooldown

import discord
from discord import app_commands

from discord.ui import *
from senv.senvcomp import Senv_c

senv = Senv_c()
senv.load_file(".senv")
environ = senv.get_env()
senv.close_file()

class _vclient(discord.Client):

    synced = False
    added = False

    def __init___(self):
        super().__init__(intents = discord.Intents.default())

    async def on_ready(self):
        await self.wait_until_ready()

        if not self.synced:
            await tree.sync(guild = discord.Object(id = 882070536430166067))
            self.synced = True

        if not self.added:
            self.add_view((_virtual__view()))
            self.added = True

        print(f"We have logged in as {self.user}.")
        await init_logtest()

class _virtual__view(discord.ui.View):
    def __init__(self, msg = None) -> None:
        super().__init__(timeout=None)

class _vblurple__button(discord.ui.Button):
    def __init__(self, label, custom_id, emoji=None):
        super().__init__(label=label, style=discord.ButtonStyle.blurple, emoji=emoji, custom_id=custom_id)

class _vgray__button(discord.ui.Button):
    def __init__(self, label, custom_id, emoji=None):
        super().__init__(label=label, style=discord.ButtonStyle.gray, emoji=emoji, custom_id=custom_id)

class _vgreen__button(discord.ui.Button):
    def __init__(self, label, custom_id, emoji=None):
        super().__init__(label=label, style=discord.ButtonStyle.green, emoji=emoji, custom_id=custom_id)

class _vred__button(discord.ui.Button):
    def __init__(self, label, custom_id, emoji=None):
        super().__init__(label=label, style=discord.ButtonStyle.red, emoji=emoji, custom_id=custom_id)

client = _vclient(intents = discord.Intents.default())
tree = app_commands.CommandTree(client)

async def background():
    while True:
        await client.change_presence(activity=discord.Game(name="spiral abyss"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="labyrinth warriors"))
        await asyncio.sleep(10)

def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + ' ' + item
    return str

def _vhandle__callback(callback):
    async def _vempty_callback(interaction: discord.Interaction):
        return 0
        
    if callback == None:
        return _vempty_callback

    if callback != None:
        return callback

async def init_logtest():
    await logtest.test_loop(client)

async def getreaction(e1, e2):
    if e1 == "pyro":
        if e2 == "cryo":
            return "melt"
        if e2 == "pyro":
            return "immune"
        if e2 == "electro":
            return "overload"
        if e2 == "hydro":
            return "vaporize"
        if e2 == "dendro":
            return "burning"
        if e2 == "anemo":
            return None
        if e2 == "geo":
            return None
    if e1 == "cryo":
        if e2 == "pyro":
            return "melt"
        if e2 == "electro":
            return "superconduct"
        if e2 == "hydro":
            return "freeze"
        if e2 == "cryo":
            return "immune"
        if e2 == "dendro":
            return None
        if e2 == "anemo":
            return None
        if e2 == "geo":
            return None
    if e1 == "electro":
        if e2 == "pyro":
            return "overload"
        if e2 == "hydro":
            return "electro-charged"
        if e2 == "cryo":
            return "superconduct"
        if e2 == "electro":
            return "immune"
        if e2 == "dendro":
            return None
        if e2 == "anemo":
            return None
        if e2 == "geo":
            return None
    if e1 == "hydro":
        if e2 == "electro":
            return "electro-charged"
        if e2 == "pyro":
            return "vaporize"
        if e2 == "hydro":
            return "immune"
        if e2 == "cryo":
            return "freeze"
        if e2 == "dendro":
            return None
        if e2 == "anemo":
            return None
        if e2 == "geo":
            return None

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

async def get_party(id):
    userdata = await login(id)

    party = []
    
    for i in userdata[5]:
        empty = _vempty__character()

        empty._vconvert_from__json(i)

        party.append(empty)

    return party

async def replaceuserdata(id, userdata):
    file2 = open("json/users.json", "r")
    json_data = json.load(file2)
    json_data[str(id)] = userdata
    file2.close()
    file = open("json/users.json", "w")
    json.dump(json_data, file)
    file.close()

async def addxp(id, amount):
    userdata = await login(id)

    userdata[3] = int(userdata[3])+amount

    if userdata[3] >= 1000*int(userdata[2]):
        userdata[3] = int(userdata[3])-1000
        userdata[2] = int(userdata[2])+1
    
    await replaceuserdata(id, userdata)

async def additem(id, item: _vitem, amount):
    userdata = await login(id)

    for i in range(len(userdata[1])):
        if userdata[1][i][0] == item.name:
            avamount = copy.deepcopy(userdata[1][i][1])
            userdata[1][i][1]=amount+int(avamount)
            await replaceuserdata(id, userdata)
            return

    userdata[1].append([item.name, amount])
    await replaceuserdata(id, userdata)
    return


@tree.command(name = "ping", description = "Check if shiki is responding :)", guild = discord.Object(id = 882070536430166067))
async def ping(interaction: discord.Interaction):
    user = interaction.user.id
    userdata = await login(user)
    await interaction.response.send_message("Pong!", ephemeral=True)

@tree.command(name = "help", description = "Get Help :)", guild = discord.Object(id = 882070536430166067))
async def help(interaction: discord.Interaction):
    user = interaction.user.id
    userdata = await login(user)
    await interaction.response.send_message("Check ur DMs :)")
    await interaction.user.send(embed=discord.Embed(
        title = "How to use shiki📒",
        description = """**-s!start** 🏔️ 
Use this command to start a challenge. There will be options,click on the reactions to enter one.

**-s!party** 🤼 
Use this command to check your party members.

**-s!enemies** 😈 
When activated,the command shows enemies that are in the battle,their hp and more

**-s!combat <normal-skill-burst> <member id>**💥
When command is used,your character attacks a random enemy and deals different dmg depending on what combat move and character you’re using. Remember to put a character id at the end to choose a character to attack. 
For “s!combat normal”,your character uses their normal attack and deals dmg to enemies

When “s!combat skill” is used,your character deals elemental dmg to enemies,your current character also gains energy to consume for their burst.

Finally for “s!combat burst”, the current character consumes all energy and unleashes their elemental burst.

**-s!hp <member id>** 💚 
This command shows a party members hp

**-s!feedback <your feedback>** 👍 
This command is for you to write feedback or suggestions to the devs,hope you like the bot

**-s!exit** 🏃 
When you wanna exit a challenge you have entered,use this.

**-s!ping** ✅ 
Use this command to check your ping. 

**-s!buffs** 💪 
When activated,you can use buffs to support your characters in battle,there are a few choices so choose wisely.
""",
colour = discord.Colour.dark_blue()
    ))

@tree.command(name = "feedback", description = "To give hate to devs :)", guild = discord.Object(id = 882070536430166067))
async def feedback(interaction: discord.Interaction, feedback: str):
    user = interaction.user.id
    userdata = await login(user)
    await interaction.response.send_message('Thank you for your feedback, the devs will soon see it :)')
    file=open("json/feedbacks.json", "r")
    json_data=json.load(file)
    file.close()
    feedbackstring=feedback
    json_data["feedbackcount"]=str(int(json_data["feedbackcount"])+1)
    feedbackcount=json_data["feedbackcount"]
    json_data[feedbackcount]=[interaction.user.id, feedbackstring]
    file2=open("json/feedbacks.json", "w")
    json.dump(json_data, file2)
    file2.close()

@tree.command(name = "party", description = "View your party!", guild = discord.Object(id = 882070536430166067))
async def _vparty(interaction: discord.Interaction):
    userdata = await login(interaction.user.id)

    

@tree.command(name = "combat_preview", description = "Preview the combat system", guild = discord.Object(id = 882070536430166067))
async def _vcombat_preview(interaction: discord.Interaction, type: str):
    if interaction.user.id == 718102801242259466 or interaction.user.id == 870300208431521822:
        if type == "spiral abyss":

            view = _virtual__view()

            chars = discord.ui.Select(options=[
                discord.SelectOption(label="Aether (anemo)", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                discord.SelectOption(label="Amber", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                discord.SelectOption(label="Lisa", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                discord.SelectOption(label="Kaeya", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off")
            ])

            view.add_item(chars)

            _vattack = _vblurple__button("Attack", "attack_button", "⚔")
            _vskill = _vgreen__button("Skill", "skill_button", "🌊")
            _vult = _vred__button("Ultimate", "ultimate_button", "🎇")
            _vpause = _vgray__button("Pause Game", "pause_button")

            view.add_item(_vattack)
            view.add_item(_vskill)
            view.add_item(_vult)
            view.add_item(_vpause)
        
            embed = discord.Embed(
                title = "Spiral Abyss : floor 0 chamber 0",
                description = """<this displays events during the fight>
The game will automaticaly save every 5-10 seconds or when you pause""",
                color = 0x03a5fc
            )

            embed.set_footer(text="Pause the challenge using the button or /pause and resume with /resume")

            embed.add_field(name = "Character Info", value = "<this displays info about the character>", inline = True)
            embed.add_field(name = "Enemy Info", value = "<this displays info about enemies>", inline = True)
            embed.add_field(name = "Challenge Info", value = "<this displays info about the challenge>", inline = True)

            await interaction.response.send_message(embed=embed, view=view)

        if type == "labyrinth of heroes":

            view = _virtual__view()

            embed = discord.Embed(
                title = "Please choose what preview you want to see",
                description = " ",
                color = random.randint(0, 16777215)
            )

            _vcombat = _vblurple__button("Combat", "combat_button", "⚔")
            _vidle = _vblurple__button("Idling", "idling_button", "🧍‍♂️")

            view.add_item(_vcombat)
            view.add_item(_vidle)

            async def _vidle__callback(interaction: discord.Interaction):
                _vitview = _virtual__view()

                _vattack = _vblurple__button("Move", "move_button", "🚶‍♂️")
                _vskill = _vgreen__button("Scout", "scout_button", "🔍")
                _vpause = _vgray__button("Pause Game", "pause_button")

                _vitview.add_item(_vattack)
                _vitview.add_item(_vskill)
                _vitview.add_item(_vpause)

                embed = discord.Embed(
                    title = "Labyrinth of Heroes : Chamber 0-0",
                    description = """<this displays events in the chamber>
The game will automaticaly save every 5-10 seconds or when you pause""",
                    color = 0x03a5fc
                )

                embed.set_footer(text="Pause the challenge using the button or /pause and resume with /resume")

                embed.add_field(name = "Character Info", value = "<this displays info about the character>", inline = True)
                embed.add_field(name = "Chamber Info", value = "<this displays info about the chamber, if there is a shop or anything>", inline = True)
                embed.add_field(name = "Challenge Info", value = "<this displays info about the challenge>", inline = True)

                await interaction.response.send_message(embed=embed, view=_vitview)

            async def _vcombat__callback(interaction: discord.Interaction):
                _vitview = _virtual__view()

                chars = discord.ui.Select(options=[
                    discord.SelectOption(label="Aether (anemo)", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                    discord.SelectOption(label="Amber", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                    discord.SelectOption(label="Lisa", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
                    discord.SelectOption(label="Kaeya", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off")
                ])

                _vitview.add_item(chars)

                _vattack = _vblurple__button("Attack", "attack_button", "⚔")
                _vskill = _vgreen__button("Skill", "skill_button", "🌊")
                _vult = _vred__button("Ultimate", "ultimate_button", "🎇")
                _vpause = _vgray__button("Pause Game", "pause_button")

                _vitview.add_item(_vattack)
                _vitview.add_item(_vskill)
                _vitview.add_item(_vult)
                _vitview.add_item(_vpause)

                embed = discord.Embed(
                    title = "Labyrinth of Heroes : Chamber 0-0",
                    description = """<this displays events during the fight>
The game will automaticaly save every 5-10 seconds or when you pause
You encountered some enemies! Defeat them all before you can move to another chamber""",
                    color = 0x03a5fc
                )

                embed.set_footer(text="Pause the challenge using the button or /pause and resume with /resume")

                embed.add_field(name = "Character Info", value = "<this displays info about the character>", inline = True)
                embed.add_field(name = "Enemy Info", value = "<this displays info about enemies>", inline = True)
                embed.add_field(name = "Chamber Info", value = "<this displays info about the chamber>", inline = True)

                await interaction.response.send_message(embed=embed, view=_vitview)

            _vcombat.callback = _vhandle__callback(_vcombat__callback)
            _vidle.callback = _vhandle__callback(_vidle__callback)

            await interaction.response.send_message(embed=embed, view=view)

    else:
        await interaction.response.send_message("This command is dev-only")

    

@tree.command(name = "challenge", description = "Start A Challenge :)", guild = discord.Object(id = 882070536430166067))
async def challenge(interaction: discord.Interaction):
    user = interaction.user.id
    userdata = await login(user)
    inter = interaction

    await interaction.response.send_message("The challenge function is in beta, expect bugs! :)", ephemeral=True)

    view=_virtual__view()

    _vspiral = _vblurple__button("", "spiral_abyss", "🌀")
    _vlabyrinth = _vblurple__button("", "labyrinth_warriors", "🏚️")
    _vnvm = _vblurple__button("nevermind", "_nvm__b")

    view.add_item(_vspiral)
    view.add_item(_vlabyrinth)
    view.add_item(_vnvm)

    async def _vspiral__callback(interaction: discord.Interaction):
        await interaction.response.send_message("Spiral abyss is launching...", ephemeral=True)

        # launch the game
        party = await get_party(user)

        _vgame = _vspiral__game(id = interaction.user.id, login_data = userdata, userparty = party)

        async def placeholder_callback():
            await _vhandle_spiral__game(game = _vgame, interaction = interaction)

        def _vcl():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            loop.run_until_complete(placeholder_callback())
            loop.close()

        _thread = threading.Thread(target=_vcl)
        _thread.start()


        _vspiral.callback = _vhandle__callback(None)
        _vlabyrinth.callback = _vhandle__callback(None)

    async def _vlabyrinth__callback(interaction: discord.Interaction):
        await interaction.response.send_message("The labyrinth of Heroes mode is still in development sorry! :(", ephemeral=True)
        _vspiral.callback = _vhandle__callback(None)
        _vlabyrinth.callback = _vhandle__callback(None)

    async def _vnvm__callback(interaction: discord.Interaction):
        await interaction.response.send_message("Okay then...", ephemeral=True)
        _vspiral.callback = _vhandle__callback(None)
        _vlabyrinth.callback = _vhandle__callback(None)
        _vnvm.callback = _vhandle__callback(None)

    # if len(userdata[4]) != 0:
    #     interaction.response.send_message("You can't start a challenge when you are already in one!", ephemeral=True)
    #     return

    _vspiral.callback = _vhandle__callback(_vspiral__callback)
    _vlabyrinth.callback = _vhandle__callback(_vlabyrinth__callback)
    _vnvm.callback = _vhandle__callback(_vnvm__callback)

    embed = discord.Embed(
    title = 'Hi traveler!',
    description = '''Select a challenge:
🌀 Spiral abyss
🏚️ Labyrinth warriors''',
    colour = random.randint(0, 16777215)
    )
    await interaction.followup.send(embed=embed, view=view, ephemeral=True)

async def _vhandle_spiral__game(game: _vspiral__game, interaction: discord.Interaction):
    userdata = await login(interaction.user.id)

    view = _virtual__view()
    _vyes = _vblurple__button("Yes", "yes_button", "✔")
    _vno = _vblurple__button("No", "no_button", "❌")

    async def yes_callback(interaction: discord.Interaction):

        _v__view = _virtual__view()
        _vstart = _vgreen__button("Start", "start_button")

        async def start_callback(interaction: discord.Interaction):
            pass

        _v__view.add_item(_vstart)

        _vembed = discord.Embed(
            title=f"Spiral Abyss : floor {userdata[4][0]} chamber {userdata[4][1]}",
            description="The game will automaticaly save every 5-10 seconds or when you pause",
            color=0x03a5fc
        )

        _vembed.add_field(name="Challenge Info", value="Defeat all enemies", inline=True)

        _vembed.set_footer("THE AUTOSAVE FEATURE IS STILL IN HEAVY DEVELOPENT, YOU ARE BOUND TO LOSE YOUR DATA AT ANY MOMENT")

        await interaction.response.send_message(view=_v__view, embed=embed, ephemeral=True)
        _vno.callback = _vhandle__callback(None)
        _vyes.callback = _vhandle__callback(None)

    async def no_callback(interaction: discord.Interaction):
        await interaction.response.send_message("Alright...", ephemeral=True)
        _vyes.callback = _vhandle__callback(None)
        _vno.callback = _vhandle__callback(None)

    _vyes.callback = _vhandle__callback(yes_callback)
    _vno.callback = _vhandle__callback(no_callback)

    view.add_item(_vyes)
    view.add_item(_vno)

    embed = discord.Embed(
        title="Spiral Abyss Status:",
        description=f"""You are currently on floor {userdata[4][0]}, chamber {userdata[4][1]}
Do you want to continue?""",
        color=0xab03ff
    )

    await interaction.followup.send(embed=embed, ephemeral=True, view=view)

async def _vhandle_labyrinth__game(game: _vlabyrinth__game):
    pass

@tree.command(name = "battle_test", description = "Test", guild = discord.Object(id = 882070536430166067))
async def test(interaction: discord.Interaction):
    _vcur_seleted = None

    view = _virtual__view()

    chars = discord.ui.Select(
        placeholder="Choose a Character",
        options=[
        discord.SelectOption(label="Aether (anemo)", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
        discord.SelectOption(label="Amber", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
        discord.SelectOption(label="Lisa", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off"),
        discord.SelectOption(label="Kaeya", emoji="😐", description="hp: 0, infused: 0, buffs: 0, ult: on/off")
    ])

    view.add_item(chars)

    _vattack = _vblurple__button("Attack", "attack_button", "⚔")
    _vskill = _vgreen__button("Skill", "skill_button", "🌊")
    _vult = _vred__button("Ultimate", "ultimate_button", "🎇")
    _vpause = _vgray__button("Pause Game", "pause_button")

    view.add_item(_vattack)
    view.add_item(_vskill)
    view.add_item(_vult)
    view.add_item(_vpause)
        
    embed = discord.Embed(
        title = "Spiral Abyss : floor 0 chamber 0",
        description = """<this displays events during the fight>
The game will automaticaly save every 5-10 seconds or when you pause""",
        color = 0x03a5fc
    )

    embed.set_footer(text="Pause the challenge using the button or /pause and resume with /resume")

    embed.add_field(name = "Character Info", value = "<this displays info about the character>", inline = True)
    embed.add_field(name = "Enemy Info", value = "<this displays info about enemies>", inline = True)
    embed.add_field(name = "Challenge Info", value = "<this displays info about the challenge>", inline = True)

    await interaction.response.send_message(embed=embed, view=view)
    
#@tree.command(name = "challenge", description = "Start A Challenge :)", guild = discord.Object(id = 882070536430166067))
#async def challenge(interaction: discord.Interaction):
#@tree.command(name = "challenge", description = "Start A Challenge :)", guild = discord.Object(id = 882070536430166067))
#async def challenge(interaction: discord.Interaction):
#
#while True:
#    if not logtest.done:
#        continue
#    else:
#        break

client.run(environ["token"])