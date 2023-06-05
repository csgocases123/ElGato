import pygame
import button
import os
import random
import time
from pygame.locals import *
from slider import Slider
pygame.init()
pygame.font.init()

HEIGHT = 1000
WIDTH = 660

level = 0
cows = 5
wave_length = 0
bullets_to_remove = []
transparent = (0, 0, 0, 0)

mainfont = pygame.font.Font("elgatoassets/Carnevalee Freakshow.ttf", 30)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('ElGatoGame')

taustapilt = pygame.image.load("elgatoassets/pixelmenu.png").convert_alpha()
slider = Slider(WIDTH/2+75, 300, 200, 0.0, 1.0, pygame.mixer)

music_files = [
    "elgatoassets/Pistolero.mp3",
    "elgatoassets/rusty.mp3",
    "elgatoassets/gallows.mp3",
    "elgatoassets/standoff.mp3",
    "elgatoassets/ghost.mp3",
    "elgatoassets/hell.mp3",
    "elgatoassets/rooster.mp3"
    ]

#click buttons
start_img = pygame.image.load('elgatoassets/elstart.png').convert_alpha()
option_img = pygame.image.load('elgatoassets/eloptions.png').convert_alpha()
exit_img = pygame.image.load('elgatoassets/elquit.png').convert_alpha()
back_img = pygame.image.load('elgatoassets/elback.png').convert_alpha()
skip_img = pygame.image.load('elgatoassets/elskip.png').convert_alpha()
yes_img = pygame.image.load('elgatoassets/elyes.png').convert_alpha()
next_img = pygame.image.load('elgatoassets/elnext.png').convert_alpha()
next_button = button.Button(HEIGHT/2+90, 500, next_img, 1)
start_button = button.Button(150, 225, start_img, 1)
exit_button = button.Button(750, 225, exit_img, 1)
option_button = button.Button(420, 225, option_img, 1.3)
back_button = button.Button(WIDTH/2+110, 500, back_img, 1)
tutback_button = button.Button(WIDTH/2, 500, back_img, 1)
yes_button = button.Button(430, 200, yes_img, 1.3)
skip_button = button.Button(440, 310, skip_img, 1)


#characterscreen
gg_img = pygame.image.load('elgatoassets/FINALSHERIFFCAT.png').convert_alpha()
ag_img = pygame.image.load('elgatoassets/FINALARCHERCAT.png').convert_alpha()
sg_img = pygame.image.load('elgatoassets/FINALSWORDCAT.png').convert_alpha()
mg_img = pygame.image.load('elgatoassets/FINALMAGECAT.png').convert_alpha()

gg_button = button.Button(0, 200, gg_img, 1)
ag_button = button.Button(250, 200, ag_img, 1)
sg_button = button.Button(500, 200, sg_img, 1)
mg_button = button.Button(750, 200, mg_img, 1)


#enemy
fakefirefighter = pygame.image.load("elgatoassets/firefighter.png").convert_alpha()
valekokk = pygame.image.load("elgatoassets/kokk.png").convert_alpha()
vakokk = pygame.transform.flip(valekokk, True, False)
fakepolitsei = pygame.image.load("elgatoassets/elpolice.png").convert_alpha()
fakecowboy = pygame.image.load("elgatoassets/cowboy.png").convert_alpha()
cowboy = pygame.transform.scale(fakecowboy, (150, 150))
firefighter = pygame.transform.scale(fakefirefighter, (150, 150))
kokk = pygame.transform.scale(vakokk, (150, 150))
politsei = pygame.transform.scale(fakepolitsei, (150, 150))


#characters
fakegungato = pygame.image.load("elgatoassets/gungato.png").convert_alpha()
fakearchergato = pygame.image.load("elgatoassets/archergato.png").convert_alpha()
fakeswordgato = pygame.image.load("elgatoassets/swordgato.png").convert_alpha()
fakemagegato = pygame.image.load("elgatoassets/magegato.png").convert_alpha()
gungato = pygame.transform.scale(fakegungato, (150, 150))
archergato = pygame.transform.scale(fakearchergato, (150, 150))
swordgato = pygame.transform.scale(fakeswordgato, (150, 150))
magegato = pygame.transform.scale(fakemagegato, (150, 150))

