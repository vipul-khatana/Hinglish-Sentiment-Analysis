# -*- coding: utf-8 -*-
import re
_ascii_letters = re.compile(r'[a-zA-Z0-9/.:-]', flags=re.UNICODE)

def only_nonascii(text):
    return _ascii_letters.sub("", text)

swords = open('stopwords.txt','r').read().split('\n')
swords.pop()

def removeStopWords(data):
	data = only_nonascii(data)

	data = data.split(' ')

	clean = []

	for word in data:
		if len(word)>=3 and word not in swords:
			clean.append(word)

	return ' '.join(clean)


def preProcess(data):
	data = removeStopWords(data)
	#data = negDis(data)

	return data