import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,600))
screen.fill((255, 253, 208))
pygame.display.set_caption("Tic Tac Toe")

#Vars concerning array values for game logic, turn to 0's and 1's ultimately
l1, l2, l3, l4, l5, l6, l7, l8, l9 = 18, 19, 20, 21, 22, 23, 24, 25, 26
t1,j,c,s = 0,0,0,0
x,y = 0,0
j1 = [0,1]


#Loading menu buttons
font = pygame.font.Font("Pixeboy-z8XGD.ttf", 64)
fontB = pygame.font.Font("Pixeboy-z8XGD.ttf",80)


#Loading the two images, initializing variable with first player move
cross = pygame.transform.scale(pygame.image.load("Transparent_X.png"),(250,200))
naught = pygame.transform.scale(pygame.image.load("circle.png"), (250, 200))
d = cross

def menu():
    global running, Menu, click1
    pos1 = pygame.mouse.get_pos()
    p_Text = font.render("PLAY",True,(0,0,0))
    q_Text = font.render("QUIT",True,(0,0,0))
    main_Title = font.render("TIC-TAC-TOE!",True,(0,0,0))
    play_Button = pygame.draw.rect(screen,(0,0,0),(125,400,267,100),4)
    quit_Button = pygame.draw.rect(screen,(0,0,0),(500,400,267,100),4)
    screen.blit(p_Text,(195,420))
    screen.blit(q_Text,(570,420))
    screen.blit(main_Title,(285,150))
    if click1:
        if play_Button.collidepoint(pos1):
            Menu = False
            running = True
            screen.fill((255, 253, 208))
        if quit_Button.collidepoint(pos1):
            Menu = False

def play_again():
    global running, l1, l2, l3, l4, l5, l6, l7, l8, l9, t1, j, c, s, x, y, j1
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = 18, 19, 20, 21, 22, 23, 24, 25, 26
    t1, j, c, s = 0, 0, 0, 0
    x, y = 0, 0
    j1 = [0, 1]

    screen.fill((255,253,208))
    PlayAgain = True
    running = False

    w_text = fontB.render(w, True, (0, 0, 0))
    play_text = font.render("Press R to restart", True, (0, 0, 0))
    if w != "Tie!":
        screen.blit(w_text, (230, 150))
    else:
        screen.blit(w_text, (375,150))
    screen.blit(play_text, (215, 400))

    while PlayAgain:
        k = pygame.key.get_pressed()
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                PlayAgain = False
                pygame.quit()
        if k[pygame.K_r]:
            PlayAgain = False
            running = True
            screen.fill((255,253,208))
        pygame.display.update()

def lines():
    pygame.draw.line(screen,(0,0,0),(300,0),(300,600),4)
    pygame.draw.line(screen,(0,0,0),(600,0),(600,600),4)
    pygame.draw.line(screen,(0,0,0),(0,200),(900,200),4)
    pygame.draw.line(screen,(0,0,0),(0,400),(900,400),4)

def game():
    global l1, l2, l3, l4, l5, l6, l7, l8, l9,running,c,w
    t = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
    for i in t:
        if l1 == l2 == l3 or l1 == l4 == l7 or l1 == l5 == l9 or l2 == l5 == l8 or l3 == l6 == l9 or l3 == l5 == l7 or l4 == l5 == l6 or l7 == l8== l9:
            if t1%2!= 0:
                w = "Player 1 Wins!"
                play_again()
                break
                # print("Player 1 Wins!")
            else:
                w = "Player 2 Wins!"
                play_again()
                break
                # print("Player 2 Wins!")
            # running = False
            # break
        if max(t) == 1 and c == 9:
            w = "Tie!"
            play_again()
            break
            # print("Tie!")
            # running = False
            # break


def turn():
    global t1,j,d
    t1+=1
    if t1%2 != 0:
        j = 1
        d = cross
    else:
        j = 0
        d = naught


def boxes():
    global l1, l2, l3, l4, l5, l6, l7, l8, l9, x, y, c, j1

    h1 = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, 200), 4)
    h2 = pygame.draw.rect(screen, (0, 0, 0), (300, 0, 300, 200), 4)
    h3 = pygame.draw.rect(screen, (0, 0, 0), (600, 0, 300, 200), 4)
    h4 = pygame.draw.rect(screen, (0, 0, 0), (0, 200, 300, 200), 4)
    h5 = pygame.draw.rect(screen, (0, 0, 0), (300, 200, 300, 200), 4)
    h6 = pygame.draw.rect(screen, (0, 0, 0), (600, 200, 300, 200), 4)
    h7 = pygame.draw.rect(screen, (0, 0, 0), (0, 400, 300, 200), 4)
    h8 = pygame.draw.rect(screen, (0, 0, 0), (300, 400, 300, 200), 4)
    h9 = pygame.draw.rect(screen, (0, 0, 0), (600, 400, 300, 200), 4)

    pos = pygame.mouse.get_pos()
    if click:
        c+=1
        if h1.collidepoint(pos) and l1 not in j1:
            x,y = 25,0
            turn()
            l1 = j
        if h2.collidepoint(pos) and l2 not in j1:
            x, y= 325,0
            turn()
            l2 = j
        if h3.collidepoint(pos) and l3 not in j1:
            x, y = 625,0
            turn()
            l3 = j
        if h4.collidepoint(pos) and l4 not in j1:
            x, y = 25, 200
            turn()
            l4 = j
        if h5.collidepoint(pos) and l5 not in j1:
            x, y = 325, 200
            turn()
            l5 = j
        if h6.collidepoint(pos) and l6 not in j1:
            x, y = 625, 200
            turn()
            l6 = j
        if h7.collidepoint(pos) and l7 not in j1:
            x, y = 25, 400
            turn()
            l7 = j
        if h8.collidepoint(pos) and l8 not in j1:
            x, y = 325, 400
            turn()
            l8 = j
        if h9.collidepoint(pos) and l9 not in j1:
            x, y = 625, 400
            turn()
            l9 = j





running = False
Menu = True
click1 = False

while Menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click1 = True
    menu()
    pygame.display.update()


while running:
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    lines()
    boxes()
    game()
    if t1!=0:
        screen.blit(d, (x, y))
    pygame.display.update()
