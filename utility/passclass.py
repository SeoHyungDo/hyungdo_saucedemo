import pytest

@pytest.mark.usefixtures("setup")
class PassClass :
    driver = None
    wait = None
    global_obj = None
    standard_user = None
    cart = None