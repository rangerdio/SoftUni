from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return f'Player {player_name} is not in the guild.'
        player_name.guild = 'Unaffiliated'
        self.players.remove(player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"
        result += '\n'.join(current_player.player_info() for current_player in self.players)
        return result
