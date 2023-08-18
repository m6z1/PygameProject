import pygame
import random
import sys
import time

#초기화 #중요!
pygame.init() 

#색상
white = (255, 255, 255)

#이미지
titleImage = pygame.image.load("image/title.jpg")
startImage = pygame.image.load("image/start.png")
quitImage  = pygame.image.load("image/quit.png")
clickstartImage = pygame.image.load("image/clickstart.png")
clickquitImage  = pygame.image.load("image/clickquit.png")
background = pygame.image.load("image/background.jpg")
snowmanImage = pygame.image.load("image/snowman.png")
iceImage = pygame.image.load("image/ice.jpg")
bgmOn = pygame.image.load("image/soundOn.jpg")
bgmOff = pygame.image.load("image/soundX.jpg")
delete = pygame.image.load("image/delete.jpg")

#bgm
icebgm = pygame.mixer.Sound("icebgm.mp3")
backbgm = pygame.mixer.Sound("backgroundbgm.mp3")

#화면 설정
screenWidth = 700 #가로크기
screenHeight = 800 #세로크기
screen = pygame.display.set_mode((screenWidth,screenHeight))  #가로, 세로
pygame.display.set_caption("눈사람은 비가 싫어! 20211039 손명지")

#폰트 설정
Big_font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 40)

#시간
clock = pygame.time.Clock()

#버튼 객체
class Button:
    def __init__(self,img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in, (x,y))
            
            
            
#배경화면
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        screen.blit(bg_img, (bg_x, bg_y))


#게임 나가기
def quitgame():
    pygame.quit()
    sys.exit()
    

#배경음악멈춤 버튼
def bgmoff():
    screen.blit(delete, (650,0))
    backbgm.stop()
    screen.blit(bgmOff, (600,0))
    
#처음화면
def mainmenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        titletext = screen.blit(titleImage, (0, 0))
        startButton = Button(startImage, 100, 300, 100, 50, clickstartImage, 110, 350, gameScreen)
        quitButton = Button(quitImage, 400, 300, 100, 50, clickquitImage, 410, 350, quitgame)
        BGM = Button(bgmOn, 600, 0, 100, 77, bgmOff, 600, 0, bgmoff)
        pygame.display.update()
        clock.tick(15)
        
