import pygame


def updateui():
    (width, height) = (600, 500)
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption('8-Puzzle')

    background_colour = (32, 33, 36)
    screen.fill(background_colour)

    for i in range(0, 9):
        y = 0
        if i == 0 or i == 3 or i == 6:
            x = 0
        elif i == 1 or i == 4 or i == 7:
            x = 200
        else:
            x = 400
        if i > 2 & i < 6:
            y = 166.666667
        if i > 5:
            y = 333.3334
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 200, 166.6667), 1)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

updateui()