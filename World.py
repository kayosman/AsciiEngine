class World:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, new_x) -> None:
        self.x = new_x

    def set_y(self, new_y) -> None:
        self.y = new_y

    def set_world_size(self, x, y) -> int:
        self.x = x
        self.y = y
        new_world = x * y
        print(f"World Created!!! width:({x}) height:({y})")
        return new_world

    def get_world_size(self) -> int:
        return self.set_world_size(self.x, self.y)