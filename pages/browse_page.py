from playwright.sync_api import Page


class BrowsePage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = self.page.locator("[data-test='inventory-item-name']").all()

    def item_names(self):
        names = []
        for item in self.inventory_items:
            names.append(item.inner_text())
        return names