import pygame


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 640, 480

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size,
                                              pygame.HWSURFACE |
                                              pygame.DOUBLEBUF)
        self._running = True

        # self.draw_background()
        # self.draw_balls()
        # update screen
        # pygame.display.flip()
        # pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            print('saindo..')
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('saindo..')
                self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def draw_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((100, 110, 120))
        self.background = self.background.convert()

    def draw_balls(self):
        self.ball_surface = pygame.Surface((50, 50))
        pygame.draw.circle(self.ball_surface, (200, 190, 205), (25, 25), 25)
        self.ball_surface = self.ball_surface.convert()
        pygame.draw.rect(self.background, (0, 255, 0), (50, 50, 100, 25))
        self.screen.blit(self.background, (50, 300))
        self.ball_x = 120
        self.ball_y = 240
        self.screen.blit(self.ball_surface,
                                   (self.ball_x,
                                    self.ball_y))


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
