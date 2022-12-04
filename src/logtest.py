import datetime
import os.path
import asyncio
import math
import discord
import copy
from src.autosave import *

autosave_queue = []

tempdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

date = datetime.datetime.today().strftime("%d-%m-%Y")
done = False

def log(text: str, file = None, console = True, ent=False):
    global date
    
    newdate = datetime.datetime.today().strftime("%d-%m-%Y")
    if date != newdate:
        date = newdate
        new_logfile(True)
    
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    if console:
        print(f"[Vanguard Logs][{dt_string}]: {text}")
        
    if file == "standard":        
        file = open(f"logs/Logs {date}.log", "a")
        if ent:
            file.write("""
""")
        file.write(f"[Vanguard Logs][{dt_string}]: {text}")
        file.close()
        return
        
    if file != None:
        file = open(f"{file}.log", "a")
        if ent:
            file.write("""
""")
        file.write(f"[Log][{dt_string}]: {text}")
        file.close()
        
def new_logfile(console):
    log(f"Creating a log file for {date}")
    
    if os.path.exists(f"Logs {date}.log"):
        log("Log file already exist, skipping step")
    else:
        log(f"Created a log file for {date}", "standard", console=True, ent=True)
    log("Done")

def check_anomalies():
    global date
    
    log("Checking for date anomalies", "standard", ent=True)
    r_date = datetime.datetime.today().strftime("%d-%m-%Y")
    if r_date != date:
        log("Anomaly detected, fixing", "standard", ent=True)
        log("Anomaly resolved, done", "standard", ent=True)
        date = r_date
        new_logfile(True)
    else:
        log("No anomaly detected, done", "standard", ent=True)
        
# Start Logging
log("Log is now active")
log("Checking for date anomalies, step 1/3")
r_date = datetime.datetime.today().strftime("%d-%m-%Y")
if r_date != date:
    log("Anomaly detected, fixing")
    date = r_date
    log("Anomaly resolved, step 1/3 done")
else:
    log("No anomaly detected, step 1/3 done")

log(f"Creating a log file for {date}, step 2/3")

if os.path.exists(f"Logs {date}.log"):
    log("Log file already exist, skipping step 2/3")
else:
    log(f"Created a log file for {date}", "standard", console=True, ent=True)
    log("Step 2/3 done")
    
log("Starting bot, step 3/3")
log("Step 3/3 done")

done = True
    
async def test_loop(client: discord.Client):
    r_c = 0
    s = True
    highest = 0
    
    while True:
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)
        
        await asyncio.sleep(5)
        
        s = not s

        if s == True:
            await client.change_presence(activity=discord.Game(name="spiral abyss"))
        else:
            await client.change_presence(activity=discord.Game(name="labyrinth warriors"))
        
        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        s = not s

        if s == True:
            await client.change_presence(activity=discord.Game(name="spiral abyss"))
        else:
            await client.change_presence(activity=discord.Game(name="labyrinth warriors"))

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)

        await asyncio.sleep(5)

        if len(autosave_queue) != 0:
            for game in autosave_queue:
                if game.attri == "spiral":
                    save_spiral(game, game.userid)
                if game.attri == "labyrinth":
                    save_labyrinth(game, game.userid)
        
        # Log bot latency
        if r_c%3==0:
            latency = client.latency
            latency *= 1000
            
            log("", "standard", False, True)
            log(f"""Checking bot latency""", "standard", False, True)
            log(f"Bot latency: {latency}ms", "standard", False, True)
            
            if latency > 400:
                if latency > highest:
                    highest = copy.deepcopy(latency)
                log(f"lag spike encountered, top ping: {highest}", "standard", True, True)
        
        r_c+=1
        
        # Check date anomalies
        if r_c%40==0:
        	check_anomalies()
    
  