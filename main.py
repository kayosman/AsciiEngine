import pygame_menu

from window import *


# def create_menu():
#     _exit = pygame_menu.events.EXIT()
#     while not _exit:
#         menu = pygame_menu.Menu('Ascii Engine(Kayos Engine)', 200, 300,
#                                 theme=pygame_menu.themes.THEME_DARK)
#         menu.is_enabled()
#         if _exit:
#             return _exit


def create_window():  # sourcery skip: extract-method, move-assign
    print("Setting screen height\n")
    inp_x = input("X:-> ")
    inp_y = input("Y:-> ")
    x = int(inp_x)
    y = int(inp_y)
    name = "Kayos Engine(Ascii Edition)"
    if y != 0:
        running = True
        game_loop_window = Window(x, y, name)
        Window.set_screen(game_loop_window, x, y)
        Window.set_screen_name(game_loop_window, name)
        try:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
        except SystemExit:
            pygame.quit()


def main():
    create_window()


if __name__ == '__main__':
    main()
