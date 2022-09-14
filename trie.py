#! /usr/bin/env python3.10

class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def formTrie(self, keys):
		for key in keys:
			self.insert(key)
	
	def insert(self, key):
		node = self.root

		for c in key:
			if not node.children.get(c):
				node.children[c] = TrieNode()

			node = node.children[c]

		node.isEnd = True
	
	def suggestionRec(self, node, word):
		if node.isEnd:
			print(word)

		for a, n in node.children.items():
			self.suggestionRec(n, word + a)
	
	def printAutoSugg(self, key):
		node = self.root
		for c in key:
			if not node.children.get(c):
				return 0
			node = node.children[c]

		if not node.children:
			return -1

		self.suggestionRec(node, key)
		return 1

keys = map(lambda x: x.lower(), open('words.txt','r').read().split('\n'))
#keys = ['hello','hi','hell','helvetica','homostasis', 'apple', 'app', 'arson', 'zombie']
t = Trie()
t.formTrie(keys)
print(t.root.children)

while True:
	comp = t.printAutoSugg(input("<< "))

	if comp == -1:
	    print("No other strings found with this prefix\n")
	elif comp == 0:
	    print("No string found with this prefix\n")
