import allure


def test_passing():
    with allure.step("Assert 123 versus 123"):
        assert (1, 2, 3) == (1, 2, 3)


def test_almost_same_assertion():
    with allure.step("Assert tra-tata vs. tra-tata"):
        assert "tra-tata" == "tra-tata"
