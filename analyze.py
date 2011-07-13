#!/usr/bin/python
# Text to music
# By Tristan Crockett
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
f = open('texts/the_lottery.txt', 'r')
text = f.read()
paragraphs = text.split('\n\n')
for i in range(0,len(paragraphs)):
	paragraphs[i] = tokenizer.tokenize(paragraphs[i])
	for j in range(0, len(paragraphs[i])):
		paragraphs[i][j] = paragraphs[i][j].split(' ')

length = lambda x: str(len(x))
for paragraph in paragraphs:
	for sentence in paragraph:
		print " ".join(map(length, sentence))
	print "\n"
