import pygame
from constants import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.fill(COLOR, rect=None, special_flags=0)

	print("Starting asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	return screen

screen = main()

clock = pygame.time.Clock()
dt = 0
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(COLOR)
	pygame.display.flip()
	dt = clock.tick(60) / 1000.0

		