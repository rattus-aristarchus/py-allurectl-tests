import os
import allure

from allure import attachment_type


def test_attach_smallimage():
    with allure.step("Sending small mp4 attach"):
        allure.attach.file(os.path.join("./resources", "mp4.mp4"), name="mp4file", attachment_type=attachment_type.MP4)
