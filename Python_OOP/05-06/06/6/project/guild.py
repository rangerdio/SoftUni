from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.members.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        player = next((p for p in self.members if p.guild == player_name), None)
        if not player:
            return f'Player {player_name} is not in the guild.'
        player_name.guild = 'Unaffiliated'
        self.members.remove(player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"

        for current_player in self.members:
            result += '\n'.join(current_player.player_info() for current_player in self.members)
        return result
