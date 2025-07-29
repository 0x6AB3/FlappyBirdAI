import pygame
import time

class Bird:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 50
        self.height = 50
        self.x = screen_width / 6
        self.y = (screen_height - self.height) / 3
        self.velocity = 0
        self.gravity = 0.00005
        self.speed = 0.05

        self.normal_image = pygame.image.load('birdnormal.png').convert_alpha()
        self.normal_image = pygame.transform.scale(self.normal_image, (self.width, self.height))
        self.jump_image = pygame.image.load('birdjump.png').convert_alpha()
        self.jump_image = pygame.transform.scale(self.jump_image, (self.width, self.height))
        self.current_image = self.normal_image

        self.last_jump_time = 0
        self.jump_duration = 0.5 # seconds

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
        if self.y < 0:
            self.y = 0
            self.velocity = 0

        # Handle jump animation
        if time.time() - self.last_jump_time < self.jump_duration:
            self.current_image = self.jump_image
        else:
            self.current_image = self.normal_image

    def jump(self):
        max_upward_speed_magnitude = 3 * 0.08
        self.velocity -= 0.08
        if self.velocity < -max_upward_speed_magnitude:
            self.velocity = -max_upward_speed_magnitude
        self.last_jump_time = time.time()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        # Calculate rotation angle based on velocity
        # Map velocity to a rotation angle, capping at +/- 90 degrees
        # A negative velocity means going up, so positive rotation (nose up)
        # A positive velocity means going down, so negative rotation (nose down)
        rotation_angle = self.velocity * -900

        # Cap the rotation angle between -90 and 90 degrees
        if rotation_angle > 90:
            rotation_angle = 90
        elif rotation_angle < -90:
            rotation_angle = -90

        # Rotate the current image
        rotated_image = pygame.transform.rotate(self.current_image, rotation_angle)

        # Scale the rotated image back to the bird's original dimensions (50x50)
        # This ensures it always "stretches across the whole bird object"
        final_image = pygame.transform.scale(rotated_image, (self.width, self.height))

        # Get the rect for the final image, centered at the bird's position
        bird_center_x = self.x + self.width / 2
        bird_center_y = self.y + self.height / 2
        new_rect = final_image.get_rect(center=(bird_center_x, bird_center_y))

        screen.blit(final_image, new_rect)
