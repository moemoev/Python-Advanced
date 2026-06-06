class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def set_time(self,hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def next_second(self):
        self.seconds += 1

        if Time.max_seconds < self.seconds:
            self.seconds = 0
            self.minutes += 1

        if Time.max_minutes < self.minutes:
            self.minutes = 0
            self.hours += 1

        if Time.max_hours < self.hours:
            self.hours = 0

        return self.get_time()


time_1 = Time(9, 30, 59)
print(time_1.next_second())

time_2 = Time(10, 59, 59)
print(time_2.next_second())

time_3 = Time(23, 59, 59)
print(time_3.next_second())
