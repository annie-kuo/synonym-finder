# Annie Kuo

# This module contains functions that allows our program to answer synonym questions

# IMPORT MODULES
from file_processing import *
import matplotlib.pyplot as plt
import doctest



# DEFINE FUNCTIONS
def most_sim_word(word, choices, semantic_descriptors, similarity_fn):
    """ (str, list, dict, function) -> str
    
    The function returns the element of choices which has the largest
    semantic similarity to word, with the semantic similarity computed
    using the data in semantic_descriptors and the similarity function
    similarity_fn.

    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices, sem_descs, get_cos_sim)
    'cat'
    
    >>> choices = ['fruit', 'color', 'gender', 'autumn']
    >>> f = {'orange' : 3, 'avocado' : 2, 'sweet' : 2, 'green' : 1}
    >>> c = {'orange' : 2, 'red' : 5, 'dark' : 1, 'blue' : 6, 'yellow' : 1}
    >>> g = {'male' : 4, 'neutral' : 1, 'female' : 2, 'she' : 4, 'they' : 3, 'he' : 3}
    >>> a = {'fall' : 2, 'leaves' : 4, 'red' : 3, 'green' : 1}
    >>> s = {'fall' : 6, 'red' : 3, 'blue' : 2, 'winter' : 2, 'green' : 3}
    >>> sem_descs = {'fruit' : f, 'color' : c, 'gender' : g, 'autumn' : a, 'season' : s}
    >>> most_sim_word('season', choices, sem_descs, get_euc_sim)
    'autumn'
    
    >>> r = {'red' : 2, 'orange' : 2, 'yellow' : 1, 'green' : 4, 'blue' : 1, 'indigo' : 3, 'violet' : 1}
    >>> sem_descs['rainbow'] = r
    >>> most_sim_word('rainbow', choices, sem_descs, get_norm_euc_sim)
    'color'
    
    >>> choices = ['question', 'nothing']
    >>> q = {'how' : 2, 'why' : 3, 'who' : 1, 'what' : 2, 'when' : 4}
    >>> n = {}
    >>> g = {'hi' : 2, 'how' : 2, 'are' : 1, 'you' : 1}
    >>> sem_descs = {'question' : q, 'nothing' : n, 'greeting' : g}
    >>> round(get_cos_sim(sem_descs['greeting'], sem_descs['question']),3)
    0.217
    >>> get_cos_sim(sem_descs['greeting'], sem_descs['nothing']) # cannot be computed
    Traceback (most recent call last):
    ZeroDivisionError: float division by zero
    >>> most_sim_word('greeting', choices, sem_descs, get_cos_sim) # sim_word for 'nothing' = -inf
    'question'
    
    >>> choices = ['a', 'b']
    >>> a = {'d': 1, 'e': 1}
    >>> b = {'d': 1, 'f': 1}
    >>> c = {'d': 1, 'e': 1, 'f' : 1}
    >>> sem_descs = {'a' : a, 'b' : b, 'c' : c}
    >>> round(get_cos_sim(sem_descs['c'], sem_descs['a']),3)
    0.816
    >>> round(get_cos_sim(sem_descs['c'], sem_descs['b']),3)
    0.816
    >>> most_sim_word('c', choices, sem_descs, get_cos_sim) # tie
    'a'
    
    >>> choices = ['a', 'b']
    >>> sem_descs = {'a' : {}, 'b' : {}, 'c' : {}}
    >>> most_sim_word('c', choices, sem_descs, get_cos_sim) # all has sim of -inf
    ''
    """
    # initialize a variable to store all the semantic similarities
    all_sem_sim = []
    
    # compute the semantic similarity of each choice to word
    for choice in choices:
        try:
            sem_sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
            # add the semantic similarity to the list of all semantic similarities
            all_sem_sim.append(sem_sim)
        # in case the semantic similarity between two words cannot be computed
        except (ZeroDivisionError, KeyError):
            sem_sim = float('-inf')
            all_sem_sim.append(sem_sim)
    
    # determine the largest semantic similarity to word
    max_sem_sim = max(all_sem_sim)
    if max_sem_sim == float('-inf'):
        return ""
    
    # determine the index of the first occurence of the
    # largest semantic similarity to word
    max_index = all_sem_sim.index(max_sem_sim)
    
    # return the choice at that index
    return choices[max_index]
    

def run_sim_test(filename, semantic_descriptors, similarity_fn):
    """ (str, dict, function) -> float
    
    The function returns the percentage (between 0.0 and 100.0) of question on which
    most_sim_word guesses the answer correctly using the semantic descriptors
    stored in semantic_descriptors and the similarity function similarity_fn.
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    15.0
    >>> run_sim_test('test.txt', descriptors, get_euc_sim)
    20.0
    >>> run_sim_test('test.txt', descriptors, get_norm_euc_sim)
    15.0
    
    >>> descriptors = build_semantic_descriptors_from_files(['war_and_peace.txt', 'swanns_way.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    67.5
    >>> run_sim_test('test.txt', descriptors, get_norm_euc_sim)
    67.5
    >>> run_sim_test('test.txt', descriptors, get_euc_sim)
    35.0
    """
    # open file
    fobj= open(filename,"r", encoding= "UTF-8")
    
    # initialize counter variables
    correct_answers = 0
    num_of_lines = 0
    
    # compute the answer for every line/question based on the similarity function
    for line in fobj:
        words = line.split()
        answer = most_sim_word(words[0], words[2:], semantic_descriptors, similarity_fn)
        
        # update counter in case the answer is correct
        if answer == words[1]:
            correct_answers += 1
        
        # update the number of questions answered
        num_of_lines += 1
        
    # close file
    fobj.close()
    
    # compute and return the percentage of correct answers
    percentage = (correct_answers/num_of_lines) * 100
    return percentage


def generate_bar_graph(similarity_fn, filename):
    """ (list, str) -> NoneType
    
    The function generates a bar graph (using matplotlib) where the performance
    of each function on the given file test is plotted.
    The graph is saved in a file named synonyms_test_results.png
    
    """
    # initialize an empty list to store each function's score
    performances = []
    
    # generate the semantic descriptor vectors from the two novels
    descriptors = build_semantic_descriptors_from_files(['war_and_peace.txt', 'swanns_way.txt'])
    
    # evaluate the performance given by each similarity function
    for sim_fn in similarity_fn:
        performance = run_sim_test(filename, descriptors, sim_fn)
        # append the score to the list
        performances.append(performance)
    
    # convert the function names into strings
    for index in range(len(similarity_fn)):
        similarity_fn[index] = similarity_fn[index].__name__
    
    # plot the data
    plt.bar(similarity_fn, performances)
    
    # define the graph's properties
    plt.title("Performance Given by Different Similarity Functions")
    plt.ylabel("Score (%)", fontsize = 10)
    
    # save the graph
    plt.savefig("synonyms_test_results.png")




# TEST MODULE
if __name__ == "__main__":
    doctest.testmod() 