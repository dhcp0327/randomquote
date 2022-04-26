import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)


def create_surface(text, font_size, rgb, bck_rgb):
    font = pygame.freetype.SysFont("arial", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=rgb, bgcolor =bck_rgb)
    return surface.convert_alpha()


class UIClass(Sprite):
    def __init__(self, p_center, text, font_size, bck_rgb, textcolor):
        super().__init__()
        self.mouse_over = False
        default_img = create_surface(text, font_size, textcolor, bck_rgb)
        highlight_img = create_surface(text, font_size * 1.4, textcolor, bck_rgb)

        self.images = [default_img, highlight_img]
        self.rects = [default_img.get_rect(center=p_center), highlight_img.get_rect(center=p_center)]

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, p_mouse):
        if self.rect.collidepoint(p_mouse):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.images, self.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    # create a ui element
    useui = UIClass(
        p_center= (400, 400),
        font_size=30,
        bck_rgb= BLUE,
        textcolor= WHITE,
        text= "Test in Progress"
    )

    # main loop
    while True:
        for event in pygame.event.get():
            pass
        screen.fill(BLUE)

        useui.update(pygame.mouse.get_pos())
        useui.draw(screen)
        pygame.display.flip()


main()
