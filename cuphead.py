import pygame
import sprite_class

# Initialize pygame
pygame.init()

# Create screen dimensions
screen_width = 500
screen_height = 500

# Create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('spritesheets')

# Load sprite sheet image
sprite_sheets_image = pygame.image.load("Custom Edited - Cuphead Customs - Cuphead NES-Style.png").convert_alpha()
sprite_sheet = sprite_class.SpriteSheet(sprite_sheets_image)

BG = (0, 0, 0)
cyan = (84, 165, 75)

# Create a list of frames
animation_list = []
animation_steps = [9, 1, 9, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 180
frame = 0
step_counter = 0
position_x = 20
position_y = 20
image_movement_up = False
image_movement_down = False
image_movement_right = False
image_movement_left = False

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 49, 50, 3, cyan))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:

    # Fill the screen
    screen.fill(BG)

    # Update the animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # Display one of the sprites
    screen.blit(animation_list[action][frame], (position_x, position_y))

    # Update the vertical position of the image based on movements
    if image_movement_up:
        position_y -= 0.1
    elif image_movement_down:
        position_y += 0.1
    elif image_movement_right:
        position_x += 0.1
    elif image_movement_left:
        position_x -= 0.1

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                image_movement_up = True
            elif event.key == pygame.K_DOWN:
                image_movement_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                image_movement_up = False
            elif event.key == pygame.K_DOWN:
                image_movement_down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                image_movement_right = True
            elif event.key == pygame.K_LEFT:
                image_movement_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                image_movement_right = False
            elif event.key == pygame.K_LEFT:
                image_movement_left = False

    pygame.display.update()

pygame.quit()