#images
elmovetext = pygame.image.load("elgatoassets/elmovetext.png").convert_alpha()
elshoottext = pygame.image.load("elgatoassets/elshoottext.png").convert_alpha()
elgoaltext = pygame.image.load("elgatoassets/elgoaltext.png").convert_alpha()
taustapilt = pygame.image.load("elgatoassets/pixelmenu.png").convert_alpha()
tiitel = pygame.image.load("elgatoassets/eltitle.png").convert_alpha()
menüükass = pygame.image.load("elgatoassets/maingato4.png").convert_alpha()
hääl = pygame.image.load('elgatoassets/elvolume.png').convert_alpha()
tutorialtiitel = pygame.image.load("elgatoassets/eltutorialtitle.png").convert_alpha()
fakemängutaustapilt = pygame.image.load("elgatoassets/mainbackground.png").convert_alpha()
elchoose = pygame.image.load("elgatoassets/elchoose.png").convert_alpha()
elescape = pygame.image.load("elgatoassets/elescape.png").convert_alpha()
fatsword = pygame.image.load("elgatoassets/sword.png").convert_alpha()
fatarrow = pygame.image.load("elgatoassets/arrow.png").convert_alpha()
fatfireball = pygame.image.load("elgatoassets/fireball.png").convert_alpha()
fatbullet = pygame.image.load("elgatoassets/bullet.png").convert_alpha()
fakelehm = pygame.image.load("elgatoassets/lehm.png").convert_alpha()
fakegate = pygame.image.load("elgatoassets/elgate.png").convert_alpha()
fakejukebox = pygame.image.load("elgatoassets/jukebox.png").convert_alpha()
faketeacher = pygame.image.load("elgatoassets/elteacher.png").convert_alpha()
fakemove = pygame.image.load("elgatoassets/elmove.png").convert_alpha()
fakeshoot = pygame.image.load("elgatoassets/elshoot.png").convert_alpha()
fakegoal = pygame.image.load("elgatoassets/elgoal.png").convert_alpha()
elmove = pygame.transform.scale(fakemove, (200, 200))
elshoot = pygame.transform.scale(fakeshoot, (200, 200))
elgoal = pygame.transform.scale(fakegoal, (200, 300))
teacher = pygame.transform.scale(faketeacher, (100, 100))
jukebox = pygame.transform.scale(fakejukebox, (200, 200))
gate = pygame.transform.scale(fakegate, (100, 600))
lehm1 = pygame.transform.scale(fakelehm, (200, 200))
lehm2 = pygame.transform.scale(fakelehm, (200, 200))
lehm3 = pygame.transform.scale(fakelehm, (200, 200))
lehm4 = pygame.transform.scale(fakelehm, (200, 200))
lehm5 = pygame.transform.scale(fakelehm, (200, 200))
bullet = pygame.transform.scale(fatbullet, (60, 30))
enemybullet = pygame.transform.scale(fatbullet, (50, 50))
fireball = pygame.transform.scale(fatfireball, (60, 80))
arrow = pygame.transform.scale(fatarrow, (60, 80))
sword = pygame.transform.scale(fatsword, (70, 60))
mängutaustapilt = pygame.transform.scale(fakemängutaustapilt, (1000,660))
cowslabel = mainfont.render(f"Cows: {cows}", 1, (0,0,0))
levellabel = mainfont.render(f"Level: {level}", 1, (0,0,0))
lostlabel = mainfont.render("You lost!", 10, (255,0,0))


