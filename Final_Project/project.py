import pygame, sys



def main():
    # Random variables
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    clock = pygame.time.Clock()
    game_active = True
    delta_time = 0

    # Player Variables
    player_sprite = pygame.image.load("sprites/player.png")
    player_position = pygame.Vector2((screen.get_width() /2) - 16, screen.get_height() / 2)
    player_rect = (player_position, (32,32))

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                game_quit()

        screen.fill("black")
        delta_time = clock.tick(60) / 1000


        # Draw main character Sprite
        pygame.draw.rect(screen, "white", player_rect, 32)
        player_movement(player_position, delta_time)


    pygame.display.flip()

def player_movement(pos, dt):
    key = pygame.key.get_pressed()
    if key [pygame.K_d]: pos.x += 300 * dt
    if key [pygame.K_a]: pos.x -= 300 * dt
    if key [pygame.K_s]: pos.y += 300 * dt
    if key [pygame.K_w]: pos.y -= 300 * dt
    if key [pygame.K_ESCAPE]: game_quit

def game_quit():
    pygame.quit()

if __name__=="__main__":
    main()