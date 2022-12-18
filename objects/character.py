from names_generator import generator
from objects.weapon import *
from objects.enemy import all_enemies
from turtle import Turtle


def generate_random_weapon():
    import random
    return random.choice(armoury_list)


class Character:
    level = 1
    max_speed = 10
    xp = 0

    def __init__(self, name=None, weapons_list: list = None):  # weapon_XP

        self.character = Turtle()

        self.character.shape = "turtle"
        self.character.color = "darkblue"
        self.character.speed = "fastest"
        self.character.penup()
        self.character.left(90)

        if weapons_list:
            self.weapons = weapons_list
        else:
            self.weapons = [generate_random_weapon()]

        if not name:
            self.name = input("Enter your name: ")
        else:
            self.name = name

        if type(self.weapons) == list:
            self.weapon_in_hand = self.weapons[0]

    def __repr__(self):
        stats = f"---{self.name}---\nlevel:         {self.level}\nmove:          {self.max_speed}\n"

        for weapon in self.weapons:
            weapon_stat = weapon.__repr__()
            stats += weapon_stat

        return stats

    # @staticmethod
    # def nearest_enemy():
    #     distance = 1000
    #
    #     if all_enemies:
    #         print(all_enemies)
    #         closest = None
    #         enemy_xy = None
    #         for element in all_enemies:
    #             if element.distance(0, 0) < distance:
    #                 distance = element.distance(0, 0)
    #                 enemy_xy = element.current_pos()
    #                 closest = element
    #         return closest, distance, enemy_xy
    #     else:
    #         return None, distance, None
    #
    # def facing(self):
    #     if not self.nearest_enemy():
    #         pass
    #     else:
    #         self.character.setheading(self.character.towards(self.nearest_enemy()[2]))
    #         self.weapon_in_hand.point_at_target()

    def equip(self, new_weapon):  # define if primary weapon or what?
        if new_weapon not in self.weapons and len(self.weapons) < 2:
            self.weapons.append(new_weapon)

    def unequip(self, old_weapon):
        if old_weapon in self.weapons:
            self.weapons.append(old_weapon)

    def swap_weapon(self):
        pass

    # def carry_weight(self):
    #     for item in equipment


thelonius = Character("Thelonius", weapons_list=[armoury_list[0]])

# if __name__ == "__main__":
#     # victor = Character("Victor")
#     # print(victor.weapons)
#
#     namey = generator.generate(print_on=True, name_type="normal")
#
#     character_1 = Character(namey)
#
#     print(character_1)
