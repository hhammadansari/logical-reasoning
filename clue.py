# Need to determine exactly one suspect, one room, and one weapon

import termcolor

from logic import *

# Suspects
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

# Rooms
ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

# Weapons
knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: Yes", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),
) # At least one of each category is true

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
)) # At least one of these is true

knowledge.add(Not(plum)) 
knowledge.add(Not(ballroom))

check_knowledge(knowledge)