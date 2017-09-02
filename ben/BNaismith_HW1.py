
# coding: utf-8

# Ben Naismith  
# ben.naismith@pitt.edu  
# September 1st, 2017
# 
# Data set information:
# - Name: SUBTLEX-UK: Subtitle-based word frequencies for British English
# - Description: frequency data relating to lexis in subtitles from BBC broadcasts (adult and children programming)
# - The authors: Van Heuven, W.J.B., Mandera, P., Keuleers, E., & Brysbaert, M.
# - Website URL: http://crr.ugent.be/archives/1423
# - Download URL: http://crr.ugent.be/papers/SUBTLEX-UK.xlsx
# 
# Makeup:
# - size: based on corpus of 201.3 million words. Frequency data sets have 160,022 clean entries and 332,987 uncleaned entries. The data set analyzed here is the clean entries.
# - time period: Jan 2010 - Dec 2012
# - format: single text file
# 
# License: Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License. (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US)
# 
# Other information:
# - similar data set exists for American version
# - claims to be more reliable than written text corpora for psycholinguistic research
# - available tool for online searches
# 

# The code below takes a messy text file and peforms the following operations:
# * Reads in the text
# * Turns each word/number into a separate item by splitting the text whenever there is a tab or new line
# * Creates lists for 'Data categories', 'Word types', and 'Word frequencies'
# * Prints out some basic stats including the different categories and number of categories, total number of word types, the frequency counts of the top 10 most frequent words, and the average word frequency of the types in the data set

# My one discovery was in relation to the frequency distribution. When comparing the different frequency bands, the top 10 most frequent words account for nearly 0.1% of the entire corpus, and that the top 100 are nearly equal to the top 1000 combined.

# In[1]:

import numpy

#Read-in data set SUBTLEX-UK

f = open('/Users/Benjamin\'s/Documents/Data_Science/HW1-Repo/ben/data/SUBTLEX.txt', 'r')
text = f.read()
f.close()

#separating items in text file (categories and data points)
lines = text.split("\n")
items = [x.split("\t") for x in lines]

#separating categories from other data
categories = items[0]
data = items[1:-1]

print("There are", len(categories), "data categories in the SUBTLEX-UK corpus. These categories are:")
print("\n", categories)

#creating list of types and list of frequencies (the second one as integers)
types = [i[0] for i in data]
freq = [i[1] for i in data[:-1]]
freqint = [int(i) for i in freq[:-1]]

print("\n There are", len(types), "types in the SUBTLEX-UK corpus")
print("\n The mean average word frequency in this data set is", numpy.mean(freqint))

#print top 10 most frequent types and their frequencies
print("\n The top 10 most frequent words in the SUBTLEX-UK corpus are:")

for i in data[:10]:
      print("  - ", i[0], i[1])

print("\n The following are the percentage of total tokens accounted for by different frequency bands:")

print("  - Top 10:", round(numpy.sum(freqint[:10])/numpy.sum(freqint), 6))
print("  - Top 100:", round(numpy.sum(freqint[:100])/numpy.sum(freqint), 6))
print("  - Top 500:", round(numpy.sum(freqint[:500])/numpy.sum(freqint), 6))
print("  - Top 1000:", round(numpy.sum(freqint[:1000])/numpy.sum(freqint), 6))


# Tasks I was unable to perform but would have liked to include,
# * finding a simple way to link category indices to the respective data
# * other techniques for dealing with messy data which is all in one jumbled text file
# * creating visuals and graphs based on the data provided, for example for the frequency distribution
