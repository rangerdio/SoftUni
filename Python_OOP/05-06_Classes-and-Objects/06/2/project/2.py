class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self) -> str:
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def next_second(self) -> str:
        next_total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + 1
        self.hours = (next_total_seconds // 3600) % (self.max_hours + 1)
        print(f'({next_total_seconds} // {3600}) :{next_total_seconds // 3600}   ({next_total_seconds} // {3600}) % ({self.max_hours + 1}) :{(next_total_seconds // 3600) % (self.max_hours + 1)}')
        self.minutes = (next_total_seconds // 60) % (self.max_minutes + 1)
        self.seconds = next_total_seconds % (self.max_seconds + 1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
