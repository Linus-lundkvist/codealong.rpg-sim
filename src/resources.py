#imports
#global variebels

#classes
from numpy import character


class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"
    
    def take_damage(self, damage):
        actual_damage = damage - self.armor
        if actual_damage < 0: actual_damage = 0
        if (self.health -  actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage

    def attack(self):
        return self.damage

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name

    def get_all_atributs(self):
        return self.name, self.health, self.damage, self.armor

class Råtta:

    def __init__(self, id):
        self.id = id
        self.health = 3
        self.damage = 2.5
        self.armor = 1
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0
        if (self.health -  actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage

    def attack(self):
        return self.damage
    
    def get_health(self):
        return self.health
    
    def get_name(self):
        return f"Råtta #{self.id}"

class Adam:

    def __init__(self, id):
        self.id = id
        self.health = 1
        self.damage = 0.5
        self.armor = 0
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0
        if (self.health -  actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage

    def attack(self):
        return self.damage
    
    def get_health(self):
        return self.health
    
    def get_name(self):
        return f"Adam #{self.id}"
    
#functions
def hello():
    print("Hello World")

def save_character(character : Character):
    """
    Tar in caraktär, bryter ner dess atribut och sparar ner på fil.

    Aegs: 
        character (character): Det objekt som ska sparas ner på fil.

    """

    name, health, damage, armor = character.get_all_atributs()
    with open("character_file.text", "w", encoding="utf8") as f:
        save_sting = f"{name}/{health}/{damage}/{armor}\n"
        f.write(save_sting)
        print(f"{name} has been successfully saved. ")

def load_characters():

    with open("character_file.text", "r", encoding="utf8") as f:
        characters = [] 
        for line in f.readlines():
            attributes = line.split("/")
            this_char = Character(attributes[0],
                                  int(attributes[1]),
                                  int(attributes[2]),
                                  int(attributes[3]))
            characters.append(this_char)
    print("Characters has ben loaded")
    return characters

#main code