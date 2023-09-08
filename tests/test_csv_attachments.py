import json
import os

import allure
from allure import attachment_type

def test_attach_big_table():
    with allure.step("CSV attach"):
        allure.attach.file(os.path.join("resources", "big-table.csv"), name="9Mb csv example", attachment_type=attachment_type.CSV)

def test_attach_medium_table():
    with allure.step("CSV attach"):
        allure.attach.file(os.path.join("resources", "medium-table.csv"), name="3Mb csv example", attachment_type=attachment_type.CSV)

def test_attach_normal_table():
    with allure.step("CSV attach"):
        allure.attach.file(os.path.join("resources", "normal-table.csv"), name="200 kbytes csv example", attachment_type=attachment_type.CSV)

def test_attach_small_table():
    with allure.step("CSV attach"):
        allure.attach.file(os.path.join("resources", "small-table.csv"), name="10 kbytes csv example", attachment_type=attachment_type.CSV)