#충돌 처리
def text_drop(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()


#충돌 메시지
def chungdol(text):
    Big_font = pygame.font.SysFont("malgungothic", 40)
    TextSurf = Big_font.render(text, True, white)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((screenWidth / 2), (screenHeight / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameScreen()
    

#bgm on!
backbgm.play(-1) #무한재생



#게임화면
def gameScreen():
    dt = clock.tick(20)

    
    #눈사람 
    snowmanImage = pygame.image.load("image/snowman.png")
    snowmanSize = snowmanImage.get_rect().size  #img크기 불러옴
    snowmanWidth = snowmanSize[0]
    snowmanHeight = snowmanSize[1]
    snowmanXpos = (screenWidth / 2) - (snowmanWidth / 2)
    snowmanYpos = screenHeight - snowmanHeight
    snowmanSpeed = 10
    
    #비1 설정
    rainImage1 = pygame.image.load("image/rain.png")
    rainy1Size = rainImage1.get_rect().size
    rainy1Width = rainy1Size[0]
    rainy1Height = rainy1Size[1]
    rainy1Xpos = 200
    rainy1Ypos = 0
    rainy1Speed = 5
    
    #비2 설정
    rainImage2 = pygame.image.load("image/rain.png")
    rainy2Size = rainImage2.get_rect().size
    rainy2Width = rainy2Size[0]
    rainy2Height = rainy2Size[1]
    rainy2Xpos = 100
    rainy2Ypos = 0
    rainy2Speed = 7
    
    #비3 설정
    rainImage3 = pygame.image.load("image/rain.png")
    rainy3Size = rainImage3.get_rect().size
    rainy3Width = rainy3Size[0]
    rainy3Height = rainy3Size[1]
    rainy3Xpos = 700
    rainy3Ypos = 0
    rainy3Speed = 10
    
    #비4 설정
    rainImage4 = pygame.image.load("image/rain.png")
    rainy4Size = rainImage4.get_rect().size
    rainy4Width = rainy4Size[0]
    rainyHeight = rainy4Size[1]
    rainy4Xpos = 666
    rainy4Ypos = 0
    rainy4Speed = 9
    
    #비5 설정
    rainImage5 = pygame.image.load("image/rain.png")
    rainy5Size = rainImage5.get_rect().size
    rainy5Width = rainy5Size[0]
    rainy5Height = rainy5Size[1]
    rainy5Xpos = 400
    rainy5Ypos = 0
    rainy5Speed = 8
    
    #비6 설정
    rainImage6 = pygame.image.load("image/rain.png")
    rainy6Size = rainImage6.get_rect().size
    rainy6Width = rainy6Size[0]
    rainy6Height = rainy6Size[1]
    rainy6Xpos = 199
    rainy6Ypos = 0
    rainy6Speed = 6
    
    #얼음 설정
    iceeSize = iceImage.get_rect().size
    iceeWidth = iceeSize[0]
    iceeHeight = iceeSize[1]
    iceeXpos = 500
    iceeYpos = 0
    iceeSpeed = 10
    

    #좌우로 움직이자
    x_change = 0

    #점수 초기화
    score = 0

    totalTime = 50
    
    
    gameexit = False
    while not gameexit:
        #게임 플레이 시간
        startTicks = pygame.time.get_ticks()

        #배경화면 지정
        bg = Background(background, 0, 0)

        #눈사람 불러오기
        screen.blit(snowmanImage, (snowmanXpos, snowmanYpos))

        
        #비 불러오기
        screen.blit(rainImage1, (rainy1Xpos, rainy1Ypos))
        screen.blit(rainImage2, (rainy2Xpos, rainy2Ypos))
        screen.blit(rainImage3, (rainy3Xpos, rainy3Ypos))
        screen.blit(rainImage4, (rainy4Xpos, rainy4Ypos))
        screen.blit(rainImage5, (rainy5Xpos, rainy5Ypos))       
        screen.blit(rainImage6, (rainy6Xpos, rainy6Ypos))

        #얼음 불러오기
        screen.blit(iceImage, (iceeXpos, iceeYpos))

        #좌우로 움직이기
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= snowmanSpeed
                if event.key == pygame.K_RIGHT:
                    x_change += snowmanSpeed

            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        snowmanXpos += x_change

        #경계
        if snowmanXpos < 0:
            snowmanXpos = 0
        elif snowmanXpos > screenWidth - snowmanWidth:
            snowmanXpos = screenWidth - snowmanWidth


        randomNum2 = random.randrange(1, 790)

        #drop 재생 + 점수 올리기
        if rainy1Ypos > screenHeight:
            rainy1Ypos = 0
            rainy1Xpos = randomNum2
            score += 1
            rainy1Speed += 0.1
            
        if rainy2Ypos > screenHeight:
            rainy2Ypos = 0
            rainy2Xpos = randomNum2
            score += 1
            rainy2Speed += 0.1
            
        if rainy3Ypos > screenHeight:
            rainy3Ypos = 0
            rainy3Xpos = randomNum2
            score += 1
            rainy3Speed += 0.1

        if rainy4Ypos > screenHeight:
            rainy4Ypos = 0
            rainy4Xpos = randomNum2
            score += 1
            rainy4Speed += 0.1


        if rainy5Ypos > screenHeight:
            rainy5Ypos = 0
            rainy5Xpos = randomNum2
            score += 1
            rainy5Speed += 0.1

        if rainy6Ypos > screenHeight:
            rainy6Ypos = 0
            rainy6Xpos = randomNum2
            score += 1
            rainy6Speed += 0.1

        if iceeYpos > screenHeight:
            iceeYpos = 0
            iceeXpos = randomNum2
            
        #낙하속도
        rainy1Ypos += rainy1Speed
        rainy2Ypos += rainy2Speed
        rainy3Ypos += rainy3Speed
        rainy4Ypos += rainy4Speed
        rainy5Ypos += rainy5Speed
        rainy6Ypos += rainy6Speed
        iceeYpos += iceeSpeed


        #충돌
        snowmanRect = snowmanImage.get_rect()
        snowmanRect.left = snowmanXpos
        snowmanRect.top = snowmanYpos

        rainy1Rect = rainImage1.get_rect()
        rainy1Rect.left = rainy1Xpos
        rainy1Rect.top = rainy1Ypos

        rainy2Rect = rainImage2.get_rect()
        rainy2Rect.left = rainy2Xpos
        rainy2Rect.top = rainy2Ypos

        rainy3Rect = rainImage3.get_rect()
        rainy3Rect.left = rainy3Xpos
        rainy3Rect.top = rainy3Ypos

        rainy4Rect = rainImage4.get_rect()
        rainy4Rect.left = rainy4Xpos
        rainy4Rect.top = rainy4Ypos

        rainy5Rect = rainImage5.get_rect()
        rainy5Rect.left = rainy5Xpos
        rainy5Rect.top = rainy5Ypos

        rainy6Rect = rainImage6.get_rect()
        rainy6Rect.left = rainy6Xpos
        rainy6Rect.top = rainy6Ypos
        
        iceeRect = iceImage.get_rect()
        iceeRect.left = iceeXpos
        iceeRect.top = iceeYpos
        
        if snowmanRect.colliderect(rainy1Rect):
            chungdol("나는 비가 싫어..")
        if snowmanRect.colliderect(rainy2Rect):
            chungdol("나 녹는다 아이스크림 돼")
        if snowmanRect.colliderect(rainy3Rect):
            chungdol("나 울어..")
        if snowmanRect.colliderect(rainy4Rect):
            chungdol("비는 피해줘ㅜㅜ")
        if snowmanRect.colliderect(rainy5Rect):
            chungdol("ㅠ_ㅠ")
        if snowmanRect.colliderect(rainy6Rect):
            chungdol("섭섭해..")
        if snowmanRect.colliderect(iceeRect):
            icebgm.play()
            iceeYpos = -10
            iceeXpos = randomNum2
            score += 3

        #점수 표시
        scoree = small_font.render(str(score), True, (225,225,225))
        screen.blit(scoree, (55,50))

        #타이머 표시
        elapsedTime = (pygame.time.get_ticks()) / 1000
        timer = small_font.render(str(int(totalTime - elapsedTime)), True, (255, 255, 255))
        screen.blit(timer, (100,50))

        if totalTime - elapsedTime <= 0:
            print("게임 종료")
            gameexit = True
        
        pygame.display.update()
        clock.tick(20)
        

mainmenu()
gameScreen()
