# coding: utf8
from Map import Map
from Player import Player
import curses

class Game:
	""" All a bout my game """
	DISPLAY = True

	def __init__(self):
		self.state = 'off'
		self.player = Player("Bruno", 3, 3, 100)
		self.window = curses.initscr()
		(self.width, self.height) = curses.COLS, curses.LINES
		if (Game.DISPLAY):
			self.initCurses()
		else:
			curses.endwin()
		self.map = Map(self.width, self.height)
		self.map.generateRandom()
		self.map.connectRoom(self.map.room[0], self.map.room[1])

	def initCurses(self):
		self.window.keypad(True)
		curses.cbreak()
		curses.noecho()
		curses.curs_set(0)


	def run(self):
		self.state = 'on'
		if (Game.DISPLAY):
			self.render()

	def pause(self):
		self.state = 'pause'

	def render(self):
		while(self.state != 'off'):
			self.map.renderMap(self.window)
			self.player.renderMe(self.window)
			ch = self.window.getkey()
			self.checkKey(ch)
			self.window.clear()
			self.window.refresh()

	def checkKey(self, ch):
		if (ch == 'KEY_END'):
			self.exit()
		if (ch == 'KEY_DOWN'):
			self.player.y += 1
		if (ch == 'KEY_UP'):
			self.player.y -= 1
		if (ch == 'KEY_RIGHT'):
			self.player.x += 1
		if (ch == 'KEY_LEFT'):
			self.player.x -= 1

	def stop(self):
		self.state = 'off'

	def exit(self):
		self.state = 'off'
		curses.endwin()
		print self.width, self.height

