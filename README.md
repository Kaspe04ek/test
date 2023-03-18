# test

from pygame import *
from random import randint
from time import sleep

#шрифты и надписи
font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial' , 80)
win = font1.render('Победил 1-ый игрок', True , (50 , 250 , 0))
lose = font1.render('Победил 2-ый игрок' , True , (180 , 0 , 0))

#нам нужны такие картинки:
red_platform = "red.png" # фон игры
blue_platform = "blue.png" # герой
ball = "ball.png" # враг
fon = 'phon1.jpg'
 
rect.y_1 =  350
rect.y_2 = 350

speed = 10

#Создаём окошко
win_width = 800
win_height = 800
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(fon), (win_width, win_height))

 
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
 
#класс главного игрока
class Player_l(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        if e.type == KEYDOWN:
            if e.key == K_w:
                rect.y_1 - speed
            if e.key == K_s:
                rect.y_1 + speed
            
    
class Player_R(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_R(self):
        if e.type == KEYDOWN:
            if e.key == K_UP:
                rect.y_2 - speed
            if e.key == K_DOWN:
                rect.y_2 + speed
            
 
#класс спрайта-врага  
class ball1(GameSprite):
   #движение врага
    def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдет до края экрана
 


#создаём спрайты
platform_l = Player_l(red_platform, 50 , 350 , 30 , 60 , 10)
platform_R = Player_R(blue_platform, 700 , 35 , 30 , 60 , 10)
Ball = ball1(ball , 5 , 400 , 100 , 100  , 10 )
 
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False

 
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))


        #пишем текст на экране


        #производим движения спрайтов
        platform_l.update()
        platform_R.update()
        ball.update()


        #обновляем их в новом местоположении при каждой итерации цикла
        platform_l.reset()
        platform_R.reset()
        ball.reset()
    

        display.update()
    time.delay(30)
