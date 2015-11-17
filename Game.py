# coding: utf8
from Map import Map
import curses

class Game:
	""" All a bout my game """

	def __init__(self):
		self.state = 'off'
		self.window = curses.initscr()
		self.window.keypad(True)
		(self.width, self.height) = curses.COLS, curses.LINES
		curses.cbreak()
		curses.noecho()
		curses.curs_set(0)
		self.player = [2, 4]
		self.map = Map(self.width, self.height)
		self.map.generateRandom()
		self.map.connectRoom(self.map.room[0], self.map.room[1])

	def run(self):
		self.state = 'on'
		self.render()

	def pause(self):
		self.state = 'pause'

	def render(self):
		while(self.state != 'off'):
			self.window.move(self.player[0], self.player[1])
			self.map.renderMap(self.window)
			ch = self.window.getkey()
			self.checkKey(ch)
			self.window.clear()
			self.window.refresh()

	def checkKey(self, ch):
		if (ch == 'KEY_END'):
			self.exit()
		if (ch == 'KEY_DOWN'):
			self.player[0] += 1
		if (ch == 'KEY_UP'):
			self.player[0] -= 1
		if (ch == 'KEY_RIGHT'):
			self.player[1] += 1
		if (ch == 'KEY_LEFT'):
			self.player[1] -= 1

	def stop(self):
		self.state = 'off'

	def exit(self):
		self.state = 'off'
		curses.endwin()
		print self.width, self.height

