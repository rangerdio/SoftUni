class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills.items():
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self) -> str:
        # dat = "\n".join(f'==={skill_name} - {skill_mana_cost}' for skill_name, skill_mana_cost in self.skills.items())
        # return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{dat}'
        result = [f'Name: {self.name}', f'Guild: {self.guild}', f'HP: {self.hp}', f'MP: {self.mp}']
        for skill_name, skill_mana_cost in self.skills.items():
            result.append(f'=== {skill_name} - {skill_mana_cost}')
        return '\n'.join(result)
