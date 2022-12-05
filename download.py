# If for whatever reason you want to download the source code of Shiki Taishou Rewrite
# And if you dont have git
#
# If you have git use: git clone https://github.com/Henrydev-tran/Discord-Shiki-Rewrite.git
#
# You can use this file to download the source code on the current directory

import os
import requests
import time

print("The source code of Discord-Shiki-Taishou will be downloaded on this directory and it will replace previous version of Shiki Taishou installed on this directory.")
confirmation = input("Do you confirm? (Y/n) ")

while confirmation.lower() != "y" and confirmation.lower() != "n":
    confirmation = input("Input not recognized, please try again: (Y/n) ")

if confirmation.lower() == "n":
    os._exit(0)

def get_file(dir, link):
    response = requests.get(link)
    page_source = response.text
    file = open(dir, "w", encoding="utf-8")
    file.write(page_source)
    file.close()
    page_source = None
    response = None

current = time.time()

if not os.path.exists("./src"):
    os.mkdir("src")
if not os.path.exists("./app"):
    os.mkdir("app")
if not os.path.exists("./scripts"):
    os.mkdir("scripts")
    os.mkdir("scripts/addons")

get_file("main.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/main.py")
get_file("requirements.txt", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/requirements.txt")
get_file(".gitignore", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/.gitignore")
get_file("README.md", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/README.md")
get_file("LICENSE", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/LICENSE")
get_file("app.project", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/app.project")
get_file("src/logtest.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/src/logtest.py")
get_file("src/autosave.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/src/autosave.py")
get_file("scripts/interactable.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/scripts/interactable.py")
get_file("scripts/Item.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/scripts/Item.py")
get_file("scripts/addons/rando.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/scripts/addons/rando.py")
get_file("app/Game.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/app/Game.py")
get_file("app/dbset.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/app/dbset.py")
get_file("app/variables.py", "https://raw.githubusercontent.com/Henrydev-tran/Discord-Shiki-Rewrite/master/app/variables.py")

print(f"Done in {time.time() - current} seconds")
