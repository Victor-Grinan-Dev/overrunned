from turtle import Turtle, Screen
from random import choice, randint
from time import sleep
import heroes

GAME_SPEED = 1
FRAME_SPEED = 0.1  # "fastest"
MELEE = 10  # melee distance

WIDTH = 700
HEIGHT = 600

OUTLINE_THICKNESS = 5
OUTLINE_TOP = int(HEIGHT / 2), int(HEIGHT / 2) + OUTLINE_THICKNESS
OUTLINE_BOTTOM = 0 - int(HEIGHT / 2) - OUTLINE_THICKNESS, 0 - int(HEIGHT / 2)
OUTLINE_RIGHT = int(WIDTH / 2), int(WIDTH / 2) + OUTLINE_THICKNESS
OUTLINE_LEFT = 0 - int(WIDTH / 2) - OUTLINE_THICKNESS, 0 - int(WIDTH / 2)
OUTLINE = [OUTLINE_TOP, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_LEFT]

game_on = True
all_enemies = []
armoury = []


class Sprite:

    def __init__(self):
        self.sprite = Turtle()
        self.sprite.penup()
        self.sprite.speed(FRAME_SPEED)


class Weapon:

    def __init__(self, weapon_name, weapon_range, damage, attack_per_second, clip, reload, weight):

        self.weapon = Turtle()
        self.weapon.shape("square")
        self.weapon.shapesize(0.5, 0.1, 1)  # pistol size
        self.weapon.penup()
        self.weapon.color("black")
        self.weapon.speed(FRAME_SPEED)

        self.weapon_name = weapon_name
        self.w_range = weapon_range
        self.damage = damage
        self.attack_per_second = attack_per_second
        self.max_capacity = clip
        self.weight = weight

        self.clip = self.max_capacity
        self.reload_time = reload

        self.gun_barrel = (0, 10)  # TODO: get the position of the weapon barrel
        self.attack_rate = int(1 / self.attack_per_second)

    def __repr__(self):
        return f"weapon_name:   {self.weapon_name}\nrange:         {self.w_range}\ndamage:        {self.damage}\n" \
               f"attack rate:   {self.attack_rate} attacks/second \nclip:          {self.clip}\nreload:        " \
               f"{self.reload_time}\nweight:          {self.weight}"

    def fire(self):
        # self._mutex.lock() #TODO: learn about mutex
        fire = Turtle()
        fire.speed(FRAME_SPEED)
        fire.penup()
        fire.goto(self.gun_barrel)
        fire.setheading(fire.towards(0, 0))
        self.fire_animation(fire)
        fire.hideturtle()
        print("fire!")
        return fire

    @staticmethod
    def fire_animation(action):  # pass the sound

        action.color("yellow")
        win.update()

        action.hideturtle()
        win.update()

        # win.ontimer(self.shoot, 1000)
        # TODO: add sound import winsound
        # winsound.PlaySound("file.wav", winsound.SND_ASYNC)

    def point_at_target(self):
        closest = self.target_cords()
        self.weapon.setheading(self.weapon.towards(closest))

    def shot(self):
        if all_enemies:
            self.point_at_target()
        if self.in_range and self.clip > 0:
            self.fire()
            self.clip -= 1
            if self.clip == 0:
                self.reload()

    def shoot(self):
        win.ontimer(self.shot, int(1000 / self.attack_rate))

    def reload(self):
        print("reloading!")
        self.clip = self.max_capacity
        win.ontimer(self.fire, self.attack_rate * 1100)

    @staticmethod
    def target_cords():
        return Character.nearest_enemy()[0].pos()

    def in_range(self):
        in_range = False
        distance = Character.nearest_enemy()[1]
        if distance <= self.w_range * 10:
            in_range = True
        return in_range


# ok
class Character:
    level = 1
    speed = 4 + level

    def __init__(self, name, weapons: list):  # weapon_XP
        """

        :param name:
        :param weapons: a list of class Weapon instances.
        """

        self.character = Turtle()

        self.character.shape("turtle")
        self.character.color("darkblue")
        self.character.penup()
        self.character.left(90)
        self.character.speed(FRAME_SPEED)

        self.primary_weapon = None
        self.side_weapon = None

        self.name = name

        # cases of 1 or 2 weapons in form of a list of objects
        self.weapons = weapons
        # TODO: just make one entrance type for this.(list of objects)
        if type(self.weapons) == list and len(weapons) <= 2:
            self.weapon_in_hand = weapons[0]
            self.primary = self.weapon_in_hand
            if len(weapons) == 2:
                self.side_weapon = weapons[1]
        elif type(self.weapons) == list and len(weapons) >= 2:
            print("too many weapons, only too allowed... for now")

        self.weapon_position = (0, 10)

    def __repr__(self):
        stats = f"---{self.name}---\nlevel:         {self.level}\nmove:          {self.speed}\n"
        if type(self.weapons) == list:
            for weapon in self.weapons:
                stats += Weapon.__repr__(weapon)
            return stats

    @staticmethod
    def nearest_enemy():
        distance = 1000
        closest = None
        enemy_xy = None
        for element in all_enemies:
            if element.distance(0, 0) < distance:
                distance = element.distance(0, 0)
                enemy_xy = element.pos()
                closest = element
        return closest, distance, enemy_xy

    def facing(self):
        self.character.setheading(self.character.towards(self.nearest_enemy()[2]))
        self.weapon_in_hand.point_at_target()

    def grab_weapon(self):
        self.weapon_in_hand.goto(10, 0)

    def equip(self, new_weapon):  # define if primary weapon or what?
        if new_weapon not in self.weapons and len(self.weapons) < 2:
            self.weapons.append(new_weapon)

    def unequip(self, old_weapon):
        if old_weapon in self.weapons:
            self.weapons.append(old_weapon)

    def swap_weapon(self):
        pass


