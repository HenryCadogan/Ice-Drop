#!/usr/bin/python
import random
import sys
import time
from Penguin import Penguin
from IceBerg import Iceberg


class Board:
	def __init__(self, boardSize):
		self.x = ""
		self.size = boardSize
		if not sys.stdout.isatty():
			print("Colors not enabled on this terminal, please ensure it is a tty to enable color")	
		self.board = [[Iceberg()]*boardSize]*boardSize
		self.placePenguins()

	def displayBoard(self):
		for rows in self.board:
			self.x = ""
			for column in rows:
				self.x += column.getSymbol()
			print(self.x)
			
	def placePenguins(self):
		numPenguins = max(1, round(self.size/10))
		print("Placing Penguins")
		while numPenguins > 0:
			if self.placeRow():
				break

	def placeRow(self):
		for row in range(self.size):
			if self.placeColumn(row):
				return True

	def placeColumn(self, row):
		for column in range(self.size):
			if random.randint(0, self.size ** 2) == 1:
				self.board[row][column] = Penguin()
				return True
				
	time.sleep(1)
	print("Penguins Placed!")
