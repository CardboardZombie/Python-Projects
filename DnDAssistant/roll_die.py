import random

D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20
D100 = 100


def roll_dice(times, dice_type):
    for _ in range(times):
        roll = random.randint(1, dice_type)
        print(roll)


def get_gold(times, dice_type):
    roll = 0
    for _ in range(times):
        roll += random.randint(1, dice_type)
    print(f"{roll * 10} gold pieces")


if __name__ == "__main__":
    get_gold(times=4, dice_type=D6)
