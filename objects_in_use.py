from objects.armoury import *
from objects.character import Character
from objects.enemy import Enemy

# alma = Character("Alma", weapons_list=[pistol])
# annu = Character("Annu", weapons_list=[auto_assault_rifle])
# viti = Character("Viti", weapons_list=[fragmentation_missile_launcher])

enemy = Enemy()

thelonius = Character("Thelonius", weapons_list=[armoury_list[0]])

if __name__ == '__main__':
    from objects.game import Setup
    from turtle import Screen

    win = Screen()
    win.setup(Setup.WIDTH, Setup.HEIGHT)  # each step is 10... or every 10pixels 1 inch
    win.bgcolor("green")
    win.title("BATTLE TURTLE")
    win.tracer(0)

    game_on = True

    print(enemy)
    print(thelonius)

    while game_on:
        win.update()

    win.exitonclick()
