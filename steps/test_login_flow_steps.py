from pytest_bdd import given, parsers, scenarios, then, when

from abilities.browse_the_web import BrowseTheWeb
from questions.items_displayed import ItemsDisplayed
from questions.login_error_msg import LoginErrorMsg
from questions.text_of import TextOf
from tasks.login_to_swag_labs import LogIn
from tasks.nav_to_login import NavToLogin
from ui.login_page import LoginPage

scenarios("../features/login_flow.feature")


@given("I am on the login page")
def step_nav_to_login(actor):
    actor.attempts_to(NavToLogin())

    logo_text = actor.asks_for(TextOf(LoginPage.LOGO))
    assert logo_text == "Swag Labs"


@when(parsers.parse('I log on as "{username}" with pw "{password}"'))
def step_nav_to_log_in(actor, username: str, password: str):
    actor.attempts_to(
        LogIn(username, password),
    )


@then("I should be taken to my product browse page")
def step_successful_login(actor):
    assert "/inventory.html" in actor.ability_to(BrowseTheWeb).page.url


@then("Be shown normal products")
def step_products_displayed_are_normal(actor):
    expected_normal_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ]

    actual_items = actor.asks_for(ItemsDisplayed())
    for item in actual_items:
        assert item in expected_normal_items, f"Item {item} is not displayed"


@then(parsers.parse('I should see error "{error}"'))
def step_error_is_displayed(actor, error):
    error_msg = actor.asks_for(LoginErrorMsg())
    assert error in error_msg
