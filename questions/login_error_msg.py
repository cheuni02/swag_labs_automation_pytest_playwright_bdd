from abilities.browse_the_web import BrowseTheWeb
from ui.login_page import LoginPage


class LoginErrorMsg:
    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        return page.locator(LoginPage.ERROR).inner_text()
