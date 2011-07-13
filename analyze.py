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
