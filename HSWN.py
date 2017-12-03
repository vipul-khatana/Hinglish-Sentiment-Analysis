''' 
Created on Fri Nov 3 2017
@author: vipulkhatana
 '''
from difflib import SequenceMatcher

# Module to interact with the Hindi Senti Word Net

# Read the HSWN
class Word:
	
	def __init__(self,word,ppol,npol):
		self.word = word
		self.pol = ppol - npol

	def getPol(self):
		return self.pol

	def search(self,s):
		for w in self.word:
			if SequenceMatcher(a=s, b=w).ratio()>0.85:
				return True

# Contains the HSWN in memory
HSWN = []

# Searches for a word in HSWN
def searchHSWN(s):
	for word in HSWN:
		if word.search(s):
			return word.getPol()
	return 'NF'

hswn = open('HSWN.txt','r').read()
hswn = hswn.split('\n')

for line in hswn:
	parts = line.split(' ')
	words = ''.join(parts[-1:]).split(',')
	if len(words[0])>1:
		npol = float(''.join(parts[-2:-1]))
		ppol = float(''.join(parts[-3:-2]))
		HSWN.append(Word(words,ppol,npol))
