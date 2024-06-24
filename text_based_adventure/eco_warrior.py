# ================================
# CA3 - Data Structures for Games
# Author: Tadhg Deeney
# GamesDev Year 2
# MainApp.py
# ================================

from collections import deque
import random
import time


# Placeholder classes for Player, Room, Item, Weapon, and Creature
class Player:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.money = 0
        self.weapon = None
        self.xp = 0
        self.acc = 0

    def load_point(self):
        # Load player data from a file or other source
        return self

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def turn_on_gameboy(self):
        pass

    def flip_switch(self, app):
        pass

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon

    def take_damage(self, damage):
        pass

    def is_dead(self):
        return False

    def set_cash(self, amount):
        self.money += amount

    def set_xp(self, xp):
        self.xp += xp

    def lvl_up(self):
        pass

    def end_game(self):
        pass


class Room:
    def __init__(self):
        self.name = ""
        self.item = ""
        self.weapon = ""
        self.app = ""
        self.key_obj = ""
        self.exit_list = []

    def load(self, file):
        # Load room data from file
        return self

    def get_name(self):
        return self.name

    def get_item(self):
        return self.item

    def get_weapon(self):
        return self.weapon

    def get_app(self):
        return self.app

    def get_key_obj(self):
        return self.key_obj

    def exit_list(self):
        return self.exit_list

    def set_item(self, item):
        self.item = item

    def set_weapon(self, weapon):
        self.weapon = weapon

    def print(self):
        pass


class Item:
    def __init__(self):
        self.name = ""

    def load(self, file):
        # Load item data from file
        return self

    def print(self):
        pass


class Weapon:
    def __init__(self):
        self.name = ""
        self.damage_range = (0, 0)

    def load(self, file):
        # Load weapon data from file
        return self

    def print(self):
        pass


class Creature:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.xp_reward = 0

    def load(self, file):
        # Load creature data from file
        return self

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_xp_reward(self):
        return self.xp_reward

    def take_damage(self, damage):
        pass

    def is_dead(self):
        return False

    def attack(self, player):
        pass


def print_time(text):
    print(text)
    time.sleep(1)


# Global variables
txt_spacer = "=" * 80
the_plyr = Player()
the_room = Room()
rooms = []
apps = []
items = []
weapons = []
game_app = None
the_item = None
the_enemy = None
game_weapon = None


def set_up():
    """
    The set_up() function details the backstory and how to play using the commands given
    to help the player navigate through the game.
    """
    print("\033[H\033[J")
    print_time("\n\n\t\t\t\tSTORYLINE: INTRO")
    print(txt_spacer)
    print(f"Welcome To Eco Warrior!! This game invites you, {the_plyr.get_name()}, to learn about")
    print("Saving Energy in your own home (While taking on some mean baddies too!)\n\n")
    print_time("You hear a noise from outside your Room...")
    print_time("It sounds like your home has been infested by Energy Pests:")
    print("\nVampires suck away all the Energy in the room feeding and growing.\n")
    print("Ghosts have been known to appear when an infestation occurs to spook people.")
    print("The Energy Trolls don't really gain from the Energy they steal,")
    print("but they love watching you squirm knowing that they are costing you")
    print("tonnes of Money!!")
    print_time("Take them out.")
    print("\nYour Mission is to stop all creatures from wasting Energy in your home.")
    print(
        "Accomplish this by turning off an Electronic Appliance in each Room in the House and defeating each creature in Combat.")
    print_time("Are you ready? You better be...Gather your wits and become the last hope to Save Energy in your Home!")
    input("Press Enter to continue...")
    print("\033[H\033[J")
    print_time("\n\n\t\t\t\tHOW TO PLAY!!!")
    print(txt_spacer)
    print_time("Explore all the Rooms and be sure to Turn off as many Appliances as you can.")
    print_time("Take Items that will help you defeat Enemies you may Encounter.")
    print_time("Commands:\n")
    print_time("\"Show Commands\"\n\"Check Gameboy/Room/Pack/Weapons\"\n\"Quit Game\"\n\"Kill [Name of Appliance]\"")
    print_time("\"Take [Name of Object]\"\n\"Enter [Name of Room]\"\n\"Take [Name of Weapon]\"\n\"Switch Weapons\"")
    print(txt_spacer)
    input("Press Enter to continue...")


def load_game():
    """
    The load_game function loads in the player or creates a new player and sets it to the main player.
    It also loads in a number of other objects from their txt files.
    """
    global the_plyr, the_room, the_enemy

    e_stack = deque()

    # Load in the Player
    while the_plyr.get_name() == "":
        the_plyr = the_plyr.load_point()

    # Load in the Rooms
    with open("Room.txt") as in_room_file:
        num_of_rooms = int(in_room_file.readline().strip())
        for _ in range(num_of_rooms):
            room = Room().load(in_room_file)
            rooms.append(room)

    pos = the_plyr.get_position()
    for room in rooms:
        if pos == room.get_name():
            the_room = room
            break

    # Load in the Items
    with open("Item.txt") as item_file:
        num_of_items = int(item_file.readline().strip())
        for _ in range(num_of_items):
            item = Item().load(item_file)
            items.append(item)

    # Load Apps
    with open("App.txt") as in_app_file:
        num_of_apps = int(in_app_file.readline().strip())
        for _ in range(num_of_apps):
            app = App().load(in_app_file)
            apps.append(app)

    # Load in Weapons
    with open("Weapon.txt") as weapon_file:
        num_of_weapons = int(weapon_file.readline().strip())
        for _ in range(num_of_weapons):
            weapon = Weapon().load(weapon_file)
            weapons.append(weapon)

    # Load Enemies
    with open("Creature.txt") as in_file:
        num_of_enemies = int(in_file.readline().strip())
        for _ in range(num_of_enemies):
            enemy = Creature().load(in_file)
            e_stack.append(enemy)

    if the_plyr.money == 0:  # If the player is new display the set up
        set_up()

    play_game(e_stack)


