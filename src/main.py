from re import S
from resources import Character, Råtta
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


def main():
    enemies = []

    mulle = Character("Mulle", 30, 28, 17)
    bufa = Character("Bufa", 15, 48, 7)
    eskil = Character("Eskil", 20, 20, 15)
    salka = Character("salka", 10, 3, 25)

    adam = Råtta("Adam", 1, 0.5, 0)
    råtta = Råtta("Råtta", 3, 2.5, 1)

    print(mulle)
    print()
    print(bufa)
    print()
    print(eskil)



    enemies.append(adam)
    enemies.append(råtta)
    print("\nRåttor")
    print(enemies[0],"\n",enemies[1])

    fight(mulle, enemies)

if __name__ == "__main__":
    main()
