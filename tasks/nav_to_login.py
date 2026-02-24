from abilities.browse_the_web import BrowseTheWeb
from ui.login_page import LoginPage


class NavToLogin:
    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        page.goto(LoginPage.BASE_URL)
