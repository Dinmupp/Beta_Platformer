import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('BetaPlatformer')
clock = pygame.time.Clock()

level = Level()

while True:
	keys = pygame.key.get_pressed()
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	
	screen.fill(BG_COLOR)
	level.run()
	

	# drawing logic
	pygame.display.update()
	clock.tick(60)