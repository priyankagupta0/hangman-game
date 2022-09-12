import math
import pygame
import random
pygame.init() #we are initializing the pygame which is necessary

# colors
WHITE=(255,255,255)
BLACK=(0,0,0) #rgb values
BROWN=(48,8,8)

# fonts
WORD_FONT=pygame.font.SysFont(None,60)
LETTER_FONT=pygame.font.SysFont("script",35)
    
WIDTH,HEIGHT=800,500
bg_img = pygame.image.load('hangman-background.png')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
title=pygame.image.load("title.png")
window =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HANGMAN!")

# images
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+ str(i)+".png")
    images.append(image)

# game variables and words
hangman_status=0
words=["PRIYANKA",'PYTHON','HELLO','LOSER','STUPID','GOODBYE','LOCATE','KEYS','MONEY','DRUGS','KILLER']
word=random.choice(words)
guessed=[]

# button variables
letters=[]
GAP=12
RADIUS=18
WIDTH=800
A=65
startx= 200 #round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty=380
for i in range (26):
    x = startx + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y,chr(A+i), True])

# win or lose message
def won_lose(message):
    pygame.time.delay(2000)
    window.blit(bg_img,(0,0))
    text=WORD_FONT.render( message,1,BLACK)
    window.blit(text,(WIDTH/2- text.get_width()/2, HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    
def play():
    
    # word
    display_word=""
    for letter in word:
        if letter in guessed:
            display_word += letter +" "
        else:
            display_word+="_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    window.blit(text,(350,250))   

    # letters
    for letter in letters:
        [x,y,ltr,visible]=letter
        if visible:
            pygame.draw.circle(window, BROWN, (x,y), 20, 3)
            text= LETTER_FONT.render(ltr,1,BLACK)
            window.blit(text,(x-text.get_width()/2 , y - text.get_height()/2)) #for rendering text in middle

def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        window.blit(bg_img,(0,0))
        window.blit(title,(200,-30))
        window.blit(images[hangman_status],(-49,250))
        MENU_MOUSE_POS=pygame.mouse.get_pos()
        

# game loop
def main():
    # setup game loop
    FPS= 60
    clock=pygame.time.Clock()
    run=True
    global hangman_status

    while run:
        clock.tick(FPS) #to make sure that loop runs at this speed 

        for event in pygame.event.get(): #an event is trigerred whenever user does something like clicking mouse
            # any event that happened is stored in py.evnt.get
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()
                for letter in letters:
                    x,y,ltr, visible=letter
                    if visible:
                        dis= math.sqrt((x-m_x)**2+(y-m_y)**2)
                        if dis < RADIUS:
                            letter[3]=False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status +=1
        
        window.blit(bg_img,(0,0))
        window.blit(title,(200,-30))
        play()  
        window.blit(images[hangman_status],(-49,250))
        pygame.display.update()     
        won=True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            won_lose("you WON!..!!")
            break

        if hangman_status==6:
            won_lose('SIKE YOU LOST')
            won_lose(f"The word was..{word}")
            break
        
main()        
pygame.quit()