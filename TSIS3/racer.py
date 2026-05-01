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
blink_interval = 567
blinks = 2
blink_active = False

#Other Variables for use in the program
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 2180
SPEED = 70
SCORE = 0
KROMER = 0
BIG_SHOT_ENEMY_SPEED = 0
SLOW_DOWN_SPEED = 0
LAST_KROMER = 0
SHIELD = False
Nitro = False
nitro_start = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 120)
font_small = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, RED)
big = font.render("BIG", True, PINK)
shot = font.render("SHOT!", True, YELLOW)

background = pygame.image.load("assets/AnimatedStreet.jpg")

#Create a white screen 
screen = pygame.display.set_mode((1080,2180))
screen.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(240, SCREEN_WIDTH-240), 0)  
        self.slowed = 0

      def move(self):
        global SCORE
        global BIG_SHOT_ENEMY_SPEED
        global SLOW_DOWN_ENEMY
        a = SLOW_DOWN_SPEED
        self.rect.move_ip(0,SPEED + BIG_SHOT_ENEMY_SPEED - self.slowed)
        if (self.rect.top > 1980):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(240, 720), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        a = random.randint(1, 1000)
        if a < 75 * 10:
        	self.image = pygame.image.load("assets/coin.png").convert_alpha()
        	self.value = 1
        else:
        	self.image = pygame.image.load("assets/alsocoin.png").convert_alpha()
        	self.value = 3
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(200, 950), 0)

    def move(self):
        global SLOW_DOWN_SPEED
        self.rect.move_ip(0, 0.9 * SPEED - 12 - SLOW_DOWN_SPEED)

        if self.rect.top > 1980:
            self.kill()

class Puddle(pygame.sprite.Sprite):
        def __init__(self):
        	super().__init__()
        	self.image = pygame.image.load("assets/Puddle.png").convert_alpha()
        	self.rect = self.image.get_rect()
        	self.spawn()
        
        def spawn(self):
        	self.rect.center = (random.randint(250, 800), 0)
        
        def move(self):
        	global SLOW_DOWN_SPEED
        	self.rect.move_ip(0, 0.9 * SPEED - 12 - SLOW_DOWN_SPEED)
        	if self.rect.top > 1980:
        		self.kill()    	
        
class PowerUp(pygame.sprite.Sprite):
	      def __init__(self):
	      	super().__init__()
	      	a = random.randint(1, 1000)
	      	if a < 619:
	      		self.image = pygame.image.load("assets/pipis.png").convert_alpha()
	      		self.type = "Shield"
	      	else:
	      		self.image = pygame.image.load("assets/magic_drink.png").convert_alpha()
	      		self.type = "Nitro"
	      	self.rect = self.image.get_rect()
	      	self.spawn()
	      
	      def spawn(self):
	      	self.rect.center = (random.randint(250, 850), 0)
	      
	      def move(self):
        	global SLOW_DOWN_SPEED
        	self.rect.move_ip(0, 0.9 * SPEED - 12 - SLOW_DOWN_SPEED)
        	if self.rect.top > 1980:
        		self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/Player.png").convert_alpha()
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
            self.rect.move_ip(self.direction * (SPEED - 10 - SLOW_DOWN_SPEED), 0)
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
puddles = pygame.sprite.Group()
powerups = pygame.sprite.Group()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

AFFECT_SPEED = -5 * SPEED + 2 * SLOW_DOWN_SPEED

SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 4500 + AFFECT_SPEED)

SPAWN_PUDDLE = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_PUDDLE, 15000 + AFFECT_SPEED + SPEED)

SPAWN_POWERUP = pygame.USEREVENT + 4
pygame.time.set_timer(SPAWN_POWERUP, 25000 + AFFECT_SPEED + 2 * SPEED)

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
        if event.type == SPAWN_PUDDLE:
        	  puddle = Puddle()
        	  puddles.add(puddle)
        	  all_sprites.add(puddle)
        if event.type == SPAWN_POWERUP:
        	  powerup = PowerUp()
        	  powerups.add(powerup)
        	  all_sprites.add(powerup)
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
    hit_enemies = pygame.sprite.spritecollide(P1, enemies, False)
    if hit_enemies:
          if SHIELD is False:
            pygame.mixer.Sound('assets/incident.mp3').play()
            time.sleep(0.5)
                   
            screen.fill(BLACK)
            screen.blit(game_over, (250,250))
          
            pygame.display.update()
            for entity in all_sprites:
                  entity.kill() 
            time.sleep(3.67)
            pygame.quit()
            sys.exit()
            
          else:
    	      pygame.mixer.Sound('assets/shield-break.mp3').play()
    	      SHIELD = False
    	      SCORE += 1
    	      for enemy in hit_enemies:
    	      	enemy.rect.top = 0
    	      	enemy.rect.center = (random.randint(240, 720), 0)

    if pygame.sprite.spritecollide(P1, puddles, True):
          pygame.mixer.Sound('assets/splat.mp3').play()
          SLOW_DOWN_SPEED += 0.3 * SPEED
    
    for enemy in enemies:
          if pygame.sprite.spritecollide(enemy, puddles, True):
            pygame.mixer.Sound('assets/splat.mp3').play()
            enemy.slowed += 0.4 * SPEED
            
    for powerup in powerups:
          if P1.rect.colliderect(powerup.rect):
            if powerup.type == "Shield":
              pygame.mixer.Sound('assets/shield.mp3').play()
              SHIELD = True
            if powerup.type == "Nitro":
              pygame.mixer.Sound('assets/roblox-drink.mp3').play()
              Nitro = True
              SPEED += 20
              nitro_start = pygame.time.get_ticks()
            powerup.kill()
    cur_time = pygame.time.get_ticks()
    if Nitro:
      if cur_time - nitro_start >= 5000:
              Nitro = False
              SPEED -= 20
              
                       
    # Collecting coins and playing the sound effect
    collected = pygame.sprite.spritecollide(P1, coins, True)
    if collected:
    	LAST_KROMER = KROMER
    	KROMER  += sum(pipis.value for pipis in collected)
    	if KROMER != 0 and (KROMER % 4 == 0 or (KROMER - LAST_KROMER > 1 and KROMER % 4 != 3)) and not t:
    		start_time = pygame.time.get_ticks()
    		pygame.mixer.Sound('assets/insanity.mp3').play()
    		BIG_SHOT_ENEMY_SPEED += 1.997
    		pp = True
    		t = True
    		blink_start = pygame.time.get_ticks()
    		blink_active = True
    	elif KROMER < 5:
    	    pygame.mixer.Sound('assets/kromer_received.mp3').play()
    	    t = False
    	elif KROMER >= 5:
    		  pygame.mixer.Sound('assets/evil_kromer_received.mp3').play()
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