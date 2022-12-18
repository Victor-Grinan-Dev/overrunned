from turtle import Turtle
from objects.game import Setup as win
from random import choice, randint

all_enemies = []


class Enemy(Turtle):
    max_speed = 1
    level = 1

    def __init__(self):
        super().__init__()

        # self.name = heroes.gen()
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
        if abs(current_x) - win.MELEE == 0 and abs(current_y) - win.MELEE == 0:
            print("explode")
            # self.attack()
            # self.explode()

    @staticmethod
    def generate_position():
        position = choice(win.OUTLINE)

        if position == win.OUTLINE[0] or position == win.OUTLINE[1]:
            return randint(position[0], position[1]), randint(0 - win.WIDTH / 2, win.WIDTH / 2)
        else:
            return randint(0 - win.HEIGHT / 2, win.HEIGHT / 2), randint(position[0], position[1])

    # @staticmethod
    # def spawn(n, birth_position):
    #     # give birth to more enemies
    #     for _ in range(n):
    #         new_born = Enemy()
    #         print(f"birth position {birth_position}")
    #         # self.goto(birth_position)
    #         all_enemies.append(new_born)
    #
    # def got_hit(self):
    #     self.enemy.color("yellow")
    #     win.update()
    #     self.enemy.color("red")
    #     win.update()
    #     self.enemy.color("yellow")
    #     win.update()
    #     self.enemy.color("red")
    #     win.update()
    #     self.enemy.hideturtle()
    #
    # def attack(self):
    #     print(f"attacking: {self.name}")
    #     win.ontimer(self.attack, int(1000 / self.attack_rate))
    #
    # def shoot(self):
    #     # reduce the health of closer character
    #     pass
    #
    # def charge(self):
    #     # sprint forward the character
    #     if Character.nearest_enemy()[1] >= 50:
    #         self.max_speed *= 2
    #
    # def explode(self):
    #     # reduce the health of closer character
    #     print(f"explodes: {self.name}")
    #     self.enemy.hideturtle()
    #     # TODO: explosion animation
    #     all_enemies.remove(self.enemy)


if __name__ == '__main__':
    enemy = Enemy()
    print(enemy)
