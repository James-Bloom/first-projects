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
cloud_1_xp=100
cloud_2_xp=240
cloud_3_xp=427
moon_xp=580
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()
    screen.fill((blue))
    pygame.draw.rect(screen, brown, (width / 2.6, height / 1.6, 50, 80))
    pygame.draw.rect(screen, brick, (width / 3.2, height / 3.4, 40, 60))
    pygame.draw.rect(screen, gray, (width / 3, height / 5, 15, 15))
    pygame.draw.rect(screen, gray, (width / 3.5, height / 4, 15, 15))
    pygame.draw.rect (screen,brown,(width/2,height/2,tile_size,150))
    pygame.draw.rect(screen, brown, (width / 4, height / 2, 20, 150))
    pygame.draw.rect(screen, brown, (width / 2.13, height / 2.18, 20, 20))
    pygame.draw.rect(screen, brown, (width / 2.26, height / 2.360, 20, 20))
    pygame.draw.rect(screen, brown, (width / 2.45, height / 2.62, 20, 20))
    pygame.draw.rect(screen, brown, (width / 3.55, height / 2.18, 20, 20))
    pygame.draw.rect(screen, brown, (width / 3.18, height / 2.39, 20, 20))
    pygame.draw.rect(screen, brown, (width / 2.89, height / 2.64, 20, 20))
    pygame.draw.rect(screen, brown, (width / 2.65, height / 2.9, 20, 20))
    pygame.draw.rect(screen, black, (width / 2.35, height / 1.45, 14, 15))
    pygame.draw.rect(screen, green, (width / 25, height / 1.28, 750, 120))
    pygame.draw.rect(screen, brown, (width / 1.5, height / 2.1, 30, 150))
    pygame.draw.rect(screen, green, (width / 1.65, height / 3.5, 150, 130))
    pygame.draw.rect(screen, gray, (width / 1.21, height / 1.8, 10, 80))
    pygame.draw.rect(screen, gray, (width / 1.3, height / 1.8, 10, 80))
    pygame.draw.rect(screen, brown, (width / 1.3, height / 1.4, 46, 10))
    pygame.draw.rect(screen, gray, (width / 2.8, height / 4.3, 15, 15))
    pygame.draw.rect(screen, brown, (width / 14, height / 1.44, 15, 45))
    pygame.draw.rect(screen, brown, (width / 5, height / 1.44, 15, 45))
    pygame.draw.rect(screen, brown, (width / 14, height / 1.45, 97, 15))
    for x in range(0, 2):
        yp = yp + -.8
        cloud_1_xp = cloud_1_xp + -.8
        cloud_2_xp = cloud_2_xp + -.8
        cloud_3_xp = cloud_3_xp + -.8
        moon_xp = moon_xp + -.8
        pygame.draw.rect(screen, (white), (cloud_1_xp, 77, 80, 30))
        pygame.draw.rect(screen, (white), (cloud_2_xp, 57, 80, 30))
        pygame.draw.rect(screen, (white), (cloud_3_xp, 60, 80, 30))
        pygame.draw.rect(screen, (yellow), (yp, 55, 80, 80))
        pygame.display.update()
