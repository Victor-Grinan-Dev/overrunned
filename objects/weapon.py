from turtle import Turtle


class Weapon(Turtle):

    def __init__(self, weapon_name, weapon_range, damage, attack_per_second, clip, reload, weight, area_damage=False):
        super().__init__()

        # self.weapon = Turtle()
        self.shape = "square"
        self.shapesize = (0.5, 0.1, 1)  # pistol size
        self.penup()
        self.color = "black"
        self.speed = "fastest"

        self.weapon_name = weapon_name
        self.w_range = weapon_range
        self.damage = damage
        self.weight = weight
        self.attack_per_second = attack_per_second
        self.max_capacity = clip
        self.area_damage = area_damage  # explosives = 1 or 2 x 24(a turtle size) around the original target
        # flamers = fix pixels from the weapon: #######
        ###
        self.clip = self.max_capacity  #
        self.reload_time = reload  #

        self.gun_barrel = (0, 10)  # TODO: get the position of the weapon barrel
        self.attack_rate = int(1 / self.attack_per_second)

        self.__repr__()

    def __repr__(self):
        return f"weapon_name:   {self.weapon_name}\nrange:         {self.w_range}\ndamage:        {self.damage}\n" \
               f"attack rate:   {self.attack_rate} attacks/second \nclip:          {self.clip}\nreload:        " \
               f"{self.reload_time} "

    # def fire(self):
    #     # self._mutex.lock() #TODO: learn about mutex
    #     fire = Turtle()
    #     fire.speed("fastest")
    #     fire.penup()
    #     fire.goto(self.gun_barrel)
    #     fire.setheading(fire.towards(0, 0))
    #     self.fire_animation(fire)
    #     fire.hideturtle()
    #     print("fire!")
    #     return fire

    # @staticmethod
    # def fire_animation(action):  # pass the sound
    #
    #     action.color("yellow")
    #     action.hideturtle()
    #     # win.ontimer(self.shoot, 1000)
    #     # TODO: play sound!!!

    # def point_at_target(self):
    #     closest = self.target_cords()
    #     self.weapon.setheading(self.weapon.towards(closest))

    # TODO: Thread/multiprocess this
    # def shot(self):
    #     self.point_at_target()
    #     if self.in_range and self.clip > 0:
    #         self.fire()
    #         self.clip -= 1
    #         if self.clip == 0:
    #             self.reload()
    #     sleep(1000 / self.attack_rate)

    # TODO: Thread/multiprocess this
    # def reload(self):
    #     print("reloading!")
    #     self.clip = self.max_capacity

    # @staticmethod
    # def target_cords():
    #     return Character.nearest_enemy()[0].pos()
    #
    # def in_range(self):
    #     in_range = False
    #     distance = Character.nearest_enemy()[1]
    #     if distance <= self.w_range * 10:
    #         in_range = True
    #     return in_range


pistol = Weapon("pistol", 12, 2, 1, 8, 3, 1)  # 34pts + 1
submachinegun = Weapon("submachinegun", 18, 1, 3, 30, 3, 2)  # 53pts + 2
auto_assault_rifle = Weapon("auto_assault_rifle", 24, 1, 2, 30, 3, 3)  # 61 + 3
sniper_rifle = Weapon("sniper rifle", 48, 4, 0.5, 5, 2, 2)  # 60.5 + 2
fragmentation_missile_launcher = Weapon("missile launcher (frag)", 48, 1, 1, 1, 4, 3)  # 56 + 3
penetration_missile_launcher = Weapon("missile launcher (solid)", 48, 8, 1, 1, 4, 3)  # 56 + 3
ak_47 = Weapon("ak-47", 24, 2, 2, 30, 3, 3)
uzi = Weapon("uzi", 16, 1, 4, 35, 3, 2)
magnun = Weapon("magnun", 18, 3, 0.75, 6, 3, 1)
# flame_trhower= Weapon("flame_trhower", 6, 1, 0.5, )

armoury_list = [pistol, submachinegun, auto_assault_rifle, ak_47, sniper_rifle, fragmentation_missile_launcher,
               penetration_missile_launcher, uzi, magnun]


# class Ammo:
#
#     def __init__(self, size, head, weapon_fit, range_modifier=0, damage_modifier=0, area_impact=False,
#                  percent_chance_to_jam=1):
#         self.name = f"{size}mm {head}"
#         self.range_mod = range_modifier
#         self.damage_mod = damage_modifier
#         self.area_impact = area_impact
#         self.jams = percent_chance_to_jam
#
#         self.image = None
#         self.speed_mod = 0
#
#
# small_ammo = ["9mm", "10mm", ".22LR", ".38", ".45"]
# mid_ammo = ["5.7x28mm", ".357", ".30", ".300", "5.56x45mm"]
# big_ammo = [".308", "7.62x54mm", ".30-06"]
# mega_ammo = [".50"]
# shells = [".410", "28ga", "20ga", "16ga", "12ga", "10ga", "8ga", "4ga"]
# ammo_types = [small_ammo, mid_ammo, big_ammo, mega_ammo, shells]

if __name__ == '__main__':
    pistol = Weapon("Pistol", 12, 2, 1, 6, 3, 1)  # 34pts + 1
    print(pistol)