class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        
    def draw(self, window):
        screen.blit(self.img, (self.x,self.y))

    def bulmove(self,vel):
        self.x += bullet_vel

    def offscreen(self, HEIGHT):
        return not (self.x <= HEIGHT and self.x >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Player:
    COOLDOWN = 30
    
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.player_img = None
        self.bullet_img = None
        self.health = health
        self.attack = ()
        self.cooldowncounter = 0
        self.bullets = []

    def cooldown(self):
        if self.cooldowncounter >= self.COOLDOWN:
            self.cooldowncounter = 0
        elif self.cooldowncounter > 0:
            self.cooldowncounter += 1

    def shoot(self):
        if self.cooldowncounter == 0:
            bullet = Bullet(self.x+120, self.y+50, self.bullet_img)
            self.bullets.append(bullet)
            self.cooldowncounter = 1


    def movebullets(self, vel, objs):
        self.cooldown()
        bullets_to_remove = []

        for bullet in self.bullets:
            bullet.bulmove(vel)
            if bullet.offscreen(HEIGHT):
                bullets_to_remove.append(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        objs.remove(obj)
                        bullets_to_remove.append(bullet)

        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)
            

    def draw(self, window):
        self.healthbar(window)
        screen.blit(self.player_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)
        

    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()

    def healthbar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y + self.player_img.get_height() + 10, self.player_img.get_width(), 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y + self.player_img.get_height() + 10, self.player_img.get_width() * (self.health / self.max_health), 10))


class Enemy:
    COOLDOWN = 30
    
    def __init__(self, x, y, enemy_type, health):
        self.x = x
        self.y = y
        self.enemy_img = self.get_enemy_image(enemy_type)
        self.enemybullet_img = enemybullet
        self.health = health
        self.attack = ()
        self.cooldowncounter = 0
        self.speed = enemy_vel
        self.mask = pygame.mask.from_surface(self.enemy_img)
        self.enemybullets = []
 
    def cooldown(self):
        if self.cooldowncounter >= self.COOLDOWN:
            self.cooldowncounter = 0
        elif self.cooldowncounter > 0:
            self.cooldowncounter += 1


    def movebullets(self, vel, obj):
        self.cooldown()
        for enemybullet in self.enemybullets:
            enemybullet.bulmove(vel)
            if enemybullet.offscreen(HEIGHT):
                self.enemybullets.remove(enemybullet)
            elif collide(enemybullet, obj):
                obj.health -= 10
                self.enemybullets.remove(enemybullet)

            
    def shoot(self):
        if self.cooldowncounter == 0:
            enemybullet = Bullet(self.x, self.y, self.enemybullet_img)
            self.enemybullets.append(enemybullet)
            self.cooldowncounter = 1

    def draw(self, window):
        screen.blit(self.enemy_img, (self.x, self.y))

    def get_width(self):
        return self.enemy_img.get_width()

    def get_height(self):
        return self.enemy_img.get_height()

    def move(self):
        self.x -= self.speed

        self.shoot()

    def get_enemy_image(self, enemy_type):
        if enemy_type == "kokk":
            return kokk
        elif enemy_type == "firefighter":
            return firefighter
        elif enemy_type == "politsei":
            return politsei
        elif enemy_type == "cowboy":
            return cowboy
        else:
            return None


class Gungato(Player):
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = gungato
        self.bullet_img = bullet
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health
        self.bullets = []
        self.cooldowncounter = 0
        

class Archergato(Player):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = archergato
        self.bullet_img = arrow
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health
        self.bullets = []
        self.cooldowncounter = 0
        

class Swordgato(Player):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = swordgato
        self.bullet_img = sword
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health
        self.bullets = []
        self.cooldowncounter = 0
        

class Magegato(Player):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = magegato
        self.bullet_img = fireball
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health
        self.bullets = []
        self.cooldowncounter = 0
        




def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def mainmenu():
    screen.blit(taustapilt, (0,0))
    screen.blit(tiitel, (WIDTH/2+25, 50))
    screen.blit(menüükass, (WIDTH/2+50, 400))

