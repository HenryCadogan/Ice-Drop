#!/usr/bin/python


class Eskimo:
	def __init__(self, name):
		self.name = name
		
	def getTurn(self):
		return [input("Enter a row: "), input("Enter a column: ")]
		
	def getName(self):
		return self.name
