import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, parsers, then

from pages.browse_page import BrowsePage
from pages.login_page import LoginPage

scenarios("../features/login_flow.feature")

@pytest.fixture(autouse=True)
def login_page_obj(page: Page):
    login_page = LoginPage(page)
    return login_page

@given("I am on the login page")
def step_nav_to_login(login_page_obj):
    login_page_obj.goto()

@when(parsers.parse('I log on as "{username}" with pw "{password}"'))
def step_login_process(login_page_obj, username, password):
    login_page_obj.perform_login(username, password)

@then("I should be taken to my product browse page")
def step_successful_login(login_page_obj, page: Page):
    assert "/inventory.html" in login_page_obj.get_url()

@then("Be shown normal products")
def step_products_displayed_are_normal(page: Page):
    browse_page = BrowsePage(page)
    expected_normal_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]
    for item in expected_normal_items:
        assert item in browse_page.item_names()


@then(parsers.parse('I should see error "{error}"'))
def step_error_is_displayed(login_page_obj, error):
    expect(login_page_obj.error_container).to_contain_text(error)