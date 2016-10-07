# import av diverse

import random

# alla stats 0-100 eller bool
class djur:
    def __init__(self,species, namn):
        self.species = species
        self.namn = namn
        self.hunger = random.randint(50,100)
        self.attachment = random.randint(25,50)
        self.hygiene = random.randint(0,100)
        self.fun = random.randint()
        self.alive = True
        self.social = random.randint(40,60)
        self.sick = False
        self.
