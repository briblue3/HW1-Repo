def getTokens(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    new = txt.lower()
    for s in sym :
        new = new.replace(s, " "+s+" ")
    return new.split()


def getTypeFreq(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a frequency count dictionary.
    KEY is a word, VALUE is its frequency count.
    """
    # [1] Complete this function. YOUR CODE BELOW.
    freq = {}
    for c in getTokens(txt):
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    # Use getTokens().
    return freq

def getTypes(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a alphabetically sorted list of unique word types.
    """ 
    # [2] Complete this function. YOUR CODE BELOW.
    # Use getTypeFreq().
    freq = getTypeFreq(txt)
##    for c in getTypeFreq(rose):
##        if c in freq:
##            freq[c] += 1
##        else:
##            freq[c] = 1
    return sorted(freq.keys())


def getXLengthWords(wtypes, x):
    """Takes a list of unique words (= word types) and integer x as
    arguments. Returns a sorted list of words whose length is at least x.
    """
    # [3] Complete this function. YOUR CODE BELOW.
    #wtypes  ['a', 'rose','.', 'a']
    #rosetypes = getTypes(rose)
    newlist = []
    for w in wtypes:
        if len(w) >= x:
            newlist.append(w)
    return sorted(newlist)


def getXFreqWords(freqdi, x):
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [4] Complete this function. YOUR CODE BELOW.
    anotherone = []
    for w in freqdi:
        if freqdi[w] >= x:
            anotherone.append(w)
    return sorted(anotherone)


#frequency
def getFreq(li):
    "Takes a list as input, returns a dict of freq count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] = 1
    return di

    
