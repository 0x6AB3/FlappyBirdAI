import pygame
from bird import Bird
from bars import Bar
import time

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bird = Bird(width, height)
bars = []
score = 0

# Bar spawning timer
bar_spawn_time = time.time()
bar_spawn_interval = 3  # Increased interval for more space between bars

# Font for score display
    # Font for score display
font = pygame.font.Font(None, 74)
game_over_font = pygame.font.Font(None, 100)

running = True
game_started = False
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    # Reset game
                    bird = Bird(width, height)
                    bars = []
                    score = 0
                    game_over = False
                    game_started = False
                    bar_spawn_time = time.time()
                elif not game_started:
                    game_started = True
                bird.jump()

    if not game_over and game_started:
        bird.update()

        # Adjust bar spawn interval based on score
        current_bar_spawn_interval = max(0.8, bar_spawn_interval - (score * 0.05)) # Minimum interval of 0.8 seconds

        # Spawn new bars
        if time.time() - bar_spawn_time > current_bar_spawn_interval:
            bars.append(Bar(width, height))
            bar_spawn_time = time.time()

        # Update and draw bars, remove off-screen bars
        for bar in list(bars):
            bar.update(bird.speed)
            # Check for scoring
            if not bar.scored and bar.x + bar.width < bird.x:
                score += 1
                bar.scored = True

            # Check for collision with bars
            if bird.get_rect().colliderect(bar.top_bar_rect) or bird.get_rect().colliderect(bar.bottom_bar_rect):
                game_over = True

            if bar.off_screen():
                bars.remove(bar)

        # Check for collision with ground
        if bird.y + bird.height > height:
            game_over = True

    screen.fill(BLACK)
    bird.draw(screen)

    for bar in bars:
        bar.draw(screen)

    # Sensor visualization
    if not game_over and game_started:
        next_bar = None
        for bar in bars:
            if bar.x + bar.width > bird.x:
                next_bar = bar
                break

        if next_bar:
            bird_center_x = bird.x + bird.width / 2
            bird_center_y = bird.y + bird.height / 2

            # Ray to top-left of top bar
            pygame.draw.line(screen, (255, 0, 0), (bird_center_x, bird_center_y), (next_bar.x, next_bar.gap_y), 2)
            # Ray to top-right of top bar
            pygame.draw.line(screen, (255, 0, 0), (bird_center_x, bird_center_y), (next_bar.x + next_bar.width, next_bar.gap_y), 2)
            # Ray to bottom-left of bottom bar
            pygame.draw.line(screen, (255, 0, 0), (bird_center_x, bird_center_y), (next_bar.x, next_bar.gap_y + next_bar.gap_height), 2)
            # Ray to bottom-right of bottom bar
            pygame.draw.line(screen, (255, 0, 0), (bird_center_x, bird_center_y), (next_bar.x + next_bar.width, next_bar.gap_y + next_bar.gap_height), 2)

            # AI logic: try to stay as low as possible to the bottom bar
            # Jump only if the bird is falling and its bottom is getting too close to the bottom bar
            if bird.velocity > 0 and (bird.y + bird.height) > (next_bar.gap_y + next_bar.gap_height - 10): # 10 pixels buffer from bottom bar
                bird.jump()

        # Always check for ground and draw ground sensors
        bird_center_x = bird.x + bird.width / 2
        bird_center_y = bird.y + bird.height / 2

        # Ray to top of screen
        pygame.draw.line(screen, (0, 0, 255), (bird_center_x, bird_center_y), (bird_center_x, 0), 2)
        # Ray to bottom of screen (ground)
        pygame.draw.line(screen, (0, 0, 255), (bird_center_x, bird_center_y), (bird_center_x, height), 2)

        # AI logic: jump if too close to ground and moving downwards
        distance_to_ground = height - (bird.y + bird.height)
        if distance_to_ground < 50 and bird.velocity > 0: # If less than 50 pixels from ground and falling
            bird.jump()

            # Display distances (optional, for debugging)
            # dist_top = next_bar.gap_y - bird_center_y
            # dist_bottom = (next_bar.gap_y + next_bar.gap_height) - bird_center_y
            # dist_text = font.render(f"T: {int(dist_top)} B: {int(dist_bottom)}", True, WHITE)
            # screen.blit(dist_text, (bird_center_x + 20, bird_center_y))

    # Display score
    score_text = font.render(str(score), True, WHITE)
    score_rect = score_text.get_rect(center=(width / 2, 50))
    screen.blit(score_text, score_rect)

    if game_over:
        game_over_text = game_over_font.render("Game Over!", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(width / 2, height / 2 - 50))
        screen.blit(game_over_text, game_over_rect)

        final_score_text = font.render(f"Score: {score}", True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(width / 2, height / 2 + 20))
        screen.blit(final_score_text, final_score_rect)
    elif not game_started:
        # Keep bird at initial position if game not started
        bird.y = (height - bird.height) / 2
        bird.velocity = 0
        start_text = font.render("Press Space to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(width / 2, height / 2))
        screen.blit(start_text, start_rect)

    pygame.display.flip()

pygame.quit()