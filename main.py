# This is my new coffee maker. It makes coffee for all my favorite people.
# Actually it will make coffee for my not so favorite people also, but they have to pay more

from menu import Menu

# Make coffee while the sun shines. If life gives you beans, make coffee
jittery = False

while not jittery:

    my_menu = Menu()
    option = my_menu.options()
    while 1 > option > 4:
        option = my_menu.options()

    if option != 4:
        my_choices = my_menu.get_items()
        choice = input(f"Please choose a drink {my_choices}: ")
        while not my_menu.find_drink(choice):
            choice = input(f"You can only choose one of {my_choices}: ")

        print(f"You have chosen {choice}")
    else:
        jittery = True