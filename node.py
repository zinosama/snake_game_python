class Node(object):
	def __init__(self, data = None, prev_node = None, next_node = None):
		self.data = data
		self.prev_node = prev_node
		self.next_node = next_node

	def set_next(self, new_node):
		self.next_node = new_node

	def get_next(self):
		return self.next_node

	def get_prev(self):
		return self.prev_node

	def get_data(self):
		return self.data
