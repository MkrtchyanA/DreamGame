import pygame as pg

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

UP = pg.K_w
DOWN = pg.K_s
LEFT = pg.K_a
RIGHT = pg.K_d

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

TEST_HERO_PATH = "../resources/testHero.png"

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

JUMP_POWER = 20
GRAVITY = 0.98