def play_game(e_stack):
    """
    Main game loop where the player can enter rooms, take items, check stats, and fight enemies.
    """
    plyr_pack = []
    weapon_pack = deque()
    command_list = ["Enter", "Take", "Check", "Kill", "Switch", "Show"]
    game_ovr = False

    print(f"Good Luck with your quest, Eco-Warrior {the_plyr.get_name()}.\nTo find out more \"Check Room\"")

    while not game_ovr:
        input_str = input("\n\nWhat's Next?\n>").strip().split(' ', 1)
        command = input_str[0]
        input_arg = input_str[1] if len(input_str) > 1 else ""

        if command == "Enter":
            enter_room(input_arg, plyr_pack)
        elif command == "Take":
            if " " + input_arg == the_room.get_item():
                for item in items:
                    if " " + input_arg == item.name:
                        plyr_pack.append(item)
                        print_time("It was added to your pack!")
                        the_room.set_item("Already Taken")
                        break
            elif " " + input_arg == the_room.get_weapon():
                print(f"{the_plyr.get_name()} Lifted the{the_room.get_weapon()}")
                for weapon in weapons:
                    if " " + input_arg == weapon.name:
                        if len(e_stack) > 0:
                            game_ovr = fight(weapon_pack, e_stack)
                        weapon_pack.append(weapon)
                        print_time(f"The {weapon.name} was added to the Weapons!")
                        the_room.set_weapon("Already Taken")
                        if len(e_stack) > 0:
                            game_ovr = fight(weapon_pack, e_stack)
                        break
            else:
                print("Invalid Command!!")
        elif command == "Check":
            if input_arg == "Gameboy":
                the_plyr.turn_on_gameboy()
            elif input_arg == "Room":
                the_room.print()
            elif input_arg == "Pack":
                for item in plyr_pack:
                    item.print()
            elif input_arg == "Weapons":
                for weapon in weapon_pack:
                    weapon.print()
            else:
                print("Invalid Command!!")
        elif command == "Kill":
            if " " + input_arg == the_room.get_app():
                print(f"\n{the_plyr.get_name()} Killed the{the_room.get_app()}")
                the_plyr.flip_switch(the_room.get_app())
            else:
                print("Invalid Command!!")
        elif command == "Switch":
            the_weapon = weapon_pack.popleft()
            weapon_pack.append(the_plyr.get_weapon())
            the_plyr.set_weapon(the_weapon)
        elif command == "Show":
            print(command_list)
        elif command == "Quit":
            the_plyr.end_game()
            print("Thanks for playing!!")
            break
        else:
            print("Invalid Command!!")

        if the_plyr.is_dead():
            game_ovr = True
            print_time("\nGAME OVER: You're Dead!\nBetter Luck Next Time...")
            the_plyr.end_game()


def enter_room(input_str, plyr_pack):
    global game_app
    for room in rooms:
        if input_str == room.get_name():
            the_plyr.set_position(input_str)
            the_room = room
            the_room.print()
            if room.get_key_obj() == " Items ":
                room.set_item(drop_item(plyr_pack))
            if room.get_key_obj() == " Weapons ":
                room.set_weapon(drop_weapon(plyr_pack))
            if room.get_key_obj() == " App ":
                game_app = the_room.get_app()
            break


def drop_item(plyr_pack):
    if plyr_pack:
        r = random.randint(0, len(plyr_pack) - 1)
        dropped_item = plyr_pack.pop(r)
        return f" {dropped_item.name}"
    return "No Items"


def drop_weapon(plyr_pack):
    if plyr_pack:
        r = random.randint(0, len(plyr_pack) - 1)
        dropped_weapon = plyr_pack.pop(r)
        return f" {dropped_weapon.name}"
    return "No Items"


def fight(weapon_pack, e_stack):
    """
    Handles the combat between the player and the enemy.
    """
    global the_enemy
    the_enemy = e_stack.pop()
    print_time(f"{the_enemy.get_type()} {the_enemy.get_name()} wants to Fight!!")
    while not the_enemy.is_dead() and not the_plyr.is_dead():
        print_time(f"\nYou attack with your{the_plyr.get_weapon().name}")
        if not the_enemy.is_dead():
            the_enemy.attack(the_plyr)
    if the_enemy.is_dead():
        print_time(f"You killed {the_enemy.get_name()} and earn £20!!")
        the_plyr.set_cash(20)
        the_plyr.set_xp(the_enemy.get_xp_reward())
        the_plyr.lvl_up()
        return False
    return True


if __name__ == "__main__":
    load_game()
