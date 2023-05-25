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

key_speed = 0.5
scale_speed = 0.003
rot_speed = 0.25

def reset():
	global offset_x
	global offset_y
	global offset_ro
	global offset_size
	
	offset_x = 0
	offset_y = 0
	offset_ro = 0
	offset_size = 1
reset()

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				reset()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		offset_x -= key_speed
	elif keys[pygame.K_RIGHT]:
		offset_x += key_speed
	elif keys[pygame.K_DOWN]:
		offset_y -= key_speed
	elif keys[pygame.K_UP]:
		offset_y += key_speed
	elif keys[pygame.K_UP]:
		offset_y += key_speed
	elif keys[pygame.K_a]:
		offset_ro -= rot_speed
	elif keys[pygame.K_d]:
		offset_ro += rot_speed
	elif keys[pygame.K_s]:
		offset_size -= scale_speed
	elif keys[pygame.K_w]:
		offset_size += scale_speed
		
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