def play_music(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    initial_volume = 1
    pygame.mixer.music.set_volume(initial_volume)
    pygame.mixer.music.play(-1)

def switch_music(new_filename):
    pygame.mixer.music.fadeout(500)
    pygame.time.wait(500)  
    pygame.mixer.music.load(new_filename)
    pygame.mixer.music.play(-1)

     
def options():
    screen.blit(taustapilt, (0,0))
    screen.blit(hääl, (WIDTH/2+125, 300))
    slider.draw(screen)

def tutorialmenu():
    screen.blit(taustapilt, (0,0))
    screen.blit(tutorialtiitel, (WIDTH/2-100, 80))
    

def tutorial():
    screen.blit(mängutaustapilt, (0,0))
    player.draw(screen)
    screen.blit(kokk, (500, 300))

def characterselection():
    screen.fill((117,48,0))
    screen.blit(elchoose, (WIDTH/2-80, 60))

def paused():
    paused = True
    while paused: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        screen.blit(taustapilt, (0,0))
        screen.blit(elescape, (WIDTH/2-110, 250))   
        pygame.display.update()
        clock.tick(5)

        if paused == False:
            play_random_music()


def maingame():
    cowslabel = mainfont.render(f"Cows: {cows}", 1, (0,0,0))
    levellabel = mainfont.render(f"Level: {level}", 1, (0,0,0))
    screen.blit(mängutaustapilt, (0,0))
    screen.blit(jukebox, (160,30))
    screen.blit(teacher, (210,0))
    screen.blit(gate, (165, 100))
    screen.blit(lehm1, (0,100))
    screen.blit(lehm2, (0,200))
    screen.blit(lehm3, (0,300))
    screen.blit(lehm4, (0,400))
    screen.blit(lehm5, (0,500))
    screen.blit(cowslabel, (10,10))
    screen.blit(levellabel, (900,10))
    player.draw(screen)
    


def spawn_enemy():
    global cows
    global level
    global wave_length
    for enemy in enemies:
        enemy.move()
        enemy.movebullets(bullet_vel, player)
        enemy.draw(screen)
        if random.randrange(0, 120) == 1:
            enemy.shoot()

        if collide(enemy, player):
            player.health -= 10
            enemies.remove(enemy)
        
        elif enemy.x + enemy.get_height() <= HEIGHT-700:
            cows -= 1
            enemies.remove(enemy)
 
    if len(enemies) == 0:
        level += 1
        wave_length += 5
        for _ in range(wave_length):
            enemy_type = random.choice(["kokk", "firefighter", "politsei", "cowboy"])
            enemy_health = 100
            enemy = Enemy(random.randrange(1050, 1500), random.randrange(50, 510), enemy_type, health=enemy_health)
            enemies.append(enemy)

    if cows == 4:
        lehm1.fill(transparent)
        pygame.display.update()

    if cows == 3:
        lehm2.fill(transparent)
        pygame.display.update()

    if cows == 2:
        lehm3.fill(transparent)
        pygame.display.update()
         
    if cows == 1:
        lehm4.fill(transparent)
        pygame.display.update()

    if cows == 0:
        lehm5.fill(transparent)
        pygame.display.update()

def play_random_music():
    pygame.mixer.music.fadeout(500)
    pygame.time.wait(500) 
    random_music = random.choice(music_files)
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.play(-1)

player_vel = 5
DOUBLE_CLICK_DELAY = 500
last_click_time = 0

enemies = []
wave_length = 5
enemy_vel = 1
bullet_vel = 4

lost_count = 0
lost = False
FPS = 60
elshowtime = False
gotime = False
clock = pygame.time.Clock()
clicked = False
menu_state = "mainmenu"
music_playing = False
pistolero = False
lostmusic = False
run = True
while run:
    clock.tick(FPS)

    if not music_playing:
        current_music = "elgatoassets/menumusic.mp3"
        play_music("elgatoassets/menumusic.mp3")
        music_playing = True
        
    
    if menu_state == "mainmenu":
        mainmenu()
        if start_button.draw(screen) and clicked == False:
            menu_state = "characterselection"
            clicked = True
        if exit_button.draw(screen) and clicked == False:
            run = False
            clicked = True
        if option_button.draw(screen) and clicked == False:
            menu_state = "options"
            clicked = True
        pygame.display.flip()

    if menu_state == "options":
        options()
        if back_button.draw(screen) and clicked == False:
            menu_state = "mainmenu"
            clicked = True
            


    if menu_state == "tutorial" and keys[pygame.K_ESCAPE]:
        switch_music("elgatoassets/pausedmusic.mp3")
        paused()

    if menu_state == "maingame" and keys[pygame.K_ESCAPE]:
        switch_music("elgatoassets/pausedmusic.mp3")
        paused()

    if menu_state == "characterselection":
        characterselection()
        if gg_button.draw(screen) and clicked == False:
            pygame.display.flip()
            player = Gungato(300,300)
            menu_state = "tutorialoffer"
            clicked = True
        if ag_button.draw(screen) and clicked == False:
            pygame.display.flip()
            player = Archergato(300,300)
            menu_state = "tutorialoffer"
            clicked = True
        if sg_button.draw(screen) and clicked == False:
            pygame.display.flip()
            player = Swordgato(300,300)
            menu_state = "tutorialoffer"
            clicked = True
        if mg_button.draw(screen) and clicked == False:
            pygame.display.flip()
            player = Magegato(300,300)
            menu_state = "tutorialoffer"
            clicked = True
        if back_button.draw(screen) and clicked == False:
            menu_state = "mainmenu"
            clicked = True
            pygame.display.flip()
        pygame.display.flip()

    if menu_state == "tutorialoffer":
        tutorialmenu()
        if yes_button.draw(screen) and clicked == False:
            menu_state = "tutorial"
            clicked = True
        if skip_button.draw(screen) and clicked == False:
            menu_state = "maingame"
        if back_button.draw(screen) and clicked == False:
            menu_state = "characterselection"
            clicked = True
            pygame.display.flip()

    if menu_state == "tutorial" and clicked == False:
        screen.fill((150,70,0))
        screen.blit(elmove, (HEIGHT/2-100, 100))
        screen.blit(elmovetext, (HEIGHT/2-350, 350))
        if tutback_button.draw(screen) and clicked == False:
            menu_state = "tutorialoffer"

        if next_button.draw(screen) and clicked == False:
            menu_state = "tutorial1"
            
        pygame.display.update()

    if menu_state == "tutorial1" and clicked == False:
        screen.fill((150,70,0))
        screen.blit(elshoot, (HEIGHT/2-110, 100))
        screen.blit(elshoottext, (HEIGHT/2-250, 350))

        if tutback_button.draw(screen) and clicked == False:
            menu_state = "tutorial"

        if next_button.draw(screen) and clicked == False:
            menu_state = "tutorial2"

        pygame.display.update()

    if menu_state == "tutorial2" and clicked == False:
        screen.fill((150,70,0))
        screen.blit(elgoal, (HEIGHT/2-110, 25))
        screen.blit(elgoaltext, (HEIGHT/2-420, 350))

        if tutback_button.draw(screen) and clicked == False:
            menu_state = "tutorial1"

        if next_button.draw(screen) and clicked == False:
            menu_state = "maingame"

        pygame.display.update()

    if menu_state == "maingame":
        maingame()
        spawn_enemy()
        player.movebullets(bullet_vel, enemies)
        pygame.display.update()
        if cows <= 0 or player.health <= 0:
            lost = True

            if lost and not lostmusic:
                switch_music("elgatoassets/womp.mp3")
                lostmusic = True
                pygame.display.update()
                screen.blit(lostlabel, (HEIGHT/2, 300))
                pygame.display.update()
                time.sleep(5)
                run = False
            else:
                continue



    if menu_state == "maingame" and not elshowtime == True:
        play_random_music()
        elshowtime = True

                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x - player_vel  > 200:
        player.x -= player_vel 
    if keys[pygame.K_d] and player.x - player_vel + player.get_width() < HEIGHT:
        player.x += player_vel 
    if keys[pygame.K_w] and player.y - player_vel > 20:
        player.y -= player_vel 
    if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < WIDTH:
        player.y += player_vel
    if keys[pygame.K_SPACE]:
        player.shoot()

            
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.QUIT:
          run = False
        slider.handle_event(event)
    pygame.display.flip()


pygame.quit()
