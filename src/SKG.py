import string 		as STR
import random 		as RND
import sys 		as SYS
import webbrowser 	as WEB

class GeneratorBase: # Define a set of base functions to utilize
	# Define global keyslots
	global fkey
	global skey
	global tkey
	global keystr

	def __init__(self): # Verify keyslots before starting, in case of any weird errors
		self.fkey = ""
		self.skey = ""
		self.tkey = ""
		self.keystr = ""
		if(self.fkey == "" and self.skey == "" and self.tkey == "" and self.keystr == ""):

			print("GeneratorBase successfully created")

		else:

			print("Launch Failure: GeneratorBase failed to create keyslots")
			SYS.exit()

	def _GenerateKey(self): # Actual key generation based on a general pattern
		i = 0
		j = 0
		k = 0
		tmp = ""
		for i in range(5):
			tmp += RND.choice(STR.letters).upper() # First key is purely letters
		self.fkey = tmp
		tmp = ""
		allowedNumber = True
		for j in range(3):
			if(j == 0):

				tmp = RND.choice(STR.letters).upper() # Second key contains a two-digit number

			a = RND.randint(1,2)
			if(a == 1 and allowedNumber):

				tmp += str(RND.randint(10,99))
				allowedNumber = False

			else:

				tmp += RND.choice(STR.letters).upper()

		if(len(tmp) == 3):

			tmp += str(RND.randint(10,99))

		if(len(tmp) == 4):

			tmp = tmp[0:len(tmp)] + str(RND.randint(10,99))

		allowedNumber = True
		self.skey = tmp
		tmp = ""
		for k in range(4):
			if(k == 0):

				tmp = RND.choice(STR.letters).upper() # Third key contains a single digit

			a = RND.randint(1,2)
			if(a == 1 and allowedNumber):

				tmp += str(RND.randint(1,9))
				allowedNumber = False

			else:

				tmp += RND.choice(STR.letters).upper()

		self.tkey = tmp
		tmp = ""
		self.keystr = self.fkey + "-" + self.skey + "-" + self.tkey # Generate key with template X-Y-Z

	def GetKey(self): # Public function to link with the wrapper
		self._GenerateKey()
		print(self.keystr)
		return self.keystr

class SteamkeyGenerator: # Actual public class
	global GEN
	def __init__(self): # Creation verification
		self.GEN = GeneratorBase()
		if(self.GEN):

			print("Generator created")

		else:

			print("SKG Generation failure -- exiting")
			SYS.exit()

	def CreateKeys(self, n): # Create a set of keys according to input
		i = 0
		self.GEN = GeneratorBase()
		keys = {}
		for i in range(n):
			keys[i] = self.GEN.GetKey()
		return keys

def main(): # Main function - Handles cli and execution

	if(len(SYS.argv) < 2 or len(SYS.argv) > 5):
		
		print("Usage :: " + SYS.argv[0] + " <keys> [-file || -f] [-open || -o] [-add || -a]")
		SYS.exit()

	SKG = SteamkeyGenerator()
	keylist = SKG.CreateKeys(int(SYS.argv[1]))

	if(len(SYS.argv) > 2):

		if(SYS.argv[2] == "-file" or SYS.argv[2] == "-f"):

			if(len(SYS.argv) == 5):

				if((SYS.argv[3] == "-add" or SYS.argv[3] == "-a") or (SYS.argv[4] == "-add" or SYS.argv[4] == "-a")):

					with open("keys.txt", "a+") as FILE:
						for p in range(len(keylist)):
							FILE.write(keylist[p]+"\n")
						print("Keys.txt has been updated successfully")

				else:

					with open("keys.txt", "w+") as FILE: # If its not an update, its a (re-)creation
						for p in range(len(keylist)):
							FILE.write(keylist[p]+"\n")
						print("Keys.txt has been created successfully")

				if((SYS.argv[3] == "-open" or SYS.argv[3] == "-o") or (SYS.argv[4] == "-open" or SYS.argv[4] == "-o")):

					WEB.open("keys.txt") # webbrowser uses the appropriate program, independent of OS
			else:

				if(SYS.argv[3] == "-add" or SYS.argv[3] == "-a"):

					with open("keys.txt", "a+") as FILE:
						for p in range(len(keylist)):
							FILE.write(keylist[p]+"\n")
						print("Keys.txt has been updated successfully")

				else:

					with open("keys.txt", "w+") as FILE:
						for p in range(len(keylist)):
							FILE.write(keylist[p]+"\n")
						print("Keys.txt has been created successfully")

				if(SYS.argv[3] == "-open" or SYS.argv[3] == "-o"):

					WEB.open("keys.txt") # webbrowser uses the appropriate program, independent of OS

		else: # No reason to attempt other file flags if the file hasnt been selected
			print("Invalid flag provided :: -file must be the first flag") 

main() # Execute
