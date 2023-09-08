import json
import os
import time

import allure
from allure import attachment_type

from conftest import github_issues


def test_attach_bigimage():
    print("After this step we'll have a pause for 10 seconds")
    allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    time.sleep(10)
    print("After this step we'll have a pause for 1 second")
    allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    time.sleep(1)
    allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    time.sleep(5)
    allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    time.sleep(10)
    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    time.sleep(10)
    allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

