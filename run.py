from board import *
from snake import *
from node import *
import os #used to clear screen
import sys
from select import select

instruction_dictionary = {"w":"up", "d":"right", "s":"down", "a":"left"}
board1 = Board(10,10)
snake1 = Snake()
board1.link_snake(snake1)
board1.drop_candy()
board1.paint_board()
board1.print_board()

user_input = "input placeholder"
time_out = 1 #default timeout: 1s
last_instruction = "d" #default instruction: move right
while user_input != "ee": #to exit, type ee
	rlist, _, _ = select([sys.stdin], [], [], time_out)
	if rlist:
		user_input = sys.stdin.readline().strip()
	else:
		user_input = last_instruction

	if user_input in instruction_dictionary:
		last_instruction = user_input
		instruction = instruction_dictionary[user_input]
		snake1.move(instruction)

		os.system('clear') #clear screen
		board1.paint_board()
		board1.print_board()
