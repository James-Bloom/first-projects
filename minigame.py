import pygame,sys,random,time

width = 700
height = 700
screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption("minigame")

cyan=(0,255,255)
brown = (156,102,31)
blue = (152,245,255)
white = (248,248,255)
brick = (210,105,30 )
gray =(128,138,135)
black = (0,0,0)
yellow=(255,246,143)
green=(69,139,0)
purple=(160,32,240)
red=(255,0,0)
orange = (255,100,10)
color1 = 245
color2= 255
color3 = 152
rectx = width/2
rect_change_x = 0
recty = height/2
rect_change_y = 0
right_down = False
left_down = False
up_down = False
down_down = False

draw_circle = False
circlex = -100
circley = -100
circleheight = 0
circlewidth =  0
rectwidth = 20
rectheight = 20
shift = False
score = 0
spawned = 0
circle_erased = False
c1 = 100
c2 = 100
c3 = 100
boss_mode = False
clock = pygame.time.Clock()
turn = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                rect_change_x = 1
                right_down = True
            if event.key == pygame.K_LEFT:
                rect_change_x = -1
                left_down = True
            if event.key == pygame.K_UP:
                rect_change_y = -1
                up_down = True
            if event.key == pygame.K_DOWN:
                down_down = True
                rect_change_y = 1
            if event.key == pygame.K_SPACE:
                color3 = random.randint(0,255)
                color2 = random.randint(0, 255)
                color1 = random.randint(0, 255)
            if event.key == pygame.K_LSHIFT:
                shift = True

            """
            if event.key == pygame.K_c:
                (c1,c2,c3) = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
                circleheight = 20
                circlewidth = 20
                circley = random.randint(0,height-circleheight)
                circlex = random.randint(0,width-circlewidth )
                spawned += 1
                draw_circle = True
            """
            if event.key == pygame.K_g:
                number = random.randint(0,1)
                if number == 0:
                    circlewidth = random.randint(0,100)
                    circleheight = random.randint(0, 100)
                else:
                    rectwidth = random.randint(0, 100)
                    rectheight = random.randint(0, 100)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
                right_down = False
                left_down = False
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0
                up_down = False
                down_down = False
            if event.key == pygame.K_LSHIFT:
                shift = False

    if shift and (left_down or right_down):
        rectx += rect_change_x * 2
    else:
        rectx += rect_change_x
    if shift and (up_down or down_down):
        recty += rect_change_y*2
    else:
        recty += rect_change_y
    screen.fill(black)
    if rectx <= 0:
        rectx = 0
    if rectx >= width - rectwidth:
        rectx = width-rectwidth
    if recty <= 0:
        recty = 0
    if recty >= height - rectheight:
        recty = height-rectheight
    if pygame.time.get_ticks() / 7000 >= turn:
        turn += 1
        (c1, c2, c3) = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circleheight = 20
        circlewidth = 20
        circley = random.randint(0, height - circleheight)
        circlex = random.randint(0, width - circlewidth)
        spawned += 1
        draw_circle = True

    if draw_circle and not boss_mode:
        pygame.draw.ellipse(screen, (c1,c2,c3), (circlex, circley, circlewidth, circleheight))
    elif boss_mode and draw_circle:
        circlex = (width/2)-(circlewidth/2)
        circley = (height/2)-(circleheight/2)
        circlewidth = width/4
        circleheight = height/4
        (c1,c2,c3) = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.ellipse(screen, (c1, c2, c3), (circlex, circley, circlewidth, circleheight))


    pygame.draw.rect(screen, (color1,color2,color3), (rectx, recty, rectwidth, rectheight))
    if rectx >= circlex - rectwidth and rectx <= circlex + circlewidth and recty >= circley - rectheight and recty <= circley + circleheight :
        if boss_mode:
            score += 1001
            rectwidth *= 2.5
            rectheight *= 2.5
            boss_mode = False
        else:
            rectwidth *= 1.1
            rectheight *= 1.1
            score += 1
        (color1,color2,color3) = (c1,c2,c3)
        draw_circle = False
        print (score)
        #circle_erased = True
        circlex = -100
        circley = -100
        circleheight = 0
        circlewidth = 0
    if score % 5 == 0 and score != 0:
        boss_mode = True
    clock.tick()
    print (pygame.time.get_ticks())
    if width <= rectwidth and height <= rectheight:
        pygame.quit()
        sys.exit()
    pygame.display.update()