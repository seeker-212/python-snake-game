#use pip install pygame and enjoy

import pygame
import random


pygame.init()


WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 5  


WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


snake_x = random.randint(1, GRID_WIDTH - 2) * GRID_SIZE
snake_y = random.randint(1, GRID_HEIGHT - 2) * GRID_SIZE
snake_direction = (0, -1)  

snake_body = [(snake_x, snake_y)]

food_x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
food_y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE


score = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    
    new_head = (snake_body[0][0] + snake_direction[0] * GRID_SIZE,
                snake_body[0][1] + snake_direction[1] * GRID_SIZE)
    snake_body.insert(0, new_head)


    if snake_body[0] == (food_x, food_y):
        score += 1
        food_x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        food_y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
    else:
        snake_body.pop()


    if (snake_body[0][0] < 0 or snake_body[0][0] >= WIDTH or
        snake_body[0][1] < 0 or snake_body[0][1] >= HEIGHT or
        snake_body[0] in snake_body[1:]):
        running = False


    screen.fill(WHITE)
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, GRID_SIZE, GRID_SIZE))


    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.flip()


    clock.tick(SNAKE_SPEED)


font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, RED)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()


pygame.time.wait(2000)

pygame.quit()
