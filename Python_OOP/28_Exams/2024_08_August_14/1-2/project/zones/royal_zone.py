from project.zones.base_zone import BaseZone
from project.battleships.pirate_battleship import PirateBattleship


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        pirate_ships = sum(1 for ship in self.ships if isinstance(ship, PirateBattleship))
        battleships = len(self.ships)
        ship_names = ", ".join(f"{ship.name}" for ship in self.get_ships())
        ship_names = "#" + ship_names + "#" if ship_names else ""

        info = f"@Royal Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
        info += f"Battleships currently in the Royal Zone: {battleships}, {pirate_ships} out of them are Pirate Battleships.\n"
        if ship_names:
            info += ship_names
        return info
