import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Creating colors and variables
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 174, 201)
pp = False
t = False
start_time = 0
blink_start = 0
blink_interval = 537
blinks = 2
blink_active = False

#Other Variables for use in the program
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 2180
SPEED = 30
SCORE = 0
KROMER = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 120)
font_small = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, RED)
big = font.render("BIG", True, PINK)
shot = font.render("SHOT!", True, YELLOW)

background = pygame.image.load("AnimatedStreet.jpg")

#Create a white screen 
screen = pygame.display.set_mode((1080,2180))
screen.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(240, SCREEN_WIDTH-240), 0)  

      def move(self):
        global SCORE
        global KROMER
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 1980):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(240, 720), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(200, 950), 0)

    def move(self):
        self.rect.move_ip(0, 0.9 * SPEED - 10)

        if self.rect.top > 1980:
            self.kill()
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (760, 1700)
        self.direction = 1
        self.moving = False
        self.pipis = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.direction *= -1
            self.moving = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.moving = False
            
    def move(self):
        if self.moving and self.pipis:
            self.rect.move_ip(self.direction * (SPEED - 10), 0)
            if self.rect.left < 0:
                  self.rect.left = 0
            if self.rect.right > 1080:
                  self.rect.right = 1080
                  
#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 4500 - SPEED * 5)

#Game Loop
while True:
      
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.67
        if event.type == SPAWN_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        P1.handle_event(event)

    screen.blit(background, (0,0))
    
    #Displaying the score and coins
    scores = font_small.render("score: " + str(SCORE), True, BLACK)
    kromer = font_small.render("coins: " + str(KROMER), True, YELLOW)
    screen.blit(scores, (800,100))
    screen.blit(kromer, (800,200))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('splat.mp3').play()
          time.sleep(0.5)
                   
          screen.fill(BLACK)
          screen.blit(game_over, (250,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(0.67)
          pygame.quit()
          sys.exit()        
        
      # Collecting coins and playing the sound effect
    collected = pygame.sprite.spritecollide(P1, coins, True)
    if collected:
    	KROMER  += len(collected)
    	if KROMER != 0 and KROMER % 4 == 0 and not t:
    		start_time = pygame.time.get_ticks()
    		pygame.mixer.Sound('insanity.mp3').play()
    		pp = True
    		t = True
    		blink_start = pygame.time.get_ticks()
    		blink_active = True
    	elif KROMER < 5:
    	    pygame.mixer.Sound('kromer_received.mp3').play()
    	    t = False
    	elif KROMER >= 5:
    		  pygame.mixer.Sound('evil_kromer_received.mp3').play()
    		  t = False
    if pp:
      current_time = pygame.time.get_ticks()
      dr = current_time - start_time
      if blink_active:
          blink_dr = current_time - blink_start
          phase = blink_dr // blink_interval

          if phase < blinks * 2:
              if phase % 2 == 0:
                  screen.blit(big, (250, 500))
                  screen.blit(shot, (500, 500))
          else:
              blink_active = False
      else:
          pass

      if dr >= 1997:
          pp = False
    pygame.display.update()
    pygame.time.Clock().tick(60)