import pygame,sys

from pygame  import font

pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game")


def search_font(name):
	found_font = font.match_font(name)
	return found_font

def font_renderer(font,size):
	font_object = pygame.font.Font(font,size)
	return font_object




pygame.display.update()

def message_renderer(font_object,color,xy,message):
	""" render the font on the screen"""
	rendered_text = font_object.render(message,True,(color))
	screen.blit(rendered_text,(xy))
	pygame.display.update()



def display_message(used_font,size,color,xy,message):
	""" render the message"""
	font_object = pygame.font.Font(used_font, size)
	rendered_text = font_object.render(message,True,(color))
	screen.blit(rendered_text,(xy))
	pygame.display.update()


## rendering the message
normal_mssage = [search_font('ubuntu'),30,(255,255,255),(5,400)]


def main():
	"""keep the window not closing"""
	while True:
		display_message(*normal_mssage,"Not much to see")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

main()				


















