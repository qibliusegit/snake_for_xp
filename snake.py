import pygame
import random

pygame.init()
window = pygame.display.set_mode((720,480))
color = (255, 192, 203)  
run = True
momentum = "east"
score = 0

pygame.display.flip()
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = "right"
pygame.draw.rect(window, color, pygame.Rect(snake_pos[0], snake_pos[1], 10, 10))
pygame.display.flip()
food_x = 0
food_y = 0

def randomize_food():
    global food_x
    global food_y
    food_x = random.randint(0, 720) 
    food_y = random.randint(0, 480)
    i = food_x
    j = food_y 
    while food_x % 10 != 0:
        food_x += 1
    while food_y % 10 != 0:
        food_y += 1

randomize_food()

food = pygame.Rect(food_x, food_y, 10, 10)

for x in snake_body:
    pygame.draw.rect(window, color, pygame.Rect(x[0], x[1], 10, 10))
    pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(window, "red", food)
    pygame.display.flip()
    pygame.time.Clock().tick(10)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_DOWN and direction != "up": 
                direction = "down"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"

    if direction == "up":
        snake_pos[1] -= 10
    elif direction == "down":
        snake_pos[1] += 10
    elif direction == "right":
        snake_pos[0] += 10
    elif direction == "left":
        snake_pos[0] -= 10
    
    window.fill((0, 0, 0))
    pygame.display.flip() 
    pygame.draw.rect(window, color, pygame.Rect(snake_pos[0], snake_pos[1], 10, 10))
    old = snake_pos.copy()
    
    
    for x in range(len(snake_body)-1, 0, -1):
        snake_body[x] = snake_body[x-1].copy()
    snake_body[0] = snake_pos
    
    for x in snake_body:
        pygame.draw.rect(window, color, pygame.Rect(x[0], x[1], 10, 10))
    pygame.display.flip()

    if snake_pos[0] == food_x and snake_pos[1] == food_y:
        score += 1
        snake_body.append([food_x, food_y])
        randomize_food()
        food = pygame.Rect(food_x, food_y, 10, 10)
        pygame.draw.rect(window, "red", food)
    
    if snake_pos[0] < 0 or snake_pos[0] > 720:
        run = False
    if snake_pos[1] < 0 or snake_pos[1] > 480:
        run = False



pygame.quit()