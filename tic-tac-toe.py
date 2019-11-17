class board():
	board = [[" ", " ", " "],
			 [" ", " ", " "],
			 [" ", " ", " "]]

	@classmethod
	def drawBoard(self):

		new_board = ""

		print("  1  2  3")

		for row in range(3):
			new_board += str(row+1)
			
			for column in range(3):
				if self.board[row][column] == " ":
					new_board += "[ ]"
				elif self.board[row][column] == "X":
					new_board += "[X]"
				else:
					new_board += "[O]"

				if column == 2:
					new_board += "\n"

		print(new_board)

class mark():

	# function to add a sign on ones turn
	def marking(self, coordinate):
		coordinate = str(coordinate)
		x = str(coordinate[0])
		y = str(coordinate[-1])
		pass

class X(mark):
	pass

class O(mark):
	pass


board.drawBoard()