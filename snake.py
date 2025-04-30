import pygame
import random
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
snake_block_size=10
snake_speed=2
snake_color=(0,255,0)

direction_x=snake_block_size
direction_y=0

snake_x=SCREEN_WIDTH//2
snake_y=SCREEN_HEIGHT//2

food_x=round(random.randrange(0,SCREEN_WIDTH-snake_block_size)/10)*10
food_y=round(random.randrange(0,SCREEN_HEIGHT-snake_block_size)/10)*10
food_color=(255,0,0)

snake_list=[]
snake_length=1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_snake(snake_block_size,snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen,snake_color,[ segment[0],segment[1],snake_block_size,snake_block_size])

def draw_food(food_x,food_y):
    pygame.draw.rect(screen,food_color,[food_x,food_y,snake_block_size,snake_block_size])

def generate_food():
    global food_x,food_y
    food_x=round(random.randrange(0,SCREEN_WIDTH-snake_block_size)/10)*10
    food_y=round(random.randrange(0,SCREEN_HEIGHT-snake_block_size)/10)*10


clock= pygame.time.Clock()
# game logic
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_x=0
                direction_y=-snake_block_size

            elif event.key == pygame.K_DOWN:
                direction_x=0
                direction_y=snake_block_size
            elif event.key == pygame.K_LEFT:
                direction_x=-snake_block_size
                direction_y=0
            elif event.key == pygame.K_RIGHT:
                direction_x=snake_block_size
                direction_y=0

    snake_x += direction_x
    snake_y += direction_y

    snake_head=[snake_x,snake_y]
    snake_list.append(snake_head)
    
    if len(snake_list)> snake_length:
        del snake_list[0]
        print(snake_list)
    
    if snake_x == food_x and snake_y == food_y:
        generate_food()
        snake_length +=1

    screen.fill((0,0,0))
    draw_food(food_x,food_y)
    draw_snake(snake_block_size,snake_list)
            
                
    clock.tick(snake_speed)
    pygame.display.flip()
pygame.quit()
    
