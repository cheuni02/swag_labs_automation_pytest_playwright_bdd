from abilities.browse_the_web import BrowseTheWeb


class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities: dict[type[BrowseTheWeb], BrowseTheWeb] = {}

    def can(self, ability: BrowseTheWeb):
        self.abilities[type(ability)] = ability

    def ability_to(self, ability_cls: type[BrowseTheWeb]) -> BrowseTheWeb:
        return self.abilities[ability_cls]

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)

    def asks_for(self, question):
        return question.answered_by(self)
