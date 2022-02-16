#imports
#global variebels

#classes
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
#main code