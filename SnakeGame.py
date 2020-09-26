import pygame
import random
import time
pygame.init()

width=800
height=600

screen =pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super(Snake,self).__init__()
        self.surf=pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()

    def update(self,pressed):
        if pressed[pygame.K_UP]:
            self.rect.move_ip(0,-5)

        if pressed[pygame.K_DOWN]:
            self.rect.move_ip(0,5)

        if pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

        if pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)



x1=200
y1=150

x=0
y=0
snake=Snake()

def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (255,255,0), [x[0], x[1], 10, 10])

running=True

clock=pygame.time.Clock()


def gameLoop():
    running = True
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x = 0
    y = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, width - 10) / 10.0) * 10.0

    while running:

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                elif event.key==pygame.K_w:
                    y = -10
                    x = 0
                elif event.key==pygame.K_s:
                    y = 10
                    x = 0
                elif event.key==pygame.K_a:
                    x = -10
                    y = 0
                elif event.key==pygame.K_d:
                    x = 10
                    y = 0


            elif event.type==pygame.QUIT:
                running=False



        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            #pass
            running = False

        x1+=x
        y1+=y

        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,0,0), [foodx, foody, 10, 10])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for xx in snake_List[:-1]:
            if xx == snake_Head:
                running = True

        our_snake(snake_List)

        pygame.display.update()
        # pygame.display.flip()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, height - 10) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(15)


    time.sleep(2)
    pygame.quit()
gameLoop()
