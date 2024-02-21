""" COFFEE MACHINE """


class CoffeeMachine:

    def __init__(self):

        """
        initiate ingredients for coffee machine
        """
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.money = 550
        self.cups = 9
        self.list = {"water": self.water, "milk": self.milk, "beans": self.beans}

    def ingredients_left(self):

        """
        prints all ingredients left
        :return: None
        """
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


    def cups_possible_to_make(self, price):

        """
        checks if machine can make a coffee
        :param price: dict ingredients needed for coffee
        :return:
        """
        if price["milk"] == 0:
            return min(self.water // price["water"], self.milk // 1, self.beans // price["beans"])
        else:
            return min(self.water // price["water"], self.milk // price["milk"], self.beans // price["beans"])

    def ingredients_need(self, price, num_of_cups=1):

        """
        calculate how many ingredients you need for cups of coffee
        :param price: dict ingredients needed for coffee
        :param num_of_cups: number of cups
        :return:  None
        """
        print(f"For {num_of_cups} cups of coffee I will need:")
        print(f"{price['water'] * num_of_cups} ml of water")
        print(f"{price['milk'] * num_of_cups} ml of milk")
        print(f"{price['beans'] * num_of_cups} g of coffee beans")
        self.coffee_is_made(price)

    def possible_to_make(self, price, num_of_cups=1):


        """
        Check how mony cups of coffee can machine make
        :param price:
        :param num_of_cups: Number of cups that needed to bo done
        :return: None of False if can't do coffeee
        """
        if self.cups_possible_to_make(price) == num_of_cups:
            print(f"Yes, I can make that amount of coffee")
            self.ingredients_need(price)
        elif self.cups_possible_to_make(price) > num_of_cups:
            print(f"Yes, I can make that amount of coffee(and even {self.cups_possible_to_make(price) - num_of_cups} more)")
            self.ingredients_need(price)
        else:
            print(f"No, I can make only {self.cups_possible_to_make(price)} cups of coffee")
            print("Please, contact someone to refill me!")
            return False


    def action(self):

        """
        method that allows user to select action
        :return: None
        """
        act = input("Write action (buy, fill, take, remaining, exit):")
        try:
            if act[0] in ("b", "f", "t", "r", "e"):
                if act[0] == "b":
                    self.buy()
                elif act[0] == "f":
                    self.fill()
                elif act[0] == "t":
                    self.take()
                elif act[0] == "r":
                    self.ingredients_left()
                elif act[0] == "e":
                    exit()
            else:
                print("sorry, I don't know what to do")
        except ValueError:
            print("You press something wrong")

    def buy(self):
        """
        method that allows user to buy coffee
        :return: None
        """
        type_of_coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
        self.coffee_cost(type_of_coffee)

    def fill(self):

        """
        Method that restores components of coffee
        :return: None
        """
        self.water += int(input("How many ml of water you want to add: "))
        self.milk += int(input("How many ml of milk you want to add: "))
        self.beans += int(input("How many grams of coffee you want to add: "))
        self.cups += int(input("How many cups you want to add: "))
        self.ingredients_left()

    def take(self):

        """
        gives all money to user
        :return: None
        """
        print(f"Giving you all ${self.money} I have")
        self.money = 0

    def coffee_cost(self, type_of_coffee):

        """
        contains dict with ingredients needed for coffee
        :param type_of_coffee: int Select type of coffee
        :return: None
        """
        match type_of_coffee:
            case 1:
                d = {"water": 250, "milk": 0, "beans": 16, "money": 4}
                self.possible_to_make(d)
            case 2:
                d = {"water": 350, "milk": 75, "beans": 20, "money": 7}
                self.possible_to_make(d)
            case 3:
                d = {"water": 200, "milk": 100, "beans": 12, "money": 6}
                self.possible_to_make(d)

    def coffee_is_made(self, price):

        """
        printing that coffee is made, also decrease ingredients in the machine
        :param price: dict with ingredients need for coffee
        :return: None
        """
        self.water -= price["water"]
        self.milk -= price["milk"]
        self.beans -= price["beans"]
        self.money += price["money"]
        self.cups -= 1
        print("Starting to make a coffee")
        print("Grinding coffee beans")
        print("Boiling water")
        print("Mixing boiled water with crushed coffee beans")
        print("Pouring coffee into the cup")
        print("Pouring some milk into the cup")
        print("Coffee is ready!")




