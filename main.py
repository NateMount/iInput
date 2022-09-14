import trie
from util import GetchUnix

getc = GetchUnix()

def main():
	t = trie.Trie()
	t.formTrie(trie.keys)

	word = ""

	while True:
		word += getc()

		if '`' in word:
			break

		t.getAutoSugg(word)

		top = t.suggestions[-1]
		print(" "*50,end="\r")
		print(f"\033[1;97m{top}\r\033[1;36m{word}\033[0m", end ="")


if __name__ == '__main__':
	main()
