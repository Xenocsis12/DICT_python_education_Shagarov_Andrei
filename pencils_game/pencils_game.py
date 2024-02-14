""" PENCILS GAME"""

import random


def print_pencils(number_of_pencils):

    """
    prints pencils
    :param number_of_pencils: (int)  receive number of pencils in the game
    :return: none
    """
    print("|" * number_of_pencils)


def validate_input(num_of_pencils: int, take: int):

    """
    verifies that input is valid
    :param num_of_pencils: (int) number of pencils in the game
    :param take :(int) number of pencils user wants to take
    :return: Bool | True if input is valid
    """
    if num_of_pencils < take:
        print("you can't take more than there is")
        return False
    if take <= 0:
        print("you can't take zero or less pencils")
        return False
    if take > 3:
        print("You can only take up to 3 pencils")
        return False
    else:
        return True


def choose_the_name():

    """
    suggest player to choose his name between alex or artem
    :return: String | name that player chose between
    """
    names = []
    while True:
        try:
            the_first = input("Who will be the first (Artem, Alex)").capitalize()
            if the_first not in ("Alex", "Artem"):
                raise ValueError()
            else:
                print(f"So, {the_first} is first")
                names.append(the_first)
                if the_first == "Alex":
                    the_second = "Artem"
                    names.append(the_second)
                    return names
                else:
                    the_second = "Alex"
                    names.append(the_second)
                    return names
        except ValueError:
            print("You must chose between these 2 names: ")


def move(number_of_pencils: int):

    """
    player's move. In other words allows player to take pencils
    :param number_of_pencils: (int)  number of pencils
    :return: int | updated number of pencils
    """
    while True:
        try:
            take = int(input("How many pencils do you want to take?: "))
            if validate_input(number_of_pencils, take):
                number_of_pencils -= take
                return number_of_pencils
        except ValueError:
            print("The number of pencils should be numeric;")


def bot_move(pencils: int, name_of_bot: str):

    """
    function that allows bot to make moves
    :param pencils: (int) number of all pencils
    :param name_of_bot: string | name of the bot
    :return: int | updated number of pencils
    """
    if pencils == 1:
        take = 1
        pencils -= take
        print(f"{name_of_bot} takes {take} pencils")
        return pencils
    elif pencils % 4 == 1:
        take = random.randint(1, 3)
        pencils -= take
        print(f"{name_of_bot} takes {take} pencils")
        return pencils
    else:
        take = (pencils - 1) % 4
        pencils -= take
        print(f"{name_of_bot} takes {take} pencils")
        return pencils


while True:
    try:
        pencils_num = int(input("How many pencils are there?: "))
        if pencils_num <= 0:
            print("Number of pencils must be greater than 0")
            continue
        break

    except ValueError:
        print("Enter number, please")
        continue
while True:
    try:
        bot = input("do you want to play with bot?(y/n)")
        if bot == "n" or bot == 'y':
            break
        else:
            raise ValueError()
    except ValueError:
        print("You must type 'y' for yes or 'n' for no")

if bot == 'n':
    name = choose_the_name()

    while pencils_num > 0:
        print(f"{name[0]}'`s move")
        print_pencils(pencils_num)
        pencils_num = move(pencils_num)
        if pencils_num <= 0:
            print(f"{name[1]} won")
            break
        print(f"{name[1]}'`s move")
        print_pencils(pencils_num)
        pencils_num = move(pencils_num)
        if pencils_num <= 0:
            print(f"{name[0]} won")
else:
    bots_random_name = [
        "Jonh The Little", "Andrei The Great", "Rem, cutie monstr", "Rei, the old love",
        "Lux, guardian of the abyss"
    ]
    name = input("You can have your own name, hero! ")
    bot_name = bots_random_name[random.randint(0, len(bots_random_name)-1)]
    while pencils_num > 0:
        print(f"{name}'`s move")
        print_pencils(pencils_num)
        pencils_num = move(pencils_num)
        if pencils_num <= 0:
            print(f"{bot_name} won")
            break
        print(f"{bot_name}'`s move")
        print_pencils(pencils_num)
        pencils_num = bot_move(pencils_num, bot_name)
        if pencils_num <= 0:
            print(f"{name} won")
