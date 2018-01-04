import string 	as STR
import random 	as RND
import sys 		as SYS

class GeneratorBase:
	global fkey
	global skey
	global tkey
	global keystr

	def __init__(self):
		self.fkey = ""
		self.skey = ""
		self.tkey = ""
		self.keystr = ""
		if(self.fkey == "" and self.skey == "" and self.tkey == "" and self.keystr == ""):
			print("GeneratorBase successfully created")
		else:
			print("Launch Failure: GeneratorBase failed to create keyslots")

	def _GenerateKey(self):
		i = 0
		j = 0
		k = 0
		tmp = ""
		for i in range(5):
			tmp = tmp + RND.choice(STR.letters).upper()
		self.fkey = tmp
		tmp = ""
		allowedNumber = True
		for j in range(3):
			if(j == 0):
				tmp = RND.choice(STR.letters).upper()
			a = RND.randint(1,2)
			if(a == 1 and allowedNumber):
				tmp = tmp + str(RND.randint(10,99))
				allowedNumber = False
			else:
				tmp = tmp + RND.choice(STR.letters).upper()
		if(len(tmp) == 3):
			tmp = tmp + str(RND.randint(10,99))
		if(len(tmp) == 4):
			tmp = tmp[0:len(tmp)] + str(RND.randint(10,99))
		allowedNumber = True
		self.skey = tmp
		tmp = ""
		for k in range(4):
			if(k == 0):
				tmp = RND.choice(STR.letters).upper()
			a = RND.randint(1,2)
			if(a == 1 and allowedNumber):
				tmp = tmp + str(RND.randint(1,9))
				allowedNumber = False
			else:
				tmp = tmp + RND.choice(STR.letters).upper()
		self.tkey = tmp
		tmp = ""
		self.keystr = self.fkey + "-" + self.skey + "-" + self.tkey

	def GetKey(self):
		self._GenerateKey()
		print(self.keystr)
		return self.keystr

class SteamkeyGenerator:
	def __init__(self):
		print("Generator created")
	def CreateKeys(self, n):
		i = 0
		GEN = GeneratorBase()
		keys = {}
		for i in range(n):
			keys[i] = GEN.GetKey()
		return keys
def main():
	if(len(SYS.argv) != 2):
		print("Usage :: " + SYS.argv[0] + " <keys>")
		SYS.exit()
	SKG = SteamkeyGenerator()
	keylist = SKG.CreateKeys(int(SYS.argv[1]))

main()