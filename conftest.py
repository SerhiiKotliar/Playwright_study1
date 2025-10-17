import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")