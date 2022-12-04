import random

def rando(chance):
    achance = chance / 10
    num = random.randint(1,10)
    if num <= achance:
        return True
    if num > achance:
        return False