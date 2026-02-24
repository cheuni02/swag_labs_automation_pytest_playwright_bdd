from abilities.browse_the_web import BrowseTheWeb


class TextOf:
    def __init__(self, element_locator):
        self.element_locator = element_locator

    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        return page.locator(self.element_locator).inner_text()
