from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone
from project.battleships.base_battleship import BaseBattleship


class BattleManager:
    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type == "RoyalZone":
            zone = RoyalZone(zone_code)
        elif zone_type == "PirateZone":
            zone = PirateZone(zone_code)
        else:
            raise Exception("Invalid zone type!")
        if any(z.code == zone_code for z in self.zones):
            raise Exception("Zone already exists!")
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type == "RoyalBattleship":
            ship = RoyalBattleship(name, health, hit_strength)
        elif ship_type == "PirateBattleship":
            ship = PirateBattleship(name, health, hit_strength)
        else:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"
        if isinstance(ship, RoyalBattleship) != isinstance(zone, RoyalZone):
            ship.is_attacking = False
        else:
            ship.is_attacking = True
        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]
        if len(attackers) < 1 or len(targets) < 1:
            return "Not enough participants. The battle is canceled."
        attacker = max(attackers, key=lambda s: s.hit_strength)
        target = max(targets, key=lambda s: s.health)

        attacker.attack()
        target.take_damage(attacker)

        if target.health == 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."
        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."
