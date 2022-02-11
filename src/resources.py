#imports
#global variebels

#classes
class Character:

    def __init__(self, name, health, damage, armor) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"


#functions
def hello():
    print("Hello World")
#main code