from models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish1 = Dish('X-Salada', 10.0)
    dish2 = Dish('X-Bacon', 10.0)

    ingredient = Ingredient('queijo mussarela')
    dish1.add_ingredient_dependency(ingredient, 2)
    assert dish1.recipe == {ingredient: 2}

    assert dish1.name == 'X-Salada'
    assert (dish1.__eq__(dish1)) is True
    assert (dish1.__eq__(dish2)) is False

    assert dish1.get_ingredients() == {ingredient}
    assert len(dish1.get_restrictions()) == 2

    assert dish1.__hash__() != dish2.__hash__()
    assert dish1.__hash__() == dish1.__hash__()

    assert dish1.__repr__() == "Dish('X-Salada', R$10.00)"

    with pytest.raises(TypeError):
        Dish('X-Salada', '10.0')

    with pytest.raises(ValueError):
        Dish('X-Salada', -10.0)
