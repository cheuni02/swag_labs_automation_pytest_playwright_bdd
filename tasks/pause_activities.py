from abilities.browse_the_web import BrowseTheWeb


class PauseActivities:
    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        page.pause()