# ok
class Enemy:
    max_speed = 15
    level = 1

    # TODO: show the health lost until disapear this model
    def __init__(self):

        self.enemy = Turtle()
        self.enemy.hideturtle()
        self.name = heroes.gen()
        self.enemy.shape("turtle")
        self.enemy.color("red")
        self.enemy.speed(FRAME_SPEED)
        self.enemy.penup()
        self.enemy.starting_pos = self.generate_position()
        self.enemy.goto(self.enemy.starting_pos)
        self.enemy.setheading(self.enemy.towards(0, 0))
        self.enemy.showturtle()

        all_enemies.append(self.enemy)

        self.current_pos = self.enemy.pos()
        self.attack_rate = self.level

        self.move()

    def __repr__(self):
        return f"name:      {self.name}lvl {self.level}\n at {self.current_pos}"

    def move(self):
        self.enemy.setheading(self.enemy.towards(0, 0))
        self.enemy.forward(randint(int(self.max_speed / 2), self.max_speed))
        current_x = self.enemy.xcor()
        current_y = self.enemy.ycor()
        if abs(current_x) - MELEE == 0 and abs(current_y) - MELEE == 0:
            self.attack()
            self.explode()

    @staticmethod
    def generate_position():
        position = choice(OUTLINE)

        if position == OUTLINE[0] or position == OUTLINE[1]:
            return randint(position[0], position[1]), randint(0 - WIDTH / 2, WIDTH / 2)
        else:
            return randint(0 - HEIGHT / 2, HEIGHT / 2), randint(position[0], position[1])

    @staticmethod
    def spawn(n, birth_position):
        # give birth to more enemies
        for _ in range(n):
            new_born = Enemy()
            print(f"birth position {birth_position}")
            # self.goto(birth_position)
            all_enemies.append(new_born)

    def got_hit(self):
        self.enemy.color("yellow")
        win.update()
        self.enemy.color("red")
        win.update()
        self.enemy.color("yellow")
        win.update()
        self.enemy.color("red")
        win.update()
        self.enemy.hideturtle()

    def attack(self):
        print(f"attacking: {self.name}")
        win.ontimer(self.attack, int(1000 / self.attack_rate))

    def shoot(self):
        # reduce the health of closer character
        pass

    def charge(self):
        # sprint forward the character
        if Character.nearest_enemy()[1] >= 50:
            self.max_speed *= 2

    def explode(self):
        # reduce the health of closer character
        print(f"explodes: {self.name}")
        self.enemy.hideturtle()
        # TODO: explosion animation
        # TODO: add sound import winsound
        # winsound.PlaySound("file.wav", winsound.SND_ASYNC)
        all_enemies.remove(self.enemy)


if __name__ == "__main__":

    win = Screen()
    win.bgcolor("green")
    win.tracer(0)

    pistol = Weapon("bolt pistol", 12, 2, 1, 6, 3, 1)
    sgt = Character("Thelonius", [pistol])
    print(sgt)

    processes = []
    enemies = []

    # controls
    def move_left():  # working
        global enemy
        for enemy in all_enemies:
            posx = enemy.pos()[0]
            enemy.goto(posx + sgt.speed, enemy.pos()[1])  # TODO:  instead of sgt.max_speed should be all squad's
            # also move scenery


    def move_right():  # working
        global enemy
        # for enemy in enemies:
        #   enemy.goto(coordenades)
        for enemy in all_enemies:
            posx = enemy.pos()[0]
            enemy.goto(posx - sgt.speed, enemy.pos()[1])  # TODO: instead of sgt.max_speed should be all squad's
            # also move scenery


    def move_up():  # working
        global enemy
        # for enemy in enemies:
        #   enemy.goto(coordenades)
        for enemy in all_enemies:
            posy = enemy.pos()[1]
            enemy.goto(enemy.pos()[0], posy - sgt.speed)  # TODO:  instead of sgt.max_speed should be all squad's
            # also move scenery
        pass


    def move_down():  # working
        global enemy
        # for enemy in enemies:
        #   enemy.goto(coordenades)
        for enemy in all_enemies:
            posy = enemy.pos()[1]
            enemy.goto(enemy.pos()[0], posy + sgt.speed)  # TODO:  instead of sgt.max_speed should be all squad's
            # also move scenery


    win.listen()
    win.onkey(key="a", fun=move_left)
    win.onkey(key="d", fun=move_right)
    win.onkey(key="w", fun=move_up)
    win.onkey(key="s", fun=move_down)

    # create the initial enemies
    for _ in range(5):
        new_enemy = Enemy()
        enemies.append(new_enemy)

    while game_on:
        win.update()
        sleep(0.1)
        sgt.facing()
        # win.ontimer(pistol.shot, int(1000 / pistol.attack_rate))

        for enemy in enemies:
            enemy.move()

    win.exitonclick()

