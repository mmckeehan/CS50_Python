import pygame, sys, random
# Classes
import background


def main():
    # Random variables
    pygame.init()
    screen_width = 1080
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game_active = True
    delta_time = 0

    # Player Variables
    player_sprite = pygame.transform.scale2x(
        pygame.image.load("sprites\\player_anim1.png").convert()
    )
    player_position = pygame.Vector2(
        (screen.get_width() / 2) - 16, screen.get_height() / 2
    )
    player_rect = (player_position, (32, 32))
    player_speed = 250

    # Background


    # Main Game Loop
    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        screen.fill("black")

        ########################## Main game goes here ##################################

        # Will need to make this a variable that travels down the screen.
        pygame.draw.circle(screen, "white", (random.randint(0, screen_width), 0), 2)

        pygame.draw.rect(screen, "white", player_rect)
        screen.blit(player_sprite, player_rect)
        player_movement(player_position, delta_time, player_speed)

        ######################### Main game stops here ##################################

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

    game_quit()


def player_movement(pos, dt, speed):
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        pos.x += speed * dt
    if key[pygame.K_a]:
        pos.x -= speed * dt
    if key[pygame.K_s]:
        pos.y += speed * dt
    if key[pygame.K_w]:
        pos.y -= speed * dt
    if key[pygame.K_ESCAPE]:
        game_quit()


def game_quit():
    pygame.quit()


if __name__ == "__main__":
    main()
