from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests= 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"

        return cls(name)

    def add_room(self, room : Room):
        self.rooms.append(room)

    def _get_room_by_number(self, room_number :int ):
        room, = [r for r in self.rooms if r.number == room_number]

        return room

    def take_room(self, room_number: int, people: int):
        room = self._get_room_by_number(room_number)

        if room.take_room(people) is None:
            self.guests += people

    def free_room(self,room_number: int):
        room = self._get_room_by_number(room_number)
        guests = room.guests

        if room.free_room() is None:
            self.guests -= guests


    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"\
                 f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"\
                 f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"

        return result
