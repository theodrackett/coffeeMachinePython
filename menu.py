from menu_item import MenuItem


class Menu:
    # This is the full menu

    def __init__(self):
        self.menu = [MenuItem(name="espresso", cost=2.5, water=200, milk=150, coffee=24),
                     MenuItem(name="latte", cost=1.5, water=50, milk=0, coffee=18),
                     MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24)]

    def get_items(self):
        choices = ""
        for drink in self.menu:
            choices += f"/{drink.name}"

        return choices
