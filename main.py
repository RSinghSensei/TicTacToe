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

#Loading the two images, initializing variable with first player move
cross = pygame.transform.scale(pygame.image.load("cross.jpg").convert_alpha(),(250,150))
naught = pygame.transform.scale(pygame.image.load("naughts.png").convert_alpha(),(250,150))
d = cross


def lines():
    pygame.draw.line(screen,(0,0,0),(300,0),(300,600),4)
    pygame.draw.line(screen,(0,0,0),(600,0),(600,600),4)
    pygame.draw.line(screen,(0,0,0),(0,200),(900,200),4)
    pygame.draw.line(screen,(0,0,0),(0,400),(900,400),4)

def game():
    global l1, l2, l3, l4, l5, l6, l7, l8, l9,running,c
    t = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
    for i in t:
        if l1 == l2 == l3 or l1 == l4 == l7 or l1 == l5 == l9 or l2 == l5 == l8 or l3 == l6 == l9 or l3 == l5 == l7 or l4 == l5 == l6 or l7 == l8== l9:
            if t1%2!= 0:
                print("Player 1 Wins!")
            else:
                print("Player 2 Wins!")
            running = False
            break
        if max(t) == 1 and c == 9:
            print("Tie!")
            running = False
            break

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
    h1 = pygame.Rect(0,0,300,200)
    h2 = pygame.Rect(300, 0, 300, 200)
    h3 = pygame.Rect(600, 0, 300, 200)
    h4 = pygame.Rect(0, 200, 300, 200)
    h5 = pygame.Rect(300, 200, 300, 200)
    h6 = pygame.Rect(600, 200, 300, 200)
    h7 = pygame.Rect(0, 400, 300, 200)
    h8 = pygame.Rect(300, 400, 300, 200)
    h9 = pygame.Rect(600, 400, 300, 200)
    pos = pygame.mouse.get_pos()
    if click:
        c+=1
        if h1.collidepoint(pos) and l1 not in j1:
            x,y = 0,0
            turn()
            l1 = j
        if h2.collidepoint(pos) and l2 not in j1:
            x, y= 300,0
            turn()
            l2 = j
        if h3.collidepoint(pos) and l3 not in j1:
            x, y = 600,0
            turn()
            l3 = j
        if h4.collidepoint(pos) and l4 not in j1:
            x, y = 0, 200
            turn()
            l4 = j
        if h5.collidepoint(pos) and l5 not in j1:
            x, y = 300, 200
            turn()
            l5 = j
        if h6.collidepoint(pos) and l6 not in j1:
            x, y = 600, 200
            turn()
            l6 = j
        if h7.collidepoint(pos) and l7 not in j1:
            x, y = 0, 400
            turn()
            l7 = j
        if h8.collidepoint(pos) and l8 not in j1:
            x, y = 300, 400
            turn()
            l8 = j
        if h9.collidepoint(pos) and l9 not in j1:
            x, y = 600, 400
            turn()
            l9 = j


    pygame.draw.rect(screen,(128,128,128),h1,4)
    pygame.draw.rect(screen,(128,128,128),h2,4)
    pygame.draw.rect(screen,(128,128,128),h3,4)
    pygame.draw.rect(screen,(128,128,128),h4,4)
    pygame.draw.rect(screen,(128,128,128),h5,4)
    pygame.draw.rect(screen,(128,128,128),h6,4)
    pygame.draw.rect(screen,(128,128,128),h7,4)
    pygame.draw.rect(screen,(128,128,128),h8,4)
    pygame.draw.rect(screen,(128,128,128),h9,4)



running = True

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
