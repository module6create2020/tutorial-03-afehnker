import pygame
import sys
from exercises.keyboard_handler import KeyboardHandler
from exercises.bubble import Bubble


class Game:
    """
    Initialize PyGame and create a graphical surface to write
    """
    def __init__(self):
        pygame.init()
        self.red_team=list()
        for i in range(10):
            self.red_team.append(Bubble(400, 400, (255, 0, 0)))

        self.blue_team = list()
        for i in range(10):
            self.blue_team.append(Bubble(400, 400, (0, 0, 255)))

        self.size = [800, 800]
        self.screen = pygame.display.set_mode(self.size)
        #Loads a random system font
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 24)
        self.time = pygame.time.get_ticks()
        self.keyboard_handler = KeyboardHandler()
        self.color = (50,50,50)

    '''
    Main game loop which will be executed every frame
    '''
    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()


    '''
    Put all logic here
    '''
    def update_game(self, dt):
        for b in self.red_team:
            b.move(100,100,self.size[0]-150, self.size[1]-150)
            for a in self.blue_team:
                b.collide(a)

        for b in self.blue_team:
            b.move(100,100,self.size[0]-150, self.size[1]-150)
            for a in self.red_team:
                b.collide(a)




    '''
    Put all draw calls here
    '''
    def draw_components(self):
        self.screen.fill([255, 255, 255])
        pygame.draw.rect(self.screen, self.color, [[100, 100], [self.size[0] - 200, self.size[1] - 200]])
        for b in self.red_team:
            b.display(self.screen,self.font)
        for b in self.blue_team:
            b.display(self.screen,self.font)
        # updates the entire surface (canvas)
        pygame.display.flip()


    def reset(self):
        pass

    '''
    Loop over all the event types and handle them accordingly
    '''
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)
            if event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_pressed(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_released(event)

    def handle_key_down(self, event):
        self.keyboard_handler.key_pressed(event.key)

    def handle_key_up(self, event):
        self.keyboard_handler.key_released(event.key)

    def handle_mouse_motion(self, event):
        pass

    def handle_mouse_pressed(self, event):
        pass

    def handle_mouse_released(self, event):
        pass


if __name__ == "__main__":
    g = Game()
    while True:
        g.game_loop()

