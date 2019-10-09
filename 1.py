import pygame
import time
import random

pygame.init()
crash_sound =pygame.mixer.Sound('Crash_Steel_Pipe.wav')
pygame.mixer.music.load('Silent_Observer.mp3')
display_width=800
display_height=550
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodeger runner')
clock=pygame.time.Clock()

background= pygame.image.load('bck.jpg')
backcrash=pygame.image.load('123.jpg')
Green=(5,100,5)
brightGreen=(10,150,10)
Red=(200,0,0)
BrightRed=(255,10,5)
blue=(169,169,169)
navy=(0,0,130)
Black=(0,0,0)
player_img =pygame.image.load('11.png')
player_img1 =pygame.image.load('22.png')
player_icon =pygame.image.load('22 - Copy.png')
pygame.display.set_icon(player_icon)
car_width =50
pause=False
def check(x,y,thing_startX,thing_startY,thing_width,thing_height):
    if y<thing_startY+thing_height:
            if x> thing_startX and x<thing_startX+thing_width or x+car_width >thing_startX and x+car_width<thing_startX+thing_width:
                crash()
def thing_dodged(count):
    font=pygame.font.SysFont('comicsansms',30)
    text=font.render("Dodged: "+str(count),True,Green)
    gameDisplay.blit(text,(0,0))
def things(thingX,thingY,thingW,thingH,color):
    pygame.draw.rect(gameDisplay,color,[thingX,thingY,thingW,thingH])
    
def chac(x,y,st):
    if st==1:
        gameDisplay.blit(player_img,(x-20,y))
    else:
        gameDisplay.blit(player_img1,(x-20,y))
        
def text_objects(text,font):
    textSurface =font.render(text, True, navy)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.SysFont('comicsansms',60)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(backcrash,(90,50))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.SysFont('comicsansms',60)
        TextSurf, TextRect = text_objects('You_Died',largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        #print(mouse)
        button("Play Again",150,350,100,50,Green,brightGreen,gameloop)
        button("Quit",550,350,100,50,Red,BrightRed,pygamequit)
        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,i,a,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w >mouse[0]>x and y+h >mouse[1]>y:
        pygame.draw.rect(gameDisplay,a,(x,y,w,h))
        if click[0]==1 and action !=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,i,(x,y,w,h))

    smallText =pygame.font.SysFont('comicsansms',20)
    textSurf,textRect =text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    
def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)
        largeText = pygame.font.SysFont('comicsansms',60)
        TextSurf, TextRect = text_objects('Paused',largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(TextSurf,TextRect)

        #print(mouse)
        button("Resume",150,350,100,50,Green,brightGreen,unpaused)
        button("Quit",550,350,100,50,Red,BrightRed,pygamequit)
        pygame.display.update()
        clock.tick(15)

def game_into():
    pygame.mixer.music.play(-1)
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)
        largeText = pygame.font.SysFont('comicsansms',60)
        TextSurf, TextRect = text_objects('Block doger',largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(TextSurf,TextRect)

        #print(mouse)
        button("Go!",150,350,100,50,Green,brightGreen,gameloop)
        button("Quit",550,350,100,50,Red,BrightRed,pygamequit)
        pygame.display.update()
        clock.tick(15)
        
def pygamequit():
    pygame.quit()
    quit()
def gameloop():
    global pause
    pygame.mixer.music.play(-1)
    x=(display_width *0.45)
    y=(display_height *0.8)+10
    x_change = 0
    thing_startX = random.randrange(0,display_width)
    thing_startY = -600
    thing_speed =3
    thing_height=80
    thing_width=60
    dodged = 0
    op=0
    op1=1
    rst=30
    obj=0
    obj1=0
    flag=0
    GameExit=False
    st=0
    while not GameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -4
                    st=1
                elif event.key == pygame.K_RIGHT:
                    x_change =4
                    st=0
                elif event.key == pygame.K_SPACE or pygame.K_p:
                    pause=True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        gameDisplay.fill(blue)
        gameDisplay.blit(background,(0,0))

        things(thing_startX,thing_startY,thing_width,thing_height,navy)
        thing_startY+=thing_speed
        chac(x,y,st)
        thing_dodged(dodged)
        if x>display_width - car_width or x<-25:
            crash()
        if obj==1:
            things(op,thing_startY,thing_width,thing_height+20,Red)
            check(x,y,op,thing_startY,thing_width,thing_height+20)
            
        if  obj1==1:
            if flag%3==0:
                rst= random.randrange(30,150)
                flag=0
            things(op1,thing_startY,rst,thing_height+30,Black)
            check(x,y,op1,thing_startY,rst,thing_height+30)
            flag+=1
        if thing_startY >display_height:
            thing_startY=0-thing_height
            thing_startX=random.randrange(0,display_width)
            op=random.randrange(0,display_width)
            op1=random.randrange(0,display_width)
            dodged+=1
            if dodged==3:
                obj=1
            if dodged==8:
                obj1=1
            thing_speed+=0.5
        check(x,y,thing_startX,thing_startY,thing_width,thing_height)
        


        pygame.display.update()
        clock.tick(60)
game_into()
gameloop()
pygame.quit()
quit()
