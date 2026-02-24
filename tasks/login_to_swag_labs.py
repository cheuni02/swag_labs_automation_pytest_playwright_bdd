from abilities.browse_the_web import BrowseTheWeb
from ui.login_page import LoginPage


class LogIn:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        page.locator(LoginPage.USERNAME).fill(self.username)
        page.locator(LoginPage.PASSWORD).fill(self.password)
        page.locator(LoginPage.LOGIN_BUTTON).click()
