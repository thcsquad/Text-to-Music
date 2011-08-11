#!/usr/bin/python

import pysynth
from math import log

def wordlen_to_notelen(wordlen):
  return pow(2, int(log(16/int(wordlen), 2) + 0.5))

def createWav(word_lengths):
  note_lengths = map(wordlen_to_notelen, word_lengths)
  print note_lengths 
