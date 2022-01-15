# Annie Kuo

# This module contains several functions to compute the similarity between two vectors.

# IMPORT MODULES
import doctest
from vectors_utils import *



# DEFINE FUNCTIONS
def get_semantic_descriptor(keyword, sentence):
    """ (str, list) -> dict
    
    The function takes as input a string representing a single word
    and a list representing all the words in a sentence.
    It returns a dictionary representing the semantic descriptor vector
    of the word computed from the sentence.
    
    >>> s1 = ['hello', 'to', 'anyone', 'reading', 'this', 'short', 'example']
    >>> desc1 = get_semantic_descriptor('reading', s1)
    >>> desc1['hello']
    1
    >>> len(desc1)
    6
    >>> 'everyone' in desc1
    False
    
    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal']
    >>> desc2 = get_semantic_descriptor('animal', s2)
    >>> desc2 == {'no': 1, 'must': 1, 'ever': 1, 'kill': 1, 'any': 1, 'other': 1}
    True
    >>> get_semantic_descriptor('animal', s1)
    {}
    
    >>> s3 = ['jingle', 'bells', 'jingle', 'bells', 'jingle', 'all', 'the', 'way']
    >>> desc3 = get_semantic_descriptor('way', s3)
    >>> len(desc3) == 4
    True
    >>> desc3 == {'jingle' : 3, 'bells' : 2, 'all' : 1, 'the' : 1}
    True
    >>> 'bell' in desc3
    False
    """
    # initialize an empty dictionary
    semantic_descriptor = {}
    
    # in case the keyword is not part of the sentence
    if keyword not in sentence:
        return semantic_descriptor
    
    # in case the keyword is part of the sentence
    else:
        # count the occurence of each word in sentence
        for word in sentence:
            if word == keyword:
                continue
            elif word in semantic_descriptor:
                semantic_descriptor[word] += 1
            else:
                semantic_descriptor[word] = 1 
    
    # return the word's semantic descriptor vector
    return semantic_descriptor


def get_all_semantic_descriptors(text):
    """ (list) -> dict
    
    The function takes as input a list of lists representing the words in a text,
    where each sentence in a text is represented by a sublist of the input list.
    It returns a dictionary such that for every word w that appears in at least
    one of the sentences d[w] is itself a dictionary which represents the semantic
    descriptor vector of w.
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    
    >>> s = [['jingle', 'bells', 'jingle', 'bells'], \
    ['jingle', 'all', 'the', 'way'], \
    ['oh', 'what', 'fun', 'it', 'is', 'to', 'ride'], \
    ['in', 'a', 'one', 'horse', 'open', 'sleigh'], \
    ['hey', 'jingle', 'bells', 'jingle', 'bells']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['bells']['jingle']
    8
    >>> d['jingle'] == {'bells' : 8, 'all' : 1, 'the' : 1, 'way' : 1, 'hey': 2}
    True
    >>> d['horse'] == {'in' : 1, 'a' : 1, 'one': 1, 'open' : 1, 'sleigh' : 1}
    True
    
    >>> s = [['the', 'wheels', 'on', 'the', 'bus', 'go', 'round', 'and', 'round'], \
    ['round', 'and', 'round'], \
    ['round', 'and', 'round'], \
    ['the', 'wheels', 'on', 'the', 'bus', 'go', 'round', 'and', 'round'], \
    ['all', 'through', 'the', 'town']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['the']['wheels']
    4
    >>> d['round']['and']
    8
    >>> d['wheels'] == {'the': 4, 'on': 2, 'bus' : 2, 'go' : 2, 'round' : 4, 'and' : 2}
    True
    """
    # initialize an empty dictionary
    semantic_descs = {}
    
    # retrieve the semantic descriptor for each word
    for sentence in text:
        for word in sentence:
            sem_desc = get_semantic_descriptor(word, sentence)
            
            # in case the word appears more than once in the text
            # add the word's semantic descriptor vectors together
            if word in semantic_descs:
                add_vectors(semantic_descs[word], sem_desc)
            
            # in case this is the first time the word appears in the text
            else:
                semantic_descs[word] = sem_desc
    
    # return the dictionary of semantic descriptor vectors
    return semantic_descs

    
def get_cos_sim(first_vector, second_vector):
    """ (dict, dict) -> float

    The function takes as input two dictionaries representing similarity descriptor vectors.
    It returns the cosine similarity between the two.
    
    >>> round(get_cos_sim({"a": 5, "b": 3, "c": 2}, {"b": -4, "c": 5, "d": 5}), 4)
    -0.0399
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_cos_sim(v1, v2), 4)
    0.0595
    
    >>> get_cos_sim({"a": 1, "b": 2, "c": 3}, {})
    Traceback (most recent call last):
    ZeroDivisionError: float division by zero
    
    >>> get_cos_sim({"a": 1, "b": 1}, {"a": -1, "b": 1})
    0.0
    """
    # calculate the dot product
    dot_product = get_dot_product(first_vector, second_vector)
    
    # calculate each vector's norm
    first_norm = get_vector_norm(first_vector)
    second_norm = get_vector_norm(second_vector)
    
    # calculate and return the cosine similarity
    cosine_sim = dot_product / (first_norm * second_norm)
    return cosine_sim
    
    
def get_euc_sim(first_vector, second_vector):
    """ (dict, dict) -> float
    
    The function takes as input two dictionaries representing similarity descriptor vectors.
    It returns the similarity between the two using the negative euclidean distance.
    
    >>> round(get_euc_sim({"a": 5, "b": 5, "c": 5}, {"b": 4, "c": 5, "d": 6}), 3)
    -7.874
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_euc_sim(v1, v2), 4)
    -7.1414
    
    >>> round(get_euc_sim({"a": 1, "b": 2, "c": 3}, {}), 3)
    -3.742
    
    >>> get_euc_sim({}, {})
    -0.0
    
    >>> get_euc_sim({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3})
    -0.0
    """
    # calculate the vector difference
    vector_difference = sub_vectors(first_vector, second_vector)
    
    # calculate and return the negative euclidean distance
    euc_sim = -get_vector_norm(vector_difference)
    return euc_sim


def get_norm_euc_sim(first_vector, second_vector):
    """ (dict, dict) -> float
    
    The function takes as input two dictionaries representing similarity descriptor vectors.
    It returns the similarity between the two using the negative euclidean distance
    between the normalized vectors.
    
    >>> round(get_norm_euc_sim({"a": 5, "b": 5, "c": 3}, {"b": 2, "c": 3, "d": 6}), 3)
    -1.137
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_norm_euc_sim(v1, v2), 4)
    -1.3715
    
    >>> get_norm_euc_sim({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3})
    -0.0
    
    >>> get_norm_euc_sim({}, {})
    -0.0
    """
    # make copies of the dictionaries
    first_vector_c = copy_dict(first_vector)
    second_vector_c = copy_dict(second_vector)
    
    # normalized the vectors
    normalize_vector(first_vector_c)
    normalize_vector(second_vector_c)
    
    # calculate and return the similarity
    norm_euc_sim = get_euc_sim(first_vector_c, second_vector_c) 
    return norm_euc_sim
    


# TEST MODULE
if __name__ == "__main__":
    doctest.testmod() 