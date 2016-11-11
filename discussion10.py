import pygame
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Drawing Shapes in Discussion Week 10!")

pygame.display.update()	

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gameDisplay.fill(white)

	pygame.draw.circle(gameDisplay, red, (50,100), 100, 0)


	pygame.draw.rect(gameDisplay, black, [700,300, 10, 100])
	pygame.draw.rect(gameDisplay, red, [400,100, 50, 50])
	pygame.draw.rect(gameDisplay, red, [500,80, 50, 50])
	pygame.draw.rect(gameDisplay, black, [400,300, 10, 70])

	pygame.display.update()	

pygame.quit()
quit()	