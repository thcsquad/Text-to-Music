#!/usr/bin/python
# Text to music
# By Tristan Crockett
from nltk import FreqDist
import nltk.text
import nltk.data
import compose
import re

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
f = open('texts/the_lottery.txt', 'r')
text = f.read()

words = text.replace('\n', ' ').split(' ')
past_tense = [w for w in words if re.search('ed$', w)]
present_tense = [w for w in words if re.search('s$', w)]

t = nltk.Text(words)
pos = nltk.pos_tag(t)
print len(pos)

paragraphs = text.split('\n\n')
for i in range(0,len(paragraphs)):
	paragraphs[i] = tokenizer.tokenize(paragraphs[i])
	for j in range(0, len(paragraphs[i])):
		paragraphs[i][j] = paragraphs[i][j].split(' ')

length = lambda x: str(len(x))
#for paragraph in paragraphs:
	#for sentence in paragraph:
                #compose.createWav(map(length, sentence))
