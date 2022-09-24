# This is my new coffee maker. It makes coffee for all my favorite people.
# Actually it will make coffee for my not so favorite people also, but they have to pay more

from menu import Menu

# Make coffee while the sun shines. If life gives you beans, make coffee
jittery = False

while not jittery:
    my_menu = Menu()
    my_choices = my_menu.get_items()
    choice = input(f"Please choose a drink {my_choices}: ")
    while choice not in my_choices:
        choice = input(f"You can only choose one of {my_choices}: ")

    print(f"You have chosen {choice}")

    jittery = True