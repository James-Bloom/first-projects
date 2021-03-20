import pygame,sys,math
from pygame.locals import *
from tetris_pieces import *
pygame.init()

width = 700
height = 800
tile_size = 30
screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption("tetris")

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
colors = [black,cyan,blue,orange,yellow,green,purple,red]

yp = 0
fps = 60
restart = -1
playing = 0
game_over = 1
game_state = playing
clock = pygame.time.Clock()

def draw_board(board,board_surface):
    for row in range (ROWS):
        for col in range (COLS):
            current_tile = board [row][col]
            tile_x = col*tile_size
            tile_y = row*tile_size
            draw_tile (tile_x,tile_y,current_tile,board_surface)

def draw_tile (posx, posy,tile,surface):
    tile_color = colors[tile]
    rect=Rect((posx,posy),(tile_size,tile_size))
    pygame.draw.rect(surface,tile_color,rect)
    pygame.draw.rect(surface,gray,rect.inflate(1,1),1)

def draw_play_area(screen_position,screen_surface,board_surface):
    rows_to_show=20.5
    topy=board_surface.get_height()-rows_to_show*tile_size
    screen_surface.blit(board_surface,screen_position,Rect((0,  topy),   (board_surface.get_width(),rows_to_show * tile_size)))

def draw_tetrimino (posX,posY,tetrimino,board_surface):
    topX=posX
    topY=posY
    rows = len(tetrimino)
    cols = len(tetrimino[0])
    for row in range (rows):
        for col in range (cols):
            tile = tetrimino [row][col]
            if tile !=0:
                tile_x = (topX + col) * tile_size
                tile_y = (topY + row) * tile_size
                draw_tile(tile_x,tile_y,tile,board_surface)

def calculate_drop_time (level):
    return math.floor(math.pow((0.8 - ((level - 1) * 0.007)), level - 1) * 60)

def lock(posX, posY, grid, tetrimino):
   top_x, top_y = posX, posY
   tetrimino_height = len(tetrimino)
   tetrimino_width = len(tetrimino[0])
   for y in range(tetrimino_height):
       for x in range(tetrimino_width):
           tile = tetrimino[y][x]
           if tile != 0:
               grid[top_y + y][top_x + x] = tile

def check_and_clear_lines(grid):
    lines_cleared = 0
    full_lines = []
    for y,line in enumerate(grid):
        if 0 not in line:
            lines_cleared += 1
            full_lines.append(y)
    if lines_cleared > 0:
        for y in full_lines:
            grid.pop(y)
            grid.insert(0,[0 for _ in range(COLS)])



level = 1
score = 0
drop_clock = 0
current_drop_time = base_drop_time = calculate_drop_time(level)

ROWS = 40
COLS = 10
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
board_surface=pygame.Surface((COLS*tile_size,ROWS*tile_size))

locking = False
lock_clock = 0
lock_delay = 30

active_tetrimino = Tetrimino()
active_tetrimino.grid_ref=board
active_tetrimino.reset()
while True:
    while game_state == playing:
        clock.tick(fps)
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit ()
            elif event.type == KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    active_tetrimino.move(1,0)
                elif event.key == pygame.K_LEFT:
                    active_tetrimino.move (-1,0)
                elif event.key == pygame.K_UP or event.key == pygame.K_x:
                    active_tetrimino.rotate (1)
                elif event.key == pygame.K_z or event.key== pygame.K_RCTRL:
                    active_tetrimino.rotate(-1)
                elif event.key == pygame.K_DOWN:
                    active_tetrimino.move(0,1)
        drop_clock += 1
        if drop_clock >= current_drop_time:
            move = active_tetrimino.move(0,1)
            if not move:
                if not locking:
                    locking = True
                    lock_clock = 0
            else:
                locking = False
            drop_clock = 0
        if locking:
            lock_clock += 1
            if lock_clock >= lock_delay:
                lock(active_tetrimino.x,active_tetrimino.y,board,pieces[active_tetrimino.type][active_tetrimino.rotation])
                drop_clock = base_drop_time
                active_tetrimino.reset()
                lock_clock = 0
                locking = False
                check_and_clear_lines(board)

        screen.fill((gray))
        draw_board (board,board_surface)
        draw_tetrimino(active_tetrimino.x,active_tetrimino.y,pieces[active_tetrimino.type][active_tetrimino.rotation],board_surface)
        draw_play_area((10,10),screen,board_surface)
        pygame.display.update()

