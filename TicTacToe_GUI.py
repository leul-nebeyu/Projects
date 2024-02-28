import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

size = WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")
FPS = 60
FONT = pygame.font.SysFont("comicsans", 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (218, 170, 87)


def draw_window():
    WIN.fill(WHITE)
    # Draw Grid
    pygame.draw.rect(WIN, BLACK, pygame.Rect(WIDTH // 3 - 5, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(
        WIDTH // 3 + WIDTH // 3 - 5, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, HEIGHT // 3 - 5, WIDTH, 10))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(
        0, HEIGHT // 3 + HEIGHT // 3 - 5, WIDTH, 10))
    pygame.display.update()


def get_box(x, y):
    if 0 <= x <= 195 and 0 <= y <= 195:
        return 1
    elif 200 <= x <= 395 and 0 <= y <= 195:
        return 2
    elif 400 <= x <= 600 and 0 <= y <= 195:
        return 3
    elif 0 <= x <= 195 and 200 <= y <= 395:
        return 4
    elif 200 <= x <= 395 and 200 <= y <= 395:
        return 5
    elif 400 <= x <= 600 and 200 <= y <= 395:
        return 6
    elif 0 <= x <= 195 and 400 <= y <= 600:
        return 7
    elif 200 <= x <= 395 and 400 <= y <= 600:
        return 8
    elif 400 <= x <= 600 and 400 <= y <= 600:
        return 9


def draw_box(x_turn, box):
    global q, w, e, r, t, y, u, i, o
    if x_turn:
        if box == 1:
            pygame.draw.line(WIN, BLUE, (30, 30), (170, 170), 8)
            pygame.draw.line(WIN, BLUE, (170, 30), (30, 170), 8)
            q = "X"
        elif box == 2:
            pygame.draw.line(WIN, BLUE, (230, 30), (370, 170), 8)
            pygame.draw.line(WIN, BLUE, (370, 30), (230, 170), 8)
            w = "X"
        elif box == 3:
            pygame.draw.line(WIN, BLUE, (430, 30), (570, 170), 8)
            pygame.draw.line(WIN, BLUE, (570, 30), (430, 170), 8)
            e = "X"
        elif box == 4:
            pygame.draw.line(WIN, BLUE, (30, 230), (170, 370), 8)
            pygame.draw.line(WIN, BLUE, (170, 230), (30, 370), 8)
            r = "X"
        elif box == 5:
            pygame.draw.line(WIN, BLUE, (230, 230), (370, 370), 8)
            pygame.draw.line(WIN, BLUE, (370, 230), (230, 370), 8)
            t = "X"
        elif box == 6:
            pygame.draw.line(WIN, BLUE, (430, 230), (570, 370), 8)
            pygame.draw.line(WIN, BLUE, (570, 230), (430, 370), 8)
            y = "X"
        elif box == 7:
            pygame.draw.line(WIN, BLUE, (30, 430), (170, 570), 8)
            pygame.draw.line(WIN, BLUE, (170, 430), (30, 570), 8)
            u = "X"
        elif box == 8:
            pygame.draw.line(WIN, BLUE, (230, 430), (370, 570), 8)
            pygame.draw.line(WIN, BLUE, (370, 430), (230, 570), 8)
            i = "X"
        elif box == 9:
            pygame.draw.line(WIN, BLUE, (430, 430), (570, 570), 8)
            pygame.draw.line(WIN, BLUE, (570, 430), (430, 570), 8)
            o = "X"
    else:
        if box == 1:
            pygame.draw.circle(WIN, RED, (100, 100), 75, 8)
            q = "O"
        elif box == 2:
            pygame.draw.circle(WIN, RED, (300, 100), 75, 8)
            w = "O"
        elif box == 3:
            pygame.draw.circle(WIN, RED, (500, 100), 75, 8)
            e = "O"
        elif box == 4:
            pygame.draw.circle(WIN, RED, (100, 300), 75, 8)
            r = "O"
        elif box == 5:
            pygame.draw.circle(WIN, RED, (300, 300), 75, 8)
            t = "O"
        elif box == 6:
            pygame.draw.circle(WIN, RED, (500, 300), 75, 8)
            y = "O"
        elif box == 7:
            pygame.draw.circle(WIN, RED, (100, 500), 75, 8)
            u = "O"
        elif box == 8:
            pygame.draw.circle(WIN, RED, (300, 500), 75, 8)
            i = "O"
        elif box == 9:
            pygame.draw.circle(WIN, RED, (500, 500), 75, 8)
            o = "O"
    pygame.display.update()


def check_win():
    if q == w == e and q != " ":
        return True, q
    elif r == t == y and r != " ":
        return True, r
    elif u == i == o and u != " ":
        return True, u
    elif q == r == u and q != " ":
        return True, q
    elif w == t == i and w != " ":
        return True, w
    elif e == y == o and e != " ":
        return True, e
    elif q == t == o and q != " ":
        return True, q
    elif e == t == u and e != " ":
        return True, e
    return False, None


def check_draw():
    if (q == " " or w == " " or e == " " or r == " " or t == " " or y == " " or u == " " or i == " " or o == " "):
        return False
    elif check_win()[0]:
        return False
    return True


def main():
    global q, w, e, r, t, y, u, i, o
    clock = pygame.time.Clock()
    run = True
    x_turn = True
    winner = ""
    used_box = []
    q = w = e = r = t = y = u = i = o = " "
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0]:
            x, y = pygame.mouse.get_pos()
            box = get_box(x, y)
            if box not in used_box:
                draw_box(x_turn, box)
                x_turn = not x_turn
                used_box.append(box)
                if check_win()[0]:
                    if check_win()[1] == "X":
                        winner_text = FONT.render(
                            "Player 1 Won!", True, BLACK, GOLD)
                        WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2,
                                 HEIGHT // 2 - winner_text.get_height() // 2))
                    else:
                        winner_text = FONT.render(
                            "Player 2 Won!", True, BLACK, GOLD)
                        WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2,
                                 HEIGHT // 2 - winner_text.get_height() // 2))
                    pygame.display.update()
                    run = False
                    pygame.time.delay(3000)
                elif check_draw():
                    winner_text = FONT.render("Tie!", True, BLACK, GOLD)
                    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width(),
                             HEIGHT // 2 - winner_text.get_height()))
                    pygame.display.update()
                    run = False
                    pygame.time.delay(3000)
    main()


if __name__ == "__main__":
    main()