# SQUAD CLASSES AND SUBCLASSES
# class model:
#     STD_MOVE = 1  # standard movement
#     level = 0
#     xp = 0
#
#     def __init__(self, name, weapons=None):  # armor, level
#         """
#
#         :param name: unique name of the character str
#         :param weapons: takes an instance of class Weapon
#         """
#         self.name = name
#
#         self.move = self.STD_MOVE
#         self.weapons = weapons
#
#     def __repr__(self):
#         stats = f"---{self.name}---\nlevel:         {self.level}\nmove:          {self.move}\n"
#         if type(self.weapons) == list:
#             for weapon in self.weapons:
#                 stats += Weapon.__repr__(weapon)
#
#             return stats
#         else:
#             return "not yet"
#
#
# class Ally(Character):
#
#     def __init__(self, name, weapons):
#         super().__init__(name, weapons)
#
#         self.name = self.gen_names
#         self.color = choice(Squad.COLORS)
#         self.weapon = None
#
#     @staticmethod
#     def gen_names():
#         name = None
#         count = len(Squad.active_members)
#         while count < 0:
#             name = heroes.gen()
#             for member in Squad.active_members:
#                 if name != member.name:
#                     count -= 1
#         return name
#
#     # COMPOSITION-STRUCT
#
#
# class Squad:
#     squad_lvl = None
#     COLORS = ["orange", "yellow", "purple", "black", "ligthblue"]
#     active_members = []  # list of character objects
#     bench = []  # list of character objects
#     armory = []
#
#     def __init__(self, members: list):
#         """
#
#         :param members: gotta be list of instances of SquadMember class
#         """
#
#         self.members = members
#         # TODO: instead of squad name variates as squad, team, group, name's group, etc
#         self.name = f"Team {self.members[0].name}"  # the name of the first member of the squad by default
#         self.movement_speed = self.set_squad_speed()
#
#     def __repr__(self):
#         n = 1
#         squad = f"Squad Name:    {self.name}\n"
#
#         for member in self.members:
#             squad += f"{n} "
#             squad += member.__repr__()
#             n += 1
#         return squad
#
#     def set_squad_speed(self):
#         min_speed = 2000
#         for member in self.members:
#             if member.move <= min_speed:
#                 min_speed = member.move
#
#         return min_speed
#
#     def rename_squad(self, new_name):
#         self.name = new_name
#
#     def add_member(self, new_member):
#         self.members.append(new_member)
#
#     def member_death(self, member):
#         if member in self.members:
#             self.members.remove(member)
#
#     def squad_formation(self):
#         pass
#
#     def member_to_bench(self, member):
#         # TODO: create a list of characters that can be swapped in and out the squad
#         pass
#
#     def rotate_formation_left(self):
#         # change the position of the characters
#         pass
#
#
# class SquadMember:
#     level = 1
#     xp = 0
#
#     def __init__(self, name, weapons):
#         super().__init__(name, weapons)
#
#         self.life = 5
#         self.weapons = weapons
#         self.move = self.level * 2
#
#     def check_xp(self):
#         pass
#
#     def set_lvl(self):  # untested
#         """other formulas to study
#         https://onlyagame.typepad.com/only_a_game/2006/08/mathematics_of_.html
#         """
#         if self.xp >= 0.5 * (1.3 ** self.level) + 1:
#             self.level += 1
#         # TODO fix the many levels gaining at once
#
#     def swap_weapon(self, new_weapon, old_weapon):
#         for weapon in self.weapons:
#             if old_weapon in self.weapons and new_weapon != weapon.name:
#                 armoury_list.append(old_weapon)
#                 self.weapons.replace(new_weapon, old_weapon)
#
#     def equip(self):
#         pass
#
#     def swap_armor(self):
#         pass
#
#     def find_gear(self):
#         pass
#
#     @staticmethod
#     def generate_character():
#         print(heroes.gen())
