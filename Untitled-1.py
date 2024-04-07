from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Maze')
background = transform.scale(image.load('321.jpg'),(win_width,win_height))

player = Player('123.png',5,win_height - 80,80,80,4)

finish = False

game =True
clock = time.Clock()
FPS = 60
score = 0
lost =  0

speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if  finish !=True:

        window.blit(background,(0,0))
        # ball.rect.x +=speed_x
        # ball.rect.y +=speed_y
        # if ball.rect.y >win_height -50
        #     or ball.rect.y <0:
        #         speed_y *=-1



        player.reset()
        player.update()


    
    display.update()
    clock.tick(FPS)




























































# from pygame import *
# from random import randint

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')


# class GameSprite(sprite.Sprite):
#     def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image),(size_x,size_y))
#         self.speed=player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y

    # def reset(self):
    #     window.blit(self.image,(self.rect.x,self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x >5:
#             self.rect.x -=self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
    
#     def fire(self):
#         bellet = Bullet('fire.ogg',self.rect.centerx,self.rect.top,15)
#         bullets.add(bullet)

 
# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = randint(80,win_width - 80)
#             self.rect.y = 0
#             lost = lost + 1


# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y <0:
#             self.kill()

        
# win_width = 700
# win_height = 500
# window = display.set_mode((win_width,win_height))
# display.set_caption('Maze')
# background = transform.scale(image.load('galaxy.jpg'),(win_width,win_height))

# player = Player('rocket.png',5,win_height - 80,50,80,4)

# monsters = sprite.Group()
# for i in range(1,6):
#     monster = Enemy('ufo.png',randint(80,win_width - 80),-40,80,50,randint(1,5))
#     monsters.add(monster)

# bullets = sprite.Group()

# font.init()
# font1 =font.Font(None,80)
# win = font1.render('YOU WIN',True,(255,255,255))
# lose = font1.render('YOU LOSE',True,(180,0,0))

# font2 = font.Font(None,36)


# finish = False


# game =True
# clock = time.Clock()
# FPS = 60
# score = 0
# lost =  0

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False

#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 fire_sound.play()
#                 player.fire

    # if  finish !=True:

    #     window.blit(background,(0,0))
         
#         text = font2.render('Счет' + str(score),1,(255,255,255))
#         window.blit(text,(10,20))

#         text_lose = font2.render('Пропущено:' + str(lost),1,(255,255,255))
#         window.blit(text_lose,(10,50))

#         collides = sprite.groupcollide(monsters,bullets,True,True)
#         for c in collides:
#             score= score+1
#             monster = Enemy('ufo.png',randint(80,win_width - 80),-40,80,50,randint(1,5))
#             monsters.add(monster)
#         if sprite.spritecollide(player,monsters,False) or lost >=4:
#             finish = True
#             window.blit(lose,(200,200))

#         if score >= 10:
#             finish = True
#             window.blit(win(200,200))
         



        # player.reset()
        # player.update()

    #     monsters.update()

    #     monsters.draw(window)






    # display.update()
    # clock.tick(FPS)


























# from pygame import *

# class GameSprite(sprite.Sprite):
#     def __init__(self,player_image,player_x,player_y,player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image),(65,65))
#         self.speed=player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y

#     def reset(self):
#         window.blit(self.image,(self.rect.x,self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x >5:
#             self.rect.x -=self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
#         if keys[K_UP] and self.rect.y >5:
#             self.rect.y -= self.speed
#         if keys[K_DOWN] and self.rect.y < win_height - 80:
#             self.rect.y +=self.speed

# class Enemy(GameSprite):
#     direction = 'left'
#     def update(self):
#         if self.rect.x <= 470:
#             self.direction = 'right'
#         if self.rect.x >= win_width - 85:
#             self.direction = 'left'
#         if self.direction == 'left':
#             self.rect.x -=self.speed
#         else:
#             self.rect.x += self.speed

# class Wall(sprite.Sprite):
#     def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
#         super().__init__()
#         self.color_1 = color_1
#         self.color_2 = color_2
#         self.color_3 = color_3
#         self.width = wall_width
#         self.height = wall_height
#         self.image = Surface((self.width,self.height))
#         self.image.fill((color_1,color_2,color_3))
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y

#     def draw_wall(self):
#         window.blit(self.image,(self.rect.x,self.rect.y))



# win_width = 700
# win_height = 500
# window = display.set_mode((win_width,win_height))
# display.set_caption('Maze')
# background = transform.scale(image.load('background.jpg'),(win_width,win_height))

# player = Player('hero.png',5,win_height - 80,4)
# monster = Enemy('cyborg.png', win_width - 80,200,2)
# final = GameSprite('treasure.png',win_width - 120,win_height - 80,0)
# stena = Wall(100,250,0,75,50,20,350)
# stena1 = Wall(250,250,0,280,-25,20,250)
# stena2 = Wall(150,50,0,180,180,20,450)
# stena3 = Wall(0,250,0,350,45,20,350)
# stena4 = Wall(180,0,0,100,45,20,50)

# finish = False
# game =True
# clock = time.Clock()
# FPS = 60

# font.init()
# font = font.Font(None,70)
# win=font.render('ꇢꄣ',True,(255,215,0))
# lose = font.render('ꇤꉾ',True,(180,0,0))


# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             gane = False

#     if  finish !=True:

#         window.blit(background,(0,0))
#         player.update()
#         monster.update()

#         player.reset()
#         monster.reset()
#         final.reset()

#         stena.draw_wall()
#         stena1.draw_wall()
#         stena2.draw_wall()
#         stena3.draw_wall()
#         stena4.draw_wall()

#         if sprite.collide_rect(player,monster) or sprite.collide_rect(player,stena) or sprite.collide_rect(player,stena1)or sprite.collide_rect(player,stena2)or sprite.collide_rect(player,stena3)or sprite.collide_rect(player,stena4):
#             finish = True
#             window.blit(lose,(200,200))
#             kick.play()

#         if sprite.collide_rect(player,final):
#             finish = True   
#             window.blit(win,(200,200))    
#             money.play()



#     display.update()
#     clock.tick(FPS)    