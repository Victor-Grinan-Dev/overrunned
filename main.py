from turtle import Screen
from objects.weapon import pistol
from objects.enemy import Enemy
from objects.enemy import all_enemies
from objects.character import thelonius
from objects.game import Setup

# window setup
win = Screen()
win.setup(Setup.WIDTH, Setup.HEIGHT)  # each step is 10... or every 10pixels 1 inch
win.bgcolor("green")
win.title("BATTLE TURTLE")
win.tracer(0)
#
# # globals and general variables
# game_on = True
# enemy_max_speed = Setup.level * 2
# char_speed = 5
#
#
# # global enemy
#
#
# # FUNCTIONS
# def generate_enemy(n=1):
#     for new_enemy in range(n):
#         new_enemy = Enemy()
#         all_enemies.append(new_enemy)
#
#
# def move_left():  # working
#     for enemy_ in all_enemies:
#         posx = enemy_.xcor()
#         enemy_.goto(posx + char_speed, enemy_.pos()[1])
#         # also move scenery
#
#
# def move_right():  # working
#     global enemy
#     # for enemy in enemies:
#     #   enemy.goto(coordenades)
#     for enemy in all_enemies:
#         posx = enemy.pos()[0]
#         enemy.goto(posx - char_speed, enemy.pos()[1])
#         # also move scenery
#
#
# def move_up():  # working
#     global enemy
#     # for enemy in enemies:
#     #   enemy.goto(coordenades)
#     for enemy in all_enemies:
#         posy = enemy.pos()[1]
#         enemy.goto(enemy.pos()[0], posy - char_speed)
#         # also move scenery
#
#
# def move_down():  # working
#     global enemy
#     # for enemy in enemies:
#     #   enemy.goto(coordenades)
#     for enemy in all_enemies:
#         posy = enemy.pos()[1]
#         enemy.goto(enemy.pos()[0], posy + char_speed)
#         # also move scenery
#
#
# win.listen()
# win.onkey(key="a", fun=move_left)
# win.onkey(key="d", fun=move_right)
# win.onkey(key="w", fun=move_up)
# win.onkey(key="s", fun=move_down)
#
# # squad members will shoot their weapons when an enemy gets in attack range, the target will be always the closest
# enemy # if the targets cross the melee range, melee weapon is used instead. if no melee weapon use pistol. #
# character wont shoot if another character is in the line of fire.
#
#
# # when move keys are pressed, the squad of characters stays in position and all the scenography moves to create
# # squad moving effect
#
#
# sargent = Character("Thelonius", [pistol])
# generate_enemy(Setup.level * 5)
#
# # game loop
# while game_on:
#
#     if all_enemies:
#         for enemy in all_enemies:
#             enemy.move()
#
#         # sargent.facing()
#     win.ontimer(generate_enemy, 1000)
#     # target = in_range(sargent.weapons)  # make the weapon shoot on the time it should
#     # hit_target(target)
#
#     win.update()

# win.ontimer(heavy_bolter.in_range, 1000)
# win.ontimer(enemy.move, 100000)
# win.ontimer(game_frame, 100)
win.exitonclick()
if __name__ == '__main__':

    win = Screen()
    win.bgcolor("green")
    win.tracer(0)

    print(thelonius)

    processes = []

    # controls
    # def move_left():  # working
    #     global enemy
    #     for enemy in all_enemies:
    #         posx = enemy.pos()[0]
    #         enemy.goto(posx + sgt.max_speed, enemy.pos()[1])  # TODO:  instead of sgt.max_speed should be all squad's
    #         # also move scenery
    #
    #
    # def move_right():  # working
    #     global enemy
    #     # for enemy in enemies:
    #     #   enemy.goto(coordenades)
    #     for enemy in all_enemies:
    #         posx = enemy.pos()[0]
    #         enemy.goto(posx - sgt.max_speed, enemy.pos()[1])  # TODO: instead of sgt.max_speed should be all squad's
    #         # also move scenery
    #
    #
    # def move_up():  # working
    #     global enemy
    #     # for enemy in enemies:
    #     #   enemy.goto(coordenades)
    #     for enemy in all_enemies:
    #         posy = enemy.pos()[1]
    #         enemy.goto(enemy.pos()[0], posy - sgt.max_speed)  # TODO:  instead of sgt.max_speed should be all squad's
    #         # also move scenery
    #     pass
    #
    #
    # def move_down():  # working
    #     global enemy
    #     # for enemy in enemies:
    #     #   enemy.goto(coordenades)
    #     for enemy in all_enemies:
    #         posy = enemy.pos()[1]
    #         enemy.goto(enemy.pos()[0], posy + sgt.max_speed)  # TODO:  instead of sgt.max_speed should be all squad's
    #         # also move scenery
    #
    #
    # win.listen()
    # win.onkey(key="a", fun=move_left)
    # win.onkey(key="d", fun=move_right)
    # win.onkey(key="w", fun=move_up)
    # win.onkey(key="s", fun=move_down)
    #
    # # create the initial enemies
    # for _ in range(10):
    #     new_enemy = Enemy()
    #     all_enemies.append(new_enemy)
    #
    while True:
        win.update()

        for enemy in all_enemies:
            enemy.move()

win.exitonclick()