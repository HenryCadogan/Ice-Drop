#!/usr/bin/python
import time
from Board import Board
from Eskimo import Eskimo


class Game:
    def __init__(self):
        self.minBoardSize = 5
        self.maxBoardSize = 20
        self.board = Board(self.getBoardSize())
        self.board.displayBoard()
        self.Eskimo1 = Eskimo(input("Player 1, input your name:"))
        self.Eskimo2 = Eskimo(input("Player 2, input your name:"))
        self.currentPlayer = self.Eskimo1
        self.playing = False
        while self.playing:
            print("{0}, it is your turn! ".format(self.currentPlayer.getName()))
            # todo check if they lost
            # todo if they have then end, and current player lost
            self.swapPlayers()
            time.sleep(0.5)
            self.clearScreen()

    def getBoardSize(self):
        size = int(input("Please enter the size for the board: "))
        while not (self.minBoardSize < size < self.maxBoardSize):
            size = int(
                input("ERROR!: Please enter a size between {0} and {1}: ".format(self.minBoardSize, self.maxBoardSize)))
        return size

    @staticmethod
    def clearScreen():
        for x in range(30):
            print("")

    def swapPlayers(self):
        if self.currentPlayer == self.Eskimo1:
            self.currentPlayer = self.Eskimo2
        else:
            self.currentPlayer = self.Eskimo1

game = Game()
