#! /usr/bin/env python3.10

import sys

class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()
		self.suggestions = []
	
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
			self.suggestions.append(word)

		for a, n in node.children.items():
			self.suggestionRec(n, word + a)
	
	def getAutoSugg(self, key):
		self.suggestions = []
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

