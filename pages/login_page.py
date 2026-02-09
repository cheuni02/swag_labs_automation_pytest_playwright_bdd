from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = self.page.locator("[data-test='username']")
        self.password = self.page.locator("[data-test='password']")
        self.login_button = self.page.locator("[data-test='login-button']")
        self.error_container = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto("/")

    def perform_login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_url(self):
        return self.page.url
