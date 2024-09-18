import pygame
from pygame.locals import QUIT

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
tier = 1

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('TD Game Demo')

#load images
lv1img = pygame.image.load('lv1.png').convert_alpha()
lv2img = pygame.image.load('lv2.png').convert_alpha()
lv3img = pygame.image.load('lv3.png').convert_alpha()
upgradeimg = pygame.image.load('upgradebutt.png').convert_alpha()

#button class
class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False

  def draw(self, surface):
    action = False
    #get mouse position
    pos = pygame.mouse.get_pos()

    #check mouseover and clicked conditions
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        action = True

    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False

    #draw button on screen
    surface.blit(self.image, (self.rect.x, self.rect.y))

    return action

def tiercheck(tier):
  if tier == 1:
    screen.blit(lv1img, (100, 100))
  elif tier == 2:
    screen.blit(lv2img, (100, 100))
  else:
    screen.blit(lv3img, (100, 100))
    
upgradebutton = Button(300,100,upgradeimg,1)
#game loop
run = True
while run:

  screen.fill((255,255,255))
  if upgradebutton.draw(screen):
    if tier <= 2:
      tier += 1
      print(f"Upgraded! Your building is now a tier {tier} building!")
    else:
      print(f"Sorry! You reached the max tier for this building: Tier {tier}")
  tiercheck(tier)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
