board = [[" ", " ", " "],
		 [" ", "X", " "],
		 [" ", " ", " "]]

new_board = ""


print("  1  2  3")

for row in range(3):
	new_board += str(row+1)

	for column in range(3):
		if board[row][column] == " ":
			new_board += "[ ]"
		elif board[row][column] == "X":
			new_board += "[X]"
		else:
			new_board += "[O]"

		if column == 2:
			new_board += "\n"

	

print(new_board)