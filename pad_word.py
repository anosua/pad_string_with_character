# Will pad the given string with the given padding character(s)
# The final string length will be 80 characters
# TODO: make it work/test with multiple padding characters

def main():

	string = input("Enter string to pad: ")
	ch =input("Enter padding character(s): ");

	# '2' is for the number of spaces (one on each side of the string)
	if (len(string) + (len(ch) * 2) + 2 > 80):
		print("The combination of the entered string and characters is longer than 80");
		exit(1)

	# Caluclating padding length
	num_of_pad = int((78 - len(string)) / 2)
	has_decimals = (78 - len(string)) % 2

	# printing out the string
	print(str(ch * num_of_pad) + " " + string + " " + str(ch * num_of_pad), end ="")
	
	# accounting for even/odd number in the final string
	if has_decimals != 0:
		print(ch)
	else:
		print("")


if __name__ == "__main__":
	main()
