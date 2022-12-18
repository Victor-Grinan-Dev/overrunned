from turtle import Turtle
from random import randint, choice

WIDTH, HEIGHT = 1270, 650

# game_speed
GAME_SPEED = 1
FRAME_SPEED = "fastest"
MELEE = 10  # melee distance

# map borders
OUTLINE_THICKNESS = 5
OUTLINE_TOP = int(HEIGHT / 2), int(HEIGHT / 2) + OUTLINE_THICKNESS
OUTLINE_BOTTOM = 0 - int(HEIGHT / 2) - OUTLINE_THICKNESS, 0 - int(HEIGHT / 2)
OUTLINE_RIGHT = int(WIDTH / 2), int(WIDTH / 2) + OUTLINE_THICKNESS
OUTLINE_LEFT = 0 - int(WIDTH / 2) - OUTLINE_THICKNESS, 0 - int(WIDTH / 2)
OUTLINE = [OUTLINE_TOP, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_LEFT]

all_enemies = []


class Character:
    level = 1
    speed = 4 + level

    def __init__(self, name):
        self.name = name
        self.character = Turtle()

        self.character.color("darkblue")
        self.character.penup()
        self.character.speed = "fastest"
        self.character.left(90)


class Enemy(Turtle):
    max_speed = 1
    level = 1

    def __init__(self):
        super().__init__()

        self.hideturtle()

        self.shape("turtle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.starting_pos = self.generate_position()
        self.goto(self.starting_pos)
        self.setheading(self.towards(0, 0))
        self.showturtle()

        self.current_pos = self.pos()
        self.attack_rate = self.level

        self.name = "Baddy"
        self.move()

    def __repr__(self):
        return f"name: {self.name} lvl: {self.level} at {self.current_pos}"

    def move(self):
        self.setheading(self.towards(0, 0))
        self.forward(randint(int(self.max_speed / 2), self.max_speed))
        current_x = self.xcor()
        current_y = self.ycor()
        if abs(current_x) - MELEE == 0 and abs(current_y) - MELEE == 0:
            print("explode")
            # self.attack()
            # self.explode()

    def attack(self):
        pass

    @staticmethod
    def generate_position():
        position = choice(OUTLINE)

        if position == OUTLINE[0] or position == OUTLINE[1]:
            return randint(position[0], position[1]), randint(0 - WIDTH / 2, WIDTH / 2)
        else:
            return randint(0 - HEIGHT / 2, HEIGHT / 2), randint(position[0], position[1])
