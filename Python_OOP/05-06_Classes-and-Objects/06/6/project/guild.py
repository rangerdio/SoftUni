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
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = 'Unaffiliated'
                return f"Player {player_name} has been removed from the guild."
        return f'Player {player_name} is not in the guild.'

    def guild_info(self) -> str:
        # result = f"Guild: {self.name}\n"
        # result += '\n'.join(current_player.player_info() for current_player in self.players)
        # return result
        result = [f"Guild: {self.name}"]
        for player in self.players:
            result.append(player.player_info())
        return '\n'.join(result)
