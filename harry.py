# This program uses the logic module to determine if it is raining outside based on the following rules:

# If it is not raining, then Hagrid is outside.
# If it is not raining, then Dumbledore may be outside.
# Hagrid and Dumbledore cannot be outside together.
# Dumbledore is outside.

from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(Not(rain), dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())

print(model_check(knowledge, rain))