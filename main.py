# This is my new coffee maker. It makes coffee for all my favorite people.
# Actually it will make coffee for my not so favorite people also, but they have to pay more

# Make coffee while the sun shines. If life gives you beans, make coffee
from coffee_machine import CoffeeMachine
from menu import Menu

jittery = False


def options():
    # Print the main menu
    print("\n")
    print("1. Make coffee\n")
    print("2. Print report\n")
    print("3. Check resources\n")
    print("4. Power off\n")

    choice = input("What would you like to do? ")
    return int(choice)


my_coffee_machine = CoffeeMachine()

while not jittery:

    option = options()
    while 1 > option > 4:
        option = options()

    if option != 4:
        match option:
            case 1:
                # Make coffee
                my_menu = Menu()
                my_choices = my_menu.get_items()
                choice = input(f"Please choose a drink {my_choices}: ")
                while my_menu.find_drink(choice) is None:
                    choice = input(f"You can only choose one of {my_choices}: ")

                my_joe = my_menu.find_drink(choice)
                if my_coffee_machine.enough_resources(my_joe):
                    my_coffee_machine.cup_a_joe(my_joe)
            case 2:
                # Print report
                pass
            case 2:
                # Check resources
                pass

    else:
        jittery = True
