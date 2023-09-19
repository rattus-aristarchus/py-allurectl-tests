import allure


def github_issues(*issues):
    return allure.label("github", *issues)
