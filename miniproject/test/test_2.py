import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings


@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
#    UCID-ab2634  DATE- 10/23/2022
@pytest.fixture
def first_order(machine):
    machine.flavors[0].quantity=2
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    return machine

def test_FlavoursInStock(first_order):
    return first_order is not None

#Test 2