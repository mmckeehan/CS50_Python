import pygame
from random import randint
from sys import exit

# Classes
import background, bullet

"""class asteroid:
    def __init__(self):
        self.sprite = pygame.image.load("sprites\\asteroid.png").convert_alpha()
        self.position = (100, 100)
        self.sprite_rect = pygame.Surface.get_rect(self.sprite)
        self.rect = (self.position, self.sprite_rect)"""


def main():
    ##################### Random variables #####################
    pygame.init()
    screen_width = 500
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game_active = True
    delta_time = 0

    ##################### Player Variables #####################
    player_hp = 3
    player_sprite = pygame.transform.scale2x(
        pygame.image.load("sprites\\player_anim1.png").convert_alpha()
    )
    player_position = pygame.Vector2(
        (screen.get_width() / 2) - 32, (screen.get_height() - 100)
    )
    player_rect = player_sprite.get_rect(center = player_position)
    player_speed = 250
    player_i_frames_max = 3
    player_i_frames = player_i_frames_max

    ##################### Enemy Variables #####################
    asteroid_sprite = pygame.transform.scale2x(
        pygame.image.load("sprites\\asteroid.png").convert_alpha()
    )
    asteroid_position = pygame.Vector2(
        (screen.get_width() / 2) + 70, (screen.get_height() - 200)
    )
    asteroid_rect = asteroid_sprite.get_rect(center = asteroid_position)
    asteroid_speed = 5

    ##################### Game Variables #####################
    enemy_destroyed = 0
    score_font = pygame.font.Font(None, 50)



    ##################### Main Game Loop #####################
    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        screen.fill("black")

        ########################## Main game goes here ##################################

        # Timer
        time = round(pygame.time.get_ticks() / 1000)
        score_render = score_font.render(f"Score: {score(time, enemy_destroyed)}", None, "white")
        health_render = score_font.render(f"HP: {player_hp}", None, "white")

        # Display Background
        pygame.draw.circle(
            screen,
            "white",
            (randint(0, screen_width), randint(0, screen_height)),
            3,
        )

        # Draw Score and health on screen
        screen.blit(score_render, ((screen_width/2) - 16, 50))
        screen.blit(health_render, (10, 50))

        # Draw Player on screen
        screen.blit(player_sprite, player_rect)

        # Draw Asteroid
        screen.blit(asteroid_sprite, asteroid_rect)
        asteroid_rect.y += asteroid_speed
        if asteroid_rect.y >= screen_height - 20:
            asteroid_rect.x = randint(50, 450)
            asteroid_rect.y = -50

        # Player control functions
        player_controls(player_rect, delta_time, player_speed)


        # Colision
        player_i_frames -= 1 * delta_time
        print(player_i_frames)
        if player_i_frames <= 0:
            if pygame.Rect.colliderect(player_rect, asteroid_rect):
                player_hp -= 1
                player_i_frames = player_i_frames_max


        if player_health(player_hp) == False:
            time = 0
            game_active = False



        ######################### Main game stops here ##################################

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

    if not game_active:
        game_quit()

def score(time, enemy_destroyed):
    total_score = time + (enemy_destroyed * 10)
    return total_score


def player_controls(pos, delta_time, speed):
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        pos.x += speed * delta_time
        return "d"
    if key[pygame.K_a]:
        pos.x -= speed * delta_time
        return "a"
    if key[pygame.K_s]:
        pos.y += speed * delta_time
        return "s"
    if key[pygame.K_w]:
        pos.y -= speed * delta_time
        return "w"
    """if key[pygame.K_UP]:
        bullet.bullet(pos, screen, delta_time)"""
    if key[pygame.K_ESCAPE]:
        game_quit()


def player_health(player_hp):
    if player_hp == 0:
        print("False")
        return False
    else:
        return True


def game_quit():
    exit()


if __name__ == "__main__":
    main()
