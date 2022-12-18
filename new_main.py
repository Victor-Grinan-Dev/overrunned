from turtle import Turtle, Screen
from random import choice, randint
from time import sleep
from new_object import Character, Enemy

WIDTH, HEIGHT = 1270, 650

win = Screen()
win.bgcolor('medium sea green')
win.tracer(0)

game_on = True

# player
rhino_tank = 'Assets/rhino.gif'
win.addshape(rhino_tank)
player = Character('Rhino')
player.character.shape(rhino_tank)


# enemy
test_enemy = Enemy()


all_enemies = [test_enemy]
while game_on:
    win.update()

win.exitonclick()
