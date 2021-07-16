import pygame,time,random
BLACK = (0,0,0)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (64, 224, 208)
pygame.init()
width, height = 800, 500
win=pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()
img = pygame.image.load(r'C:\Users\THU TRANG\Downloads\project Flappy bird\bird.jpg')
img_width=img.get_size()[0]
img_height=img.get_size()[1]

def show_score(curent_score):
    font=pygame.font.SysFont('consolas',20)
    text=font.render('Score:'+ str(curent_score),True,WHITE)
    win.blit(text,[3,3])




def blocks(x_block,y_block,block_width,block_height,gap):
    pygame.draw.rect(win,GREEN,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(win,GREEN,[x_block,y_block+block_height+gap,block_width,height])




def maketextobject(text,font):
    textWin=font.render(text,True,WHITE)
    return textWin,textWin.get_rect()



def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            continue
        return event.key
    return None
def msg_win(text):
    smallText = pygame.font.SysFont('consolas',20)
    largeText =pygame.font.SysFont('consolas',130)

    titletextSurf, titleTextRect = maketextobject(text, largeText)
    titleTextRect.center = width / 2, height / 2
    win.blit(titletextSurf, titleTextRect)

    typtextSurf, typTextRect = maketextobject('Press any key to continue', smallText)
    typTextRect.center = width / 2, ((height / 2) + 100)
    win.blit(typtextSurf, typTextRect)
    
    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()

    main()






def game_over():
    msg_win('Game over')



def bird(x,y,image):
    win.blit(image,(x,y))


def main():
    x=150
    y=200
    y_move=0
    x_block=width
    y_block=0
    block_width=50
    block_height=random.randint(0,height/2)
    gap=img_height*5
    block_move=5
    score =0
    gameover =False
    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y = y + y_move

        win.fill(BLUE)
        bird(x, y, img)
        show_score(score)



        if 3 <= score < 5:
            block_move = 6
            gap = img_height * 4

        if 5 <= score < 8:
            block_move = 7
            gap = img_height * 3.3

        if 8 <= score < 14:
            block_move = 8
            gap = img_height * 3

        if score >= 14:
            block_move = 8
            gap = img_height * 2.5

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move


        if y >height - img_height or y < 0:
            game_over()

  
        if x_block < (-1 * block_width):
            x_block = width
            block_height = random.randint(0, height / 2)

    
        if x + img_width > x_block and x < x_block + block_width:
            if y < block_height or y + img_height > block_height + gap:
                game_over()

        if x > x_block + block_width and x < x_block + block_width + img_width / 5:
            score += 1

        pygame.display.update()
        clock.tick(80)
main()
pygame.quit()
quit()


            


    


