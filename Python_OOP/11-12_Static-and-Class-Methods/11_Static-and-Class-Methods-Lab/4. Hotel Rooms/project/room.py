from typing import Optional, Union


class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Optional[Union[str, None]]:
        if not self.is_taken and self.guests + people <= self.capacity:
            self.guests += people
            self.is_taken = True
        else:
            return f'Room number {self.number} cannot be taken'

    def free_room(self) -> Optional[Union[str, None]]:
        if not self.is_taken:
            return f'Room number {self.number} is not taken'
        self.guests = 0
        self.is_taken = False


