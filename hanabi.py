import sys
import random
import cv2
import numpy as np
import pygame
 
img_bg = pygame.image.load('image/IMG_0558.png')   
img_char= pygame.image.load('image/IMG_0557.png')                             # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
#img_bg = pygame.transform.scale(img_bg, (1450,4125)) 

def main(): # メインループ
    global img_bg
    global img_char
    global tmr
    global scene
    global ac
    global sc
    global img

    tmr = 0
    scene = 1
    ac = 100
    sc = 1.0

    pygame.init()
    pygame.display.set_caption("アリスの花火")
    screen = pygame.display.set_mode((960, 720))
    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    while True:
        screen.fill((0,0,0))

        tmr = tmr +1 

        #ゲームスタートからの経過時間でのイベントを記述
        if scene == 1:
            if tmr <= 30:
                
                #このシーンの動きの初期化
                ac=100
                atemp=0
                ttmr=0
            elif tmr> 30 and tmr < 100:
                   
                atemp= ac*ttmr
                screen.blit(img_bg, [-180,800-atemp])
                screen.blit(img_char, [-180, 800-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3

            elif tmr <230:
                screen.blit(img_bg, [-180,0])
                screen.blit(img_char, [-180, 800-atemp])     
            else:
                scene = scene +1

        if scene == 2:
            if tmr <= 230:
                #このシーンの動きの初期化
                ac=120
                atemp=0
                ttmr=0
            elif tmr> 230 and tmr < 400:

                atemp= ac*ttmr
                screen.blit(img_bg, [-180,0-atemp])                   
                screen.blit(img_char, [-180, 0-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3

            elif tmr <430:
                screen.blit(img_bg, [-180,0-atemp])
                screen.blit(img_char, [-180, 0-atemp])     
            else:
                scene = scene +1
        if scene == 3:
            if tmr <= 430:
                #このシーンの動きの初期化
                ac=120
                atemp=0
                ttmr=0
            elif tmr> 430 and tmr < 600:

                atemp= ac*ttmr
                screen.blit(img_bg, [-180,-1600-atemp])                   
                screen.blit(img_char, [-180, -1600-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3

            elif tmr <600:
                screen.blit(img_bg, [-180,-1600-atemp])
                screen.blit(img_char, [-180, -1600-atemp])   
                
            elif tmr ==600:
                #このシーンの動きの初期化
                sc=1.0
                ttmr=0
                ac=0
    
            elif tmr <600:
                ac = ac + 5
                img = pygame.transform.scale(img_bg, (1350-ac,4125-ac)) 
                screen.blit(img, [-180,-1600-atemp])
                img = pygame.transform.scale(img_char, (1350-ac,4125-ac))
                screen.blit(img, [-180, -1600-atemp])   
            elif tmr <700:
                img = pygame.transform.scale(img_bg, (1350-ac,4125-ac)) 
                screen.blit(img, [-180,-1600-atemp])
                img = pygame.transform.scale(img_char, (1350-ac,4125-ac))
                screen.blit(img, [-180, -1600-atemp])   
            
            else:
                pygame.quit()
                sys.exit()

        #カウンタ表示                
        text1 = font1.render("TMR:"+str(tmr)+" TTMR:"+str(ttmr)+" AC:"+str(ac), True, (255,0,0))
        screen.blit(text1, (0,0))
        
        #ウィンドクローズで強制終了
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960, 720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        # 星のスクロール

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()



