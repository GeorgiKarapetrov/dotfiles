import sys
import pygame as pg


class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Sprite(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class TheHollyOne:
    def __init__(self):
        # mixer
        pg.mixer.init(96000)
        pg.mixer.music.load('audio.ogg')
        pg.mixer.music.play(-1)
        # graphical
        pg.init()
        pg.display.set_caption('Do your part. Subscribe to PewDiePie.')
        self.screen = pg.display.set_mode([800, 500])
        self.rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.BG = Background('BG.jpg', [0, 0])
        self.HAT = Sprite("Sprite.png", [400, 250])
        self.EVENTS = [pg.K_LEFT, pg.K_RIGHT, pg.K_DOWN, pg.K_UP]
        # events
        pg.key.set_repeat(10, 10)

    def draw(self):
        self.screen.fill([255, 255, 255])
        self.screen.blit(self.BG.image, self.BG.rect)
        self.screen.blit(self.HAT.image, self.HAT.rect)

    def wait_for_events(self):
        pg.display.update()
        self.clock.tick(60)

    def process_keyboard(self, event):
        if (event.key == pg.K_LEFT):
            self.HAT.rect.centerx -= 4
        elif (event.key == pg.K_RIGHT):
            self.HAT.rect.centerx += 4
        elif (event.key == pg.K_UP):
            self.HAT.rect.centery -= 4
        elif (event.key == pg.K_DOWN):
            self.HAT.rect.centery += 4
        self.HAT.rect.clamp_ip(self.rect)
        self.draw()

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key in self.EVENTS:
                self.process_keyboard(event)


def easter_eggs():
    """Take action on some hat positions."""

    # TODO


pew = TheHollyOne()
while True:
    pew.draw()
    pew.wait_for_events()
    pew.process_events()
