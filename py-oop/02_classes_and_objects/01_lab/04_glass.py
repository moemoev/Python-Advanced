class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def get_free_space(self):
        free_space = self.capacity - self.content

        return free_space

    def fill(self, ml: int):
        if ml  > self.get_free_space():
            return f"Cannot add {ml} ml"

        self.content += ml

        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0

        return f"Glass is now empty"

    def info(self):
        space_left = self.get_free_space()

        return f"{space_left} ml left"
