from node import *

class Snake(object):
	data = []
	move_pattern = {"x": {"up": -1, "right": 0, "down": 1, "left": 0}, "y": {"up": 0, "right": 1, "down": 0, "left": -1}}

	def __init__(self):
		self.head = Node({"x":3, "y":3, "symbol":"X"})
		self.head.next_node = Node({"x":2, "y":3, "symbol":"X"}, self.head)
		self.tail = self.head.next_node
		self.broken_tail = None

	def move(self, direction):
		new_x = self.head.data["x"] + self.move_pattern["x"][direction]
		new_y = self.head.data["y"] + self.move_pattern["y"][direction]
		new_head = Node({"x": new_x, "y": new_y, "symbol":"X"}, None, self.head)
		self.update_pointers(new_head)

	def update_pointers(self, new_head):
		self.head.prev_node = new_head #add new node
		self.head = new_head
		self.broken_tail = self.tail #preserve the last node
		self.tail = self.tail.prev_node #break off last node
		self.tail.next_node = None

	def print_snake(self):
		tmp = self.head
		while tmp:
			print tmp.data
			tmp = tmp.next_node

	def grow(self):
		if self.broken_tail:
			self.tail.next_node = self.broken_tail
			self.broken_tail.prev_node = self.tail
			self.tail = self.broken_tail
			self.broken_tail = None
		else:
			self.tail.next_node = Node({"x":3, "y":3, "symbol":"X"}, self.tail, None)
			self.tail = self.tail.next_node