import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

def create_surface(text, font_size, rgb, background_rgb):
    font = pygame.freetype.SysFont("arial", font_size, bold=True)
    surface, = font.render(text=text, fgcolor=rgb, backcolor=background_rgb)
    return surface.convert_alpha()

class UIClass(Sprite):
    def __init__(self, p_center, text, font_size, backcolor, textcolor):
        self.mouse_over = False
        default_img = create_surface(text, font_size, textcolor, backcolor)
        highlight_img = create_surface(text, font_size*1.4, textcolor, backcolor)

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