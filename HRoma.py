from pygame import *
class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_sprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 810:
            self.rect.x += self.speed 









window = display.set_mode((1360,700))
display.set_caption("Pin Pong")



background =  transform.scale(image.load("fon.jpg"),(1360,700))
finish = False

game = True
Clock = time.Clock()


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if  finish != True:
        window.blit(background,(0,0))

    display.update()
    time.delay(10)