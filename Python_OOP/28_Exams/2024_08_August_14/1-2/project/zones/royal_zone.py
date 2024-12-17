from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        pirate_ships = sum(1 for ship in self.ships if not isinstance(ship, type(self)))
        battleships = len(self.ships)
        ship_names = ", ".join(f"#{ship.name}#" for ship in self.get_ships())

        info = f"@Royal Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
        info += (f"Battleships currently in the Royal Zone:"
                 f" {battleships}, {pirate_ships} out of them are Pirate Battleships.\n")
        if ship_names:
            info += ship_names
        return info
