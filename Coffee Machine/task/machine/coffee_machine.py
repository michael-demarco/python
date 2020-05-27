# Write your code here
class CoffeeMachine:

    def __init__(self):
        self.money_in_machine = 550
        self.water_in_machine = 400
        self.milk_in_machine = 540
        self.beans_in_machine = 120
        self.cups_in_machine = 9
###
#    def __init__(self, money_in_machine, water_in_machine, milk_in_machine, beans_in_machine, cups_in_machine):
#        self.money_in_machine = money_in_machine
#        self.water_in_machine = water_in_machine
#        self.milk_in_machine = milk_in_machine
#        self.beans_in_machine = beans_in_machine
#        self.cups_in_machine = cups_in_machine
###

    def make_one_espresso(self):
        while True:
            if self.water_in_machine < 250:
                print("Sorry, not enough water!")
                break
            elif self.beans_in_machine < 16:
                print("Sorry, not enough beans!")
                break
            elif self.cups_in_machine < 1:
                print("Sorry, not enough cups!")
                break
            else:
                self.water_in_machine -= 250
                self.beans_in_machine -= 16
                self.money_in_machine += 4
                self.cups_in_machine -= 1
                print("I have enough resources, making you a coffee!")
                break

    def make_one_latte(self):
        while True:
            if self.water_in_machine < 350:
                print("Sorry, not enough water!")
                break
            elif self.milk_in_machine < 75:
                print("Sorry, not enough milk!")
                break
            elif self.beans_in_machine < 20:
                print("Sorry, not enough beans!")
                break
            elif self.cups_in_machine < 1:
                print("Sorry, not enough cups!")
                break
            else:
                self.water_in_machine -= 350
                self.milk_in_machine -= 75
                self.beans_in_machine -= 20
                self.money_in_machine += 7
                self.cups_in_machine -= 1
                print("I have enough resources, making you a coffee!")
                break

    def make_one_cappuccino(self):
        while True:
            if self.water_in_machine < 200:
                print("Sorry, not enough water!")
                break
            elif self.milk_in_machine < 100:
                print("Sorry, not enough milk!")
                break
            elif self.beans_in_machine < 12:
                print("Sorry, not enough beans!")
                break
            elif self.cups_in_machine < 1:
                print("Sorry, not enough cups!")
                break
            else:
                self.water_in_machine -= 200
                self.milk_in_machine -= 100
                self.beans_in_machine -= 12
                self.money_in_machine += 6
                self.cups_in_machine -= 1
                print("I have enough resources, making you a coffee!")
                break

    def fill_machine(self):
        filling_water = abs(int(input("Write how many ml of water do you want to add: ")))
        filling_milk = abs(int(input("Write how many ml of milk do you want to add: ")))
        filling_coffee = abs(int(input("Write how many grams of coffee beans do you want to add: ")))
        filling_cups = abs(int(input("Write how many disposable cups of coffee do you want to add: ")))

        self.water_in_machine += filling_water
        self.milk_in_machine += filling_milk
        self.beans_in_machine += filling_coffee
        self.cups_in_machine += filling_cups

    def buy_from_machine(self):
        while True:
            buy_option = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "
                                   "back - to main menu: "))
            if buy_option == "1":
                self.make_one_espresso()
                break
            elif buy_option == "2":
                self.make_one_latte()
                break
            elif buy_option == "3":
                self.make_one_cappuccino()
                break
            elif buy_option == "back":
                break
            else:
                print("Incorrect input\n\n")

    def withdrawl_from_register(self):
        print("I gave you $" + str(self.money_in_machine))
        self.money_in_machine = 0

    def coffee_machine_status(self):
        print("The coffee machine has:")
        print(str(self.water_in_machine) + " of water")
        print(str(self.milk_in_machine) + " of milk")
        print(str(self.beans_in_machine) + " of coffee beans")
        print(str(self.cups_in_machine) + " of disposable cups")
        print(str(self.money_in_machine) + " of money\n\n")


def main():
    coffee_machine = CoffeeMachine()

    while True:
        machine_action = str(input("Write action (buy, fill, take, remaining, exit): "))
        if machine_action == "buy":
            CoffeeMachine.buy_from_machine(coffee_machine)
        elif machine_action == "fill":
            CoffeeMachine.fill_machine(coffee_machine)
        elif machine_action == "take":
            CoffeeMachine.withdrawl_from_register(coffee_machine)
        elif machine_action == "remaining":
            CoffeeMachine.coffee_machine_status(coffee_machine)
        elif machine_action == "exit":
            break
        else:
            print("\n\nplease choose from one of the actions provided (buy, fill, take, remaining, exit)\n\n")

main()
