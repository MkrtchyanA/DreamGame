from src.main.player import *
from src.main.blocks import *


def main():
    pg.init()
    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption("Super Mario Boy")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))

    bg.fill(Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pg.sprite.Group()
    platforms = []
    entities.add(hero)

    timer = pg.time.Clock()
    while 1:
        timer.tick(60)

        for e in pg.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0, 0))

        x = y = 0
        for row in level:
            for col in row:
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)

                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        hero.update(left, right, up, platforms)
        entities.draw(screen)
        pg.display.update()


if __name__ == "__main__":
    main()
