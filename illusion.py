import pygame
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)

width = 800
height = 600

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Illusion')
clock = pygame.time.Clock()

display1 = pygame.Surface((width, height), pygame.SRCALPHA)
display1.fill(white)

for i in range(1000):
	x = random.randrange(0,width)
	y = random.randrange(0,height)
	r = random.randrange(0,3)
	
	pygame.draw.circle(display1, black, (x, y), r, 0)
	
display2 = display1.copy()
display2.set_colorkey(white)

offset_x = 0
offset_y = 0
offset_ro = 0
offset_size = 1


done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				offset_x -= 1
			elif event.key == pygame.K_RIGHT:
				offset_x += 1
			elif event.key == pygame.K_DOWN:
				offset_y -= 1
			elif event.key == pygame.K_UP:
				offset_y += 1
			elif event.key == pygame.K_UP:
				offset_y += 1
			elif event.key == pygame.K_a:
				offset_ro -= 1
			elif event.key == pygame.K_d:
				offset_ro += 1
			elif event.key == pygame.K_s:
				offset_size -= 0.01
			elif event.key == pygame.K_w:
				offset_size += 0.01
		
			rotated = pygame.transform.rotate(display1, offset_ro)
			scaled = pygame.transform.scale_by(rotated, offset_size)
			
			rect = scaled.get_rect(center = display1.get_rect(topleft = (0,0)).center)
			
			display2.fill(white)
			display2.blit(scaled, rect.topleft)
			display2.set_colorkey(white)
	
	gameDisplay.fill(white)
	gameDisplay.blit(display1, (0,0))
	gameDisplay.blit(display2, (offset_x, offset_y))
	

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()