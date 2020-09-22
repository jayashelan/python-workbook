import pygame
import time
import random

pygame.init()

white = (255,255,255)
yellow =(255,255,102)
black  = (0, 0, 0)
red = (213,50,80)
green =(0,255,0)
blue =(50,153,213)


dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game by Jay")

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#sound
bruit_mouvement = pygame.mixer.Sound("move.wav")

#images
head = pygame.image.load("head.png").convert_alpha() # La tête
head = pygame.transform.scale(head, (snake_block,snake_block))
corps1 = pygame.image.load("corps.png").convert_alpha() #Le corps
corps1 = pygame.transform.scale(corps1, (snake_block,snake_block))
fruit = pygame.image.load("fruit.png").convert_alpha() #Le fruit
fruit = pygame.transform.scale(fruit, (snake_block,snake_block))

def your_score(score):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: "+str(score), True, (0, 0, 0))
	dis.blit(text,(500,0))	


def our_snake(snake_block,snake_list):
	dis.blit(head, (snake_list[0][0], snake_list[0][1]))
	for x in snake_list[1:]:
		#pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
		dis.blit(corps1, (x[0], x[1]))

def message(msg,color):
	mesg = font_style.render(msg,True,color)
	dis.blit(mesg,[dis_width/3,dis_height/3])


def gameloop():
	game_over = False
	game_close = False
	
	x1 = dis_width/2
	y1 = dis_height/2

	x1_change = 0
	y1_change = 0

	snake_list = []
	length_of_snake = 1

	foodx = round(random.randrange(0,dis_width - snake_block)/ 10.0) * 10.0
	foody = round(random.randrange(0,dis_height - snake_block)/10.0) * 10.0

	print("foodx  {} foody {}".format(foodx,foody))



	
	while not game_over:
		while game_close == True:
			dis.fill(white)
			message("You Lost! Press Q-Quit or C-Play Again",red)
			your_score(length_of_snake - 1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameloop()

						
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
					pygame.mixer.Sound.play(bruit_mouvement)
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
					pygame.mixer.Sound.play(bruit_mouvement)
				elif event.key == pygame.K_UP:
					y1_change = -snake_block
					x1_change = 0
					pygame.mixer.Sound.play(bruit_mouvement)
				elif event.key == pygame.K_DOWN:
					y1_change = snake_block
					x1_change = 0
					pygame.mixer.Sound.play(bruit_mouvement)

		if x1 >=dis_width or x1 < 0 or y1 >=dis_height or y1 < 0:
			game_close = True

		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)

		#pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
		dis.blit(fruit, (foodx,foody))
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x== snake_head:
				game_close = True

		our_snake(snake_block,snake_list)
		your_score(length_of_snake -1)

		pygame.display.update()		

		if x1== foodx and y1 == foody:
			foodx = round(random.randrange(0,dis_width  - snake_block) /10.0 ) * 10.0
			foody = round(random.randrange(0,dis_height  - snake_block) /10.0 ) * 10.0
			length_of_snake +=1

		clock.tick(snake_speed)


	pygame.quit()
	quit()

gameloop()	

