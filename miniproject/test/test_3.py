import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings
from IcecreamExceptions import OutOfStockException


@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
#    UCID-ab2634  DATE- 10/23/2022


def test_ToppingInStock(machine):
    try:
        machine.toppings[0].quantity=2
        machine.handle_container("cup")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("next")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("done")
        #return machine
        assert False
    except OutOfStockException:
        assert  True

#Test 3