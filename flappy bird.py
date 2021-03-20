import pygame,sys
width = 640
height = 480
tile_size = 20
screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption("tetris")
brown = (156,102,31)
blue = (152,245,255)
white = (248,248,255)
brick = (210,105,30 )
gray =(128,138,135)
black = (0,0,0)
yellow = (255,246,143)
green=(69,139,0)
yp = 600
y=30
yvel=10
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()
    screen.fill((blue))
    pygame.draw.rect(screen, brown, (width / 2, height / y, 20, 20))
    y =+ yvel+1
    yvel = yvel-1
    pygame.display.update()
    if y == 0:
        yvel=yvel+2
    if yvel == 0:
        yvel = yvel + 2
#while True:
