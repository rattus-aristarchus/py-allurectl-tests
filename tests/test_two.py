import allure


def test_failing():
    with allure.step("Assert tuple 1,2,3 versus tuple 1,2,3"):
        assert (1, 2, 3) == (1, 2, 3)


def test_failing_strings():
    with allure.step("Assert string 'tra-tata' versus string 'trata-ta'"):
        assert "tra-tata" == "trata-ta"\


def test_failing_strings():
    with allure.step("Assert 1 is in the list [1,2,3]"):
        assert 1 in [1,2,3]