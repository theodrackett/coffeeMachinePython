# Spin up a coffee machine

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "coffee": 100,
            "milk": 200
        }

    def print_report(self):
        # print a report of all remaining ingredients
        print(f"Water {self.resources['water']}ltr")
        print(f"Coffee {self.resources['coffee']}ltr")
        print(f"Milk {self.resources['milk']}lbs")

    def enough_resources(self, drink):
        # Check if there are enough ingredients to make the drink
        enough = True
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry not enough {ingredient}")
                enough = False

        return enough

    def cup_a_joe(self, joe):
        for ingredient in joe.ingredients:
            self.resources[ingredient] -= joe.ingredients[ingredient]

            print(f"Here is your {joe.name}. Have a wonderful day!")
