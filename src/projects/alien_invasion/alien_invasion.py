import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
	"""Overall to manage game assets and behavior"""

	def __init__(self):
		"""initialize hthe game and create a game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()



	def _create_fleet(self):
		"""Create the fleet of aliens"""
		#Make an Alien
		alien = Alien(self)
		alien_width,alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_alien_x =  available_space_x // (2* alien_width)

		# Determine the number of rows of aliens that fit the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * ship_height) - ship_height  )
		number_rows = available_space_y // (2 * alien_height)


		#Creat the first row of alien
		for row_number in range(number_rows):
			for alien_number in range(number_alien_x):
				#create an alien and place it in the row
				self._create_alien(alien_number,row_number)


	def _create_alien(self,alien_number,row_number):

		""" Create an alien and place in the row"""
		alien = Alien(self)
		alien_width,alien_height = alien.rect.size

		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)



    




	def run_game(self):
		"""Start the main loop for the game"""

		while True:
			# Watch for keyword and mouse event
			self._check_events()

			#Redraw the screen during each pass through the loop
			self.ship.update()

			self._update_bullets()
			self.update_alien()
			
			self._update_screen()
	def update_alien(self):
		""" make the aliens move"""
		self.aliens.update()
			

	def _check_events(self):
		"""Respond to keypress and mouse events"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
					
	
	def _check_keydown_events(self,event):
		"""Respond to keypress"""
		if event.key == pygame.K_RIGHT:
			#move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullets()
	
	def _fire_bullets(self):
		"""Create a bullet and add to the bullet group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

			



	def _check_keyup_events(self,event):
		"""Respond to keyup event"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

			


	def _update_bullets(self):
		"""Update position"""
		#Get rid of bullets that have disappeared
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)
			
			
	def _update_screen(self):
		"""draw on the screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)	

		pygame.display.flip()

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				
		



if __name__ =='__main__':
	#Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()







	



