from snake import *
from random import randint
import sys

class Board(object):
	game_board = []

	def __init__(self, row, col):
		self.row = row + 2
		self.col = col + 2 #add border for gameboard
		self.create_board(self.row, self.col)

	def link_snake(self, snake):
		self.snake = snake

	def check_candy(self):
		if self.game_board[self.candy_x][self.candy_y] == "X":
			self.drop_candy()
			self.snake.grow()

	def drop_candy(self):
		self.candy_x = randint(1, self.row-2)
		self.candy_y = randint(1, self.col-2)
		self.game_board[self.candy_x][self.candy_y] = "*"

	def check_alive(self):
		head_x = self.snake.head.data["x"]
		head_y = self.snake.head.data["y"]
		if self.game_board[head_x][head_y] != " " and self.game_board[head_x][head_y] != "*":
			sys.exit("Game Over: You lost!")

	def paint_board(self):
		if self.snake.broken_tail:
			self.game_board[self.snake.broken_tail.data["x"]][self.snake.broken_tail.data["y"]] = " " #re-paint the broken tail
		self.check_alive()
		tmp_node = self.snake.head
		while tmp_node:
			self.game_board[tmp_node.data["x"]][tmp_node.data["y"]] = tmp_node.data["symbol"]
			tmp_node = tmp_node.next_node
		self.check_candy()

	def create_board(self, row, col):
		first_row = [" "," "]
		for j in range(0,col-2):
			first_row.insert(1, "-")
		self.game_board.append(first_row)
		
		for i in range(0, row-2):
			tmpRow = ["|","|"]
			for k in range(0, col-2):
				tmpRow.insert(1, " ")
			self.game_board.append(tmpRow)

		last_row = first_row
		self.game_board.append(last_row)


	def print_board(self):
		for col in self.game_board:
			for item in col:
				print item,
			print ""

