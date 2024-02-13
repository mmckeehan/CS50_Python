import project
import pytest
import pygame

def test_player_health():
    assert project.player_health(3) == True
    assert project.player_health(0) == False


def test_score():
    assert project.score(0, 0) == 0
    assert project.score(1, 0) == 1
    assert project.score(5, 3) == 35


def test_player_controls():
    pos = pygame.math.Vector2(0, 0)
    delta_time = 1
    speed = 10

    pygame.key.get_pressed = lambda: {pygame.K_d: True}
    assert project.player_controls(pos, delta_time, speed) == "d"