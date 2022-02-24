import pygame


class Window:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name) -> None:
        self.name = new_name

    def set_width(self, new_width) -> None:
        self.width = new_width

    def set_height(self, new_height) -> None:
        self.height = new_height

    def set_screen(self, width, height) -> pygame.display.set_mode():
        self.width = width
        self.height = height
        new_screen = pygame.display.set_mode(self, self.width, self.height)
        print(f"Width: {self.width}, Height: {self.height}")
        return new_screen

    def set_screen_name(self, name) -> pygame.display.set_caption(get_name()):
        self.name = name
        return pygame.display.set_caption(name)

    def get_screen(self):
        x = self.width
        y = self.height
        return x, y

    @staticmethod
    def set_fps(fps):
        try:
            fps = pygame.time.Clock.tick(fps)
        except pygame.error():
            print(f"{fps}")
        return print(fps.set_fps(fps))
