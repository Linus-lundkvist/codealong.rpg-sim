
from resources import Character, Råtta, Adam, save_character, load_characters
import random 


def fight(fighter : Character, enemies : list):

    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health:
            print("Target has died!")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
    print(f"Fight is over! {fighter.name} won")

def new_fight(players: list, enemis : list):
    participents = players + enemis # slå ihop alla deltagare 
    random.shuffle(participents)

    for char in participents:
        #check if råtta or character
        if char in players:
            target = random.choice(enemis)

        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} has killd {target.get_name()}")
            if (type(target) == Råtta):
                enemis.remove(target)
            elif (type(target) == Adam):
                enemis.remove(target)
            else:
                players.remove(target)
            participents.remove(target)

        else: 
            print(f"{target.get_name()} was attacked by {char.get_name()}.")
            print(f"{target.get_name()} has {target.get_health()} healhpoints left.")
        if len(players) == 0 or len(enemis) == 0: break

def main():
    enemies = []
    players = []

    mulle = Character("Mulle", 30, 28, 0) #17
    bufa = Character("Bufa", 15, 48, 0) #7
    eskil = Character("Eskil", 20, 20, 0) #15
    salka = Character("salka", 10, 3, 0) #25

    #adam = Råtta("Adam", 1, 0.5, 0)  
    #råtta = Råtta("Råtta", 3, 2.5, 1)

    players.append(salka)
    players.append(eskil)

    print(mulle)
    print()
    print(bufa)
    print()
    print(eskil)
    print()
    print(salka)

    adams = 0
    råttor = 0
    for _ in range(0,random.randint(1,20)):
        if 1 == random.randint(1,2):
            adams = adams + 1
            enemies.append(Adam(adams))
        elif 2 == random.randint(1,2):
            råttor = råttor + 1     
            enemies.append(Råtta(råttor))


    #fight(eskil, enemies)
    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)
    if len(enemies) == 0:
        print("The players won!")
    elif len(players) == 0:
        print("The Råttoe won!")

    #save_character(eskil)
    players = load_characters()

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
