"""dinner party"""
import random


def start_party():
    """
        Starts the dinner party by creating dictionary with information about the number of guests and their names.
        Returns: None
        """
    guest_dict = dict()
    num_guests = int(input("how many guests will come?: "))
    if num_guests <= 0:
        print("No one is joining the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(num_guests):
            guest = input()
            guest_dict[guest] = 0
        lucky(guest_dict)


def total_amount(guest_dict, lucky=False,lucky_person=None):
    """
    Calculate the total amount of money for each guest to spend.

    Args:
    guest_dict (dict): Dictionary containing guest names as keys and their contribution as values.
    lucky (bool): True if there's a lucky person, False otherwise.
    lucky_person (str): The name of the lucky person who does not pay.

    Returns: None
    """
    sum_for_all = float(input("Enter the total amount: "))
    if lucky == True:
        for i in guest_dict.keys():
            guest_dict[i] = round(sum_for_all/(len(guest_dict)-1),2)
        guest_dict[lucky_person] = 0
    else:
        for i in guest_dict.keys():
            guest_dict[i] = round(sum_for_all/len(guest_dict),2)
    print(guest_dict)

def lucky(guest_dict):
    """
    find out if there's a lucky person in the party and adjust the total amount according to this.

    Args:
    guest_dict (dict): Dictionary containing guest names as keys and their contribution as values.

    Returns: None
    """
    lucky_guest = input("Do you want to try your luck and not pay? (yes/no): ")
    if lucky_guest == "yes":
        lucky_person = random.choice(list(guest_dict.keys()))
        print(f"{lucky_person} is the lucky person")
        total_amount(guest_dict, True,lucky_person)
    else:
        print("no one is going to be lucky")
        total_amount(guest_dict)


start_party()