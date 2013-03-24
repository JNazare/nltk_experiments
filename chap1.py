from __future__ import division
from nltk.book import *

# concordance = shows every occurance of a given word
# text1.concordance("monstrous")

# similar = words that apear in a similar content to the arg word
# text1.similar("monstrous")

# common_contexts = examine contexts that are shared by arg words
# text2.common_contexts(["monstrous", 'very'])

# dispersion plot = positional info about a words in a corpus (each tick is an occurance of a word)
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties","America"])

# len = count the length (number of tokens) of a text4
# len(text2)

# token = techniqcal name for a sequence of characters

# set = the set of tokens in a text
# print sorted(set(text3))

# calculate the lexical richness of a text (how many different words are used)
def lexical_diversity(text):
	return len(text) / len(set(text))

# count the numbe rof times a specific word appears in a text
# text3.count("smote")

# count the percentage of a text taken up by a word
def percentage(text, word):
	ct = text.count(word)
	length = len(text)
	return 100 * ct / length

# FreqDist = tells us the frequency of each vocab item in the text
def mostFrequent(text, n):
	"""Gives the n most frequent terms in a text"""
	fdist = FreqDist(text)
	vocab = fdist.keys()
	return vocab[:n]
#print mostFrequent(text1, 50)

# Hapaxes = words that occur only once
def getHapaxes(text):
	fdist = FreqDist(text)
	return fdist.hapaxes()
# print getHapaxes(text1)

# Get long words 
def getLongWords(text, min_length):
	V = set(text)
	long_words = [w for w in V if len(w) > min_length]
	return long_words
# print getLongWords(text1, 15)

# Collocation = sequence of words that occur together unussually often (e.g. red wine)
# text4.collocations()

# Bigrams = list of word pairs
# bigrams(['more', 'is', 'said', 'than', 'done'])

def wordDist(text):
	"""Number of times a word with a specific length is in the text"""
	lengths = [len(w) for w in text]
	return lengths.items()

