class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        pass

    def player_info(self) -> str:
        sdata = "\n".join(f'==={skill_name} - {skill_mana_cost}' for skill_name, skill_mana_cost in self.skills.items())
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{sdata}'
