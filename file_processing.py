# Annie Kuo

# This module contains several functions that allow us to read a file
# and extract a dictionary of semantic descriptors from it.

# IMPORT MODULES
import doctest
from similarity_measures import *



# DEFINE FUNCTIONS
def get_sentences(text):
    """ (str) -> list
    
    The function takes as input a string. It returns a list of strings
    each representing one of the sentences from the input string.
    
    >>> t = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(t)
    ['No animal must ever kill any other animal', 'All animals are equal']
    
    >>> t = "Hello! How are you? I'm doing fine, thank you."
    >>> get_sentences(t)
    ['Hello', 'How are you', "I'm doing fine, thank you"]
    
    >>> t = "A sentence without ending punctuation"
    >>> get_sentences(t)
    ['A sentence without ending punctuation']
    
    >>> t = "Hey!I am Groot.Who are you?" # no space behind punctuation
    >>> get_sentences(t)
    ['Hey', 'I am Groot', 'Who are you']
    
    >>> t = ""
    >>> get_sentences(t)
    []
    
    >>> t = " "
    >>> get_sentences(t)
    []
    """
    # initialize variables
    sentences = []
    start = 0
    
    # locate the punctuation that separates sentences
    # by iterating through each character
    for index in range(len(text)):
        if text[index] in ".!?":
            # add the sentence to the list of sentences
            sentence = text[start : index]
            if sentence != "":
                sentences.append(sentence.strip())
            # mark the start of the next sentence
            start = index + 1
    
    # in case the sentence does not have an ending punctuation
    if (len(text) >= 1) and (text[-1] not in ".!?\" "):
        sentences.append(text[start : ])

    # return the list of sentences
    return sentences
            

def get_words(sentence):
    """ (str) -> list
    
    The function takes as input a string representing a sentence.
    It returns a list of the words from the input string.
    
    >>> s = "How wonderful it is that nobody need wait a single moment before starting to improve the world"
    >>> x = get_words(s)
    >>> x == ['How', 'wonderful', 'it', 'is', 'that', 'nobody', 'need', 'wait', 'a', \
    'single', 'moment', 'before', 'starting', 'to', 'improve', 'the', 'world']
    True
    
    >>> s = "Today, I will be staying home all day"
    >>> get_words(s)
    ['Today', 'I', 'will', 'be', 'staying', 'home', 'all', 'day']
    
    >>> s = "Okay; here's a pretty-punctuated sentence: 'Hi, -- how are you'"
    >>> get_words(s)
    ['Okay', 'here', 's', 'a', 'pretty', 'punctuated', 'sentence', 'Hi', 'how', 'are', 'you']
    
    >>> s = ""
    >>> get_words(s)
    []
    """
    # define punctuation symbols that separate phrases                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    punctuations = [',', '-', '--', ':', ';', '"', "'"]
    
    # replace the punctuation by white spaces
    for punctuation in punctuations:
        sentence = sentence.replace(punctuation, " ")
    
    # split the sentence into words depending on where white spaces are
    words = sentence.split()
    
    # return the list of words from the input sentence
    return words


def get_word_breakdown(text):
    """ (str) -> list
    
    The function takes as input a string. It returns a 2D lists of strings.
    Each sublist contains a strings representing words from each sentence.
    
    >>> text = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his \
    own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill \
    any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text)
    >>> s == w
    True
    
    >>> t = "That's all anybody can do right now. Live. Hold out. \
    Survive. I don't know whether good times are coming back again. But \
    I know that won't matter if we don't survive these times."
    >>> s = [["that", "s", "all", "anybody", "can", "do", "right", "now"], ["live"], ["hold", "out"], \
    ["survive"], ["i", "don", "t", "know", "whether", "good", "times", "are", "coming", "back", "again"],\
    ["but", "i", "know", "that", "won", "t", "matter", "if", "we", "don", "t", "survive", "these", "times"]]
    >>> w = get_word_breakdown(t)
    >>> s == w
    True
    
    >>> text = ""
    >>> get_word_breakdown(text)
    []
    """
    # initialize variable to store list to be returned
    list_of_strings = []
    
    # make sure the text is completely in lowercase
    text = text.lower()
    
    # separate the text into sentences
    sentences = get_sentences(text)
    
    # separate each sentence into words
    for sentence in sentences:
        list_of_strings += [get_words(sentence)]
    
    # return the list of strings
    return list_of_strings
        
  
def build_semantic_descriptors_from_files(files):
    """ (list) -> dict
    
    The function takes a list of file names as input.
    It returns a dictionary of semantic descriptors of
    all the words in the files received as input.
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    
    >>> d = build_semantic_descriptors_from_files(['alice.txt'])
    >>> d['king']['the']
    4
    >>> 'first' in d['king']
    True
    >>> len(d['clever'])
    19
    
    >>> d = build_semantic_descriptors_from_files(['alice.txt', 'animal_farm.txt'])
    >>> len(d['clever'])
    27
    >>> 'weak' in d['clever']
    True
    >>> len(d['all'])
    26
    """
    # initialize variable
    all_semantic_descriptors = {}
    
    # get the semantic descriptor vectors for each word of each file
    for filename in files:
        # open file
        fobj = open(filename, "r", encoding="utf-8")
        file_content= fobj.read()
        
        # separate the text into words
        file_words = get_word_breakdown(file_content)
        
        # get the semantic descriptor vectors for those words
        sem_desc = get_all_semantic_descriptors(file_words)
        
        # merge the semantic descriptor with the ones from previous files
        merge_dicts_of_vectors(all_semantic_descriptors, sem_desc)
        
        # close file
        fobj.close()
    
    # return the dictionary
    return all_semantic_descriptors


# TEST MODULE
if __name__ == "__main__":
    doctest.testmod() 