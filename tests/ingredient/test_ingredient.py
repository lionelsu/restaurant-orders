from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")

    assert (ingredient2.__eq__(ingredient1)) is False
    assert (ingredient2.__eq__(ingredient2)) is True

    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1.__hash__() == ingredient1.__hash__()

    assert ingredient1.__repr__() == "Ingredient('queijo mussarela')"

    assert ingredient1.name == "queijo mussarela"

    assert len(ingredient1.restrictions) == 2
