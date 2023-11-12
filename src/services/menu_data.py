from src.models.dish import Dish
from src.models.ingredient import Ingredient
from collections import defaultdict


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.load_data()

    def load_data(self):
        dishes = defaultdict(lambda: Dish("", 0.0))

        with open(self.source_path, "r") as file:
            for index, line in enumerate(file):
                if index == 0:
                    continue

                split_line = line.strip().split(",")
                dish_name, price_str, ingredient_name, quantity = split_line

                quantity_number = int(quantity)
                price = float(price_str)
                ingredient = Ingredient(ingredient_name)

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, price)

                dishes[dish_name].add_ingredient_dependency(
                    ingredient, quantity_number)

        return dishes.values()
