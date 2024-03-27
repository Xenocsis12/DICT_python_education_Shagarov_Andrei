"""arithmetic_test"""
import random

operations = ["+", "-", "*"]


def get_level():

    """
    asks user for level of task
    :return: None if exit
    """
    while True:
        try:
            level = int(input("Enter your level (1 or 2) or 0 to exit:"))
            if level == 1:
                level_1()
            elif level == 2:
                level_2()
            elif level == 0:
                return None
            else:
                print("level should be within range from 1 to 2")
        except ValueError:
            print("Incorrect format")


def get_answer():

    """
    asks user for input of their answer to task
    :return: user_int : int | User's input
    """
    while True:
        try:
            user_int = int(input("answer>"))
            return user_int
        except ValueError:
            print("Incorrect format.")


def check_answer(answer, task):

    """
    Checks if the answer is correct
    :param answer: user's answer to task
    :param task: answer to task
    :return: Right if answer is correct | else Wrong
    """""
    if answer == task:
        return "Right"
    else:
        return "Wrong"


def add_to_file(mark):

    """
    asks user if he wants to write their score in file
    :param mark: user's mark
    :return: None
    """
    while True:
        y_n = input("Would you like to save your result to the file? (yes/no)")
        if y_n[0].lower() == "n":
            return None
        elif y_n[0].lower() == "y":
            name = input("Enter your name >")
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(f"{name}: {mark}/5\n")
                print("The results are saved in 'results.txt'.")
                return None


def level_1():

    """
    generating level 1 task for user 5 times and gives user their mark. Also, aks if mark should be
    written in text file
    :return: None
    """
    mark = 0
    for _ in range(5):
        first_num = random.randint(2, 9)
        second_num = random.randint(2, 9)
        operation = random.choice(operations)
        task = eval(str(first_num) + operation + str(second_num))
        print(first_num, operation, second_num)
        answer = get_answer()
        checked_answer = check_answer(answer, task)
        print(checked_answer)
        if checked_answer == "Right":
            mark += 1
    print(f"Your mark is {mark}/5.")
    add_to_file(mark)


def level_2():

    """
    generating level 2 task for user 5 times and gives user their mark. Also, aks if mark should be
    written in text file
    :return: None
    """
    mark = 0
    for _ in range(5):
        first_num = random.randint(11, 29)
        print(f"what is {first_num} squared?")
        task = first_num ** 2
        answer = get_answer()
        checked_answer = check_answer(answer, task)
        print(checked_answer)
        if checked_answer == "Right":
            mark += 1
    print(f"Your mark is {mark}/5.")
    add_to_file(mark)


get_level()
