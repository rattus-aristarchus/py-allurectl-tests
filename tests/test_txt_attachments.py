import json
import os

import allure
from allure import attachment_type


def test_attach_small_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)


def test_attach_normal_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)


def test_attach_medium_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)


def test_attach_big_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)