  
#---------------------------------------------------------------#
import pygame
import sys
import random
import time
import ctypes
import subprocess
import threading
# START PYGAME MODULES
pygame.init()

# ALL VARIABLE

display_width = 576
display_height = 879
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True
bird_list_index = 0
game_font = pygame.font.Font('assets/font/Flappy.TTF', 45)
score = 0
high_score = 0
active_score = True
button_font = pygame.font.Font('assets/font/Flappy.TTF', 36)

# ---------- #
create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_flap, 80)
pygame.time.set_timer(create_pipe, 1200)
score = 0
# ---------- #
win_sound = pygame.mixer.Sound('assets/sound/smb_stomp.wav')
game_over_sound = pygame.mixer.Sound('assets/sound/smb_mariodie.wav')
loop_sound = pygame.mixer.Sound('assets/sound/org.mp3')
# ---------- #
background_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/floor.png'))
bird_image_down = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_down_flap.png'))
bird_image_mid = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_mid_flap.png'))
bird_image_up = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_up_flap.png'))
bird_list = [bird_image_down, bird_image_mid, bird_image_up]
bird_image = bird_list[bird_list_index]
pipe_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/pipe_red.png'))
game_over_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/message.png'))
game_over_image_rect = game_over_image.get_rect(center=(288, 512))


def generate_pipe_rect():
    random_pipe = random.randrange(400, 800)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe - 300))
    pipe_rect_bottom = pipe_image.get_rect(midtop=(700, random_pipe))
    return pipe_rect_top, pipe_rect_bottom


def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipes


def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            main_screen.blit(pipe_image, pipe)
        else:
            reversed_pipes = pygame.transform.flip(pipe_image, False, True)
            main_screen.blit(reversed_pipes, pipe)


def check_collision(pipes):
    global active_score
    for pipe in pipes:
        if bird_image_rect.colliderect(pipe):
            game_over_sound.play()
            time.sleep(3)
            active_score = True
            return False
        if bird_image_rect.top <= -50 or bird_image_rect.bottom >= 900:
            game_over_sound.play()
            time.sleep(3)
            active_score = True
            return False
    return True


def bird_animation():
    new_bird = bird_list[bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_image_rect.centery))
    return new_bird, new_bird_rect


def display_score(status):
    if status == 'active':
        text1 = game_font.render(str(score), False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(288, 100))
        main_screen.blit(text1, text1_rect)
    if status == 'game_over':
        # SCORE
        text1 = game_font.render(f'Score : {score}', False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(288, 100))
        main_screen.blit(text1, text1_rect)
        # HIGH SCORE
        text2 = game_font.render(
            f'HighScore : {high_score}', False, (255, 255, 255))
        text2_rect = text2.get_rect(center=(288, 795))
        main_screen.blit(text2, text2_rect)


def update_score():
    global score, high_score, active_score
    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and active_score:
                win_sound.play()
                score += 1
                active_score = False
            if pipe.centerx < 0:
                active_score = True

    if score > high_score:
        high_score = score
    return high_score


# ---------- #
bird_image_rect = bird_image.get_rect(center=(100, 520))
# GAME DISPLAY
main_screen = pygame.display.set_mode((display_width, display_height))

# GAME TIMER
clock = pygame.time.Clock()

# GAME LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            # TERMINATE PROGRAM
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_c and game_status == False:
                game_status = True
                pipe_list.clear()
                bird_image_rect.center = (100, 512)
                bird_movement = 0
                score = 0
            if event.key == pygame.K_q and game_status == False:
                pygame.QUIT()
                sys.exit()
                pygame.display.update()
            if event.key == pygame.K_SPACE and not game_status:
                game_status = True
                pipe_list.clear()
                bird_image_rect.center = (100, 512)
                bird_movement = 0
                score = 0
            
         




        if event.type == create_pipe:
            pipe_list.extend(generate_pipe_rect())
        if event.type == create_flap:
            if bird_list_index < 2:
                bird_list_index += 1
            else:
                bird_list_index = 0

            bird_image, bird_image_rect = bird_animation()

    # DISPLAY BG2.PNG
    main_screen.blit(background_image, (0, 0))

    if game_status:
        # DISPLAY BIRD IMAGE
        main_screen.blit(bird_image, bird_image_rect)
        # CHECK FOR COLLISIONS
        game_status = check_collision(pipe_list)
        # MOVE PIPES
        pipe_list = move_pipe_rect(pipe_list)
        display_pipes(pipe_list)
        # FLOOR GRAVITY AND BIRD MOVEMENT
        bird_movement += gravity
        bird_image_rect.centery += bird_movement
        # SHOW SCORE
        update_score()
        display_score('active')
    else:
        main_screen.blit(game_over_image, game_over_image_rect)
        display_score('game_over')
    # DISPLAY FLOOR.PNG
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 820))
    main_screen.blit(floor_image, (floor_x + 576, 820))
    if floor_x <= -576:
        floor_x = 0

    pygame.display.update()
    # SET GAME SPEED
    clock.tick(90)
