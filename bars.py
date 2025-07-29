
import pygame
import random

class Bar:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 70
        self.gap_height = 150  # Roughly 3 times the bird's height (50 * 3)
        self.x = screen_width
        self.color = (0, 255, 0)  # Green

        # Randomly determine the position of the gap
        # Ensure there's enough space for top and bottom bars
        min_gap_y = 50  # Minimum distance from top edge
        max_gap_y = screen_height - self.gap_height - 50 # Maximum distance from bottom edge
        self.gap_y = random.randint(min_gap_y, max_gap_y)

        self.top_bar_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        self.bottom_bar_rect = pygame.Rect(self.x, self.gap_y + self.gap_height, self.width, screen_height - (self.gap_y + self.gap_height))
        self.scored = False

    def update(self, bird_speed):
        self.x -= bird_speed
        self.top_bar_rect.x = self.x
        self.bottom_bar_rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.top_bar_rect)
        pygame.draw.rect(screen, self.color, self.bottom_bar_rect)

    def off_screen(self):
        return self.x + self.width < 0
