from abilities.browse_the_web import BrowseTheWeb
from ui.browse_page import BrowsePage


class ItemsDisplayed:
    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        items = page.locator(BrowsePage.ITEMS)
        return items.all_inner_texts()
