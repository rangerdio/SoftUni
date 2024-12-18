from .base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        pass

    def report_shift(self):
        pass
