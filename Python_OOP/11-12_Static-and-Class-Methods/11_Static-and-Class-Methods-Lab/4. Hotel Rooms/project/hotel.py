from typing import Optional, Union
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: list[Room] = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> Optional[Union[str, None]]:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number) -> Optional[Union[str, None]]:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        result = [f'Hotel {self.name} has {self.guests} total guests']
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)
        result.append(f'Free rooms: {", ".join(str(n) for n in free_rooms)}')
        result.append(f'Taken rooms: {", ".join(str(n) for n in taken_rooms)}')
        return '\n'.join(result)

    @property
    def guests(self):
        return sum(room.guests for room in self.rooms)
