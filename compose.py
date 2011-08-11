#!/usr/bin/python

from __future__ import division
from midiutil.MidiFile import MIDIFile
from math import log
import random

def wordlen_to_notelen(wordlen):
	return pow(2, int(log(int(wordlen), 2) + 0.5))/4


def ratios():
	return [1/1,16/15,9/8,6/5,5/4,4/3,45/32,3/2,8/5,5/3,9/5,15/8,2/1]

def notes(key,quality):
	base_notes = dict(
	  a = 220,
		bb = 233.082,
		b = 246.942,
		c = 261.626,
		db = 277.183,
		d = 293.665,
		eb = 311.127,
		e = 329.628,
		f = 349.228,
		gb = 369.994,
		g = 391.995,
		ab = 415.305
	)

	qualities = dict(
		major = [0,2,4,5,7,9,11,12],
		minor = [0,2,3,5,7,8,10,12]
	)

	interval_ratios = ratios()
	freq = lambda x: base_notes[key] * interval_ratios[x]
	return map(freq, qualities[quality])


def cap_at(num):
	if num > 16:
		return 16
	else:
		return num

def createWav(word_lengths):
	note_lengths = map(wordlen_to_notelen, word_lengths)
	print note_lengths
	note_library = notes('c', 'major')
	print note_library
	MyMIDI = MIDIFile(1)
	MyMIDI.addTempo(0,0,120)
	total = 0.0
	for d in note_lengths:
		MyMIDI.addNote(0,0,int(note_library[random.randint(0,7)]),total,d,100)
		total += d
	
	binfile = open("output.mid", 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()
