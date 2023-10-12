import sys
import random
import cv2
import numpy as np
import pygame
 
img_bg = pygame.image.load('image/IMG_0558.png')   
img_char= pygame.image.load('image/IMG_0557.png')                             # -1はAlphaを含んだ形式(0:グレー, 1:カラー)


def main(): # メインループ
    global img_bg
    global tmr
    global scene
    global ac

    tmr = 0
    scene = 1
    ac = 100

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
                img_bg = pygame.transform.scale(img_bg, (1450,4125)) 
                screen.blit(img_bg, [-150,0])  
                #このシーンの動きの初期化
                ac=100
                atemp=0
                ttmr=0
            elif tmr> 30 and tmr < 100:

                
                img_bg = pygame.transform.scale(img_bg, (1450,4125)) 
                screen.blit(img_bg, [-150,0])
                    
                atemp= ac*ttmr
                #if 800-atemp < 0: atemp = 800
                screen.blit(img_char, [-180, 800-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3

            elif tmr <200:
                screen.blit(img_bg, [-150,0])
                screen.blit(img_char, [-180, 0])     
            else:
                scene = scene +1

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
        clock.tick(10)

if __name__ == '__main__':
    main()



