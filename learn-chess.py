import subprocess as sp
import os

def person(info):
	return info
sp.call('clear')
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")
skill = input("From 1-10 How do you rate your Chess Game?: ")

sp.call('clear')
print(person("Name: " + f_name + " " + l_name + "\r\n" + "Age: " + age + '\r\n' + "Skill: " + skill))
print(" ")
print("Learning Chess and Programming! A Way of Life\r\n")

chess_pieces_points = {'King': 0, 'Queen': 9, 'Rook': 5, 'Bishop': 3, 'Night' :3, 'Pawn': 1}
chess_pieces = {"King": 1, "Queen": 1, "Rook": 2, "Bishop":2, "Knight": 2, "Pawn": 8}

while 1:

		def menu():
			strgs = ('Enter 1 To Learn Chess\r\n\r\n'
					 'Enter 2 To Play Chesss\r\n\r\n'
					 'Enter Ctrl-C To Exit\r\n\r\n'
					 'Your Choice Here : ')
			choice = input(strgs)
			return int(choice)
		while 1:
			choice = menu()
			if (choice == 3) is True:
				break
				print("Exiting program now!"

			elif (choice == 2):
				sp.call('clear')
				print("We Are Starting A Game Now!")
				os.system('python sunfish.py')
			elif (choice == 1):
				sp.call('clear')
				print("Chess Pieces: There are 16 chess pieces! Let's go through them\r\n\r\n")
				print("King Pieces = {}".format(chess_pieces['King']))
				print("Queen Pieces = {}".format(chess_pieces['Queen']))
				print("Rook Pieces = {}".format(chess_pieces['Rook']))
				print("Knight Pieces = {}".format(chess_pieces['Knight']))
				print("Bishop Pieces = {}".format(chess_pieces['Bishop']))
				print("Pawn Pieces = {}\r\n\r\n".format(chess_pieces['Pawn']))
