import trie
import getch


def iInput(prompt:str, lang:list) -> str:
	"""
	iInput
	function used to autosuggest input to a user based upon words in a given language
	@param prompt: prompt to be displayed for the input stream
	@param lang: list containing all words in the language to be used
	@return: string containing input given by user
	"""

	#TODO Handle non-ascii inputs such as arrow up/down along with escape codes

	t = trie.Trie()
	t.formTrie(lang)

	rw = ""
	cw = ""

	while True:

		cw += getch.getch().lower()

		if '\r' in cw:
			rw += cw
			print(' '*50, end='\r')
			print(f"{prompt}\033[1;97m{rw}{tw}\r\033[1;36m{rw}{cw}\033[0m", end="")
			break

		if '\t' in cw:
			rw += cw if len(t.suggestions) <= 1 else t.suggestions[1]+' '
			cw = ""

		if ' ' in cw:
			rw += cw
			cw = ""

		if '\x7f' in cw:
			cw = cw[:-2]

		t.getAutoSugg(cw)

		tw = "" if len(t.suggestions) <= 1 or len(cw) == 0 else t.suggestions[1]

		print(' '*50, end='\r')
		print(f"{prompt}\033[1;97m{rw}{tw}\r\033[1;36m{rw}{cw}\033[0m", end="")
	
	print("")

	return rw

def passwdIn(prompt:str, mask:str):
	
	cw = ""

	while True:

		cw += getch.getch()
		msk = mask*len(cw)

		if '\x7f' in cw:
			cw = cw[:-2]

		if '\r' in cw: 
			print(" "*50, end='\r')
			print(f"{prompt}{msk[:-2]}", end="")
			break

		print(" "*50, end='\r')
		print(f"{prompt}{msk}", end="")

	print("")
	return cw

if __name__ == '__main__':
	x = passwdIn("PASSWORD ", "*") #iInput("", open('words.txt','r').read().split('\n'))
	print(x)
