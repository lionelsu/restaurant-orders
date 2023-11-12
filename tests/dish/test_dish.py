from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish1 = Dish('X-Salada', 10.0)

    assert dish1.name == 'X-Salada'
    assert dish1.price == 10.0
