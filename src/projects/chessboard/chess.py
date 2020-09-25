import pygame
import time

def main():
	"""Set up the game and run the main loop"""
	pygame.init()
	surface_sz = 480

	#create a surface of width and height
	main_surface = pygame.display.set_mode((surface_sz,surface_sz))

	#load the image to draw
	ball = pygame.image.load("ball.png")

	#Create a font for rendering the text
	my_font = pygame.font.SysFont("Courier",16)

	frame_count= 0
	frame_rate =0
	t0 = time.process_time() 

	# Set up some data to describe a small rectangle and its color
	small_rect = ((300,200,150,0))
	some_color = ((255,0,0))

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break

		# Update the game objects and data structures here
		frame_count += 1
		if frame_count % 500 == 0:
			t1 = time.process_time() 
			frame_rate = 500 // (t1 - t0 )
			t0 = t1




		# we draw from scratch on each frame
		# so first fill everthing with background color
		main_surface.fill((0,200,255))
		# So the first fill everything with the backgroind color
		main_surface.fill((255,0,0), (300, 100, 150, 90))

		# Copy the image to the surface (x,y) postn
		main_surface.blit(ball,(100,200))

		# Make a new surface with the image of the text
		the_text = my_font.render("Frame = {0} , rate {1:.2f} fps".format(frame_count,frame_rate),True,(0,0,0))
		
		main_surface.blit(the_text,(10,10))

		#Now surface is ready tell pygame to display
		pygame.display.flip()

	pygame.quit

main()		
