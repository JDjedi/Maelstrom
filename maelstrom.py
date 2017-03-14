class Maelstrom():

	def __init__(self):
		self.name = "Maelstrom App"
		self.description = "This app connects to the twitter api and appropriates\nthe political mood of the users by detecting hashtags\nand certain keywords."

	def info(self):
		print self.name 
		print self.description

	

		
test1 = Maelstrom()
test1.info()
test1.add(2, 3)