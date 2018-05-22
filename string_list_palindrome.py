import os
playing = True

while playing == True:
	
	input_str = input("Enter a string: ")

	list_of_characters = list(input_str)

	reverse = []

	reverse =list_of_characters[::-1]

	rev =''.join(reverse)

	print("String Reversed: " + rev)

	if input_str == rev:

		print("This is a palindrome")
	else:

		print("This is not a palindrome")

	play_again = input('Do you want to play again? "Yes" or "no": ')

	if play_again == "yes":
		playing = True
		os.system('clear')

	else:
		print("Thanks for playing!")
		playing = False



























