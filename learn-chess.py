import subprocess as sp

def person(info):
	return info

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")

sp.call('clear')
print(person("Name: " + f_name + " " + l_name + "\r\n" + "Age: " + age))
print(" ")
print("Learning Chess and Programming - A Way of Life")

chess_pieces_points = {'King': 0, 'Queen': 9, 'Rook': 5, 'Bishop': 3, 'Night' :3, 'Pawn': 1}
chess_pieces = {"King": 1, "Queen": 1, "Rook": 2, "Bishop":2, "Knight": 2, "Pawn": 8}

while 1:
	try:
		ready = int(input("{} {}! Are You Ready? Enter 1 to Start - 2 for Exit: ".format(f_name, l_name)))
		if (ready == 2):
			print("Exiting program now!")
			break
		elif (ready == 1):
			print("We are starting now!")
			sp.call('clear')
			print("Chess Pieces: There are 16 chess pieces! Let's go through them")
			print("King Pieces = {}".format(chess_pieces['King']))
			print("Queen Pieces = {}".format(chess_pieces['Queen']))
			print("Rook Pieces = {}".format(chess_pieces['Rook']))
			print("Knight Pieces = {}".format(chess_pieces['Knight']))
			print("Bishop Pieces = {}".format(chess_pieces['Bishop']))
			print("Pawn Pieces = {}".format(chess_pieces['Pawn']))
			break
		else:
			print("Please Enter 1 or 2")
	except ValueError:
		print("Please enter 1 or 2")
