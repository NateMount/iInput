import trie
from util import GetchUnix

getc = GetchUnix()

def main():
	t = trie.Trie()
	t.formTrie(trie.keys)

	word = ""

	while True:
		word += getc()

		c = t.printAutoSugg(word)

		if c == -1:
			print("No other strings found with this prefix")
		elif c == 0:
			print("No string found with this prefix")

if __name__ == '__main__':
	main()
