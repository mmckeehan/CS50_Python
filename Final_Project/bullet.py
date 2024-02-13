import pygame

class bullet:

    def __init__(self, player_pos, screen, delta_time):
        bullet_sprite = pygame.image.load("sprites\\bullet.png")
        bullet_pos = pygame.Vector2(player_pos)

        # Bullet 1
        bullet_rect1 = ((bullet_pos.x + 5, bullet_pos.y), (32, 32))
        pygame.draw.rect(bullet_sprite, "white", bullet_rect1)
        screen.blit(bullet_sprite, bullet_rect1)

        #bullet 2
        bullet_rect2 = ((bullet_pos.x + 30, bullet_pos.y), (32, 32))
        pygame.draw.rect(bullet_sprite, "white", bullet_rect2)
        screen.blit(bullet_sprite, bullet_rect2)

        """if pygame.key.get_pressed(pygame.K_UP):
            self.bullet_move(bullet_pos, delta_time)"""

    def bullet_move(self, bullet_pos, delta_time):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            bullet_velocity = 300
            bullet_pos = bullet_velocity * delta_time
            print(bullet_pos)