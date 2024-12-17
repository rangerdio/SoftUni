from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=8)

    def zone_info(self):
        royal_ships = sum(1 for ship in self.ships if not isinstance(ship, type(self)))
        battleships = len(self.ships)
        ship_names = ", ".join(f"#{ship.name}#" for ship in self.get_ships())

        info = f"@Pirate Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
        info += f"Battleships currently in the Pirate Zone: {battleships}, {royal_ships} out of them are Royal Battleships.\n"
        if ship_names:
            info += ship_names
        return info
