import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

class Slider:
    def __init__(self, x, y, length, min_value, max_value, mixer):
        self.x = x
        self.y = y
        self.length = length
        self.min_value = min_value
        self.max_value = max_value
        self.value = max_value
        self.dragging = False
        self.mixer = mixer

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.length, 10))
        handle_x = self.x + int(self.length * (self.value - self.min_value) / (self.max_value - self.min_value))
        pygame.draw.circle(screen, BLACK, (handle_x, self.y + 5), 10)
        font = pygame.font.Font("elgatoassets/Carnevalee Freakshow.ttf", 30)
        text = font.render(f"{int(self.value * 100)}%", True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.length // 2, self.y - 25))
        screen.blit(text, text_rect)

    def update(self):
        if self.dragging:
            handle_x = pygame.mouse.get_pos()[0]
            handle_x = min(max(handle_x, self.x), self.x + self.length)
            self.value = self.min_value + (handle_x - self.x) / self.length * (self.max_value - self.min_value)
            self.mixer.music.set_volume(self.value)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                handle_x = self.x + int(self.length * (self.value - self.min_value) / (self.max_value - self.min_value))
                handle_rect = pygame.Rect(handle_x - 10, self.y - 5, 20, 20)
                if handle_rect.collidepoint(event.pos):
                    self.dragging = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
        elif event.type == MOUSEMOTION:
            if self.dragging:
                self.update()


