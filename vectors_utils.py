# Annie Kuo

# This module contains several helper functions to work with vectors.

# IMPORT MODULES
import math
import doctest



# DEFINE FUNCTIONS
def copy_dict(dictionary):
    """ (dict) -> dict
    
    The function takes as input a dictionary and returns a deep copy of the dictionary.
    
    >>> a = {1 : 1, 2 : {2: 2}, 3 : {3: 3}}
    >>> b = copy_dict(a)
    >>> b == a
    True
    >>> id(a) == id(b)
    False
    
    >>> a = {'a' : {1: 1, 2: 2}, 'b' : "b's value", 'c' : 3, 'd' : {4: 4, 5: 5}}
    >>> b = copy_dict(a)
    >>> b == a
    True
    >>> id(a) == id(b)
    False
    >>> a['a'][1] = 2
    >>> a['a'][1] == 2
    True
    >>> b['a'][1] == 2
    False
    
    >>> a = {}
    >>> b = copy_dict(a)
    >>> a == b
    True
    >>> id(a) == id(b)
    False
    """
    # initialize a new dictionary
    copy = {}
    
    # add every key-value pair into the new dictionary
    for key in dictionary:
        # in case the value are mutable as well
        if type(dictionary[key]) in (dict, list):
            copy[key] = {}
            for subkey in dictionary[key]:
                copy[key][subkey] = dictionary[key][subkey]
        else:
            copy[key] = dictionary[key]
    
    # return the deep copy
    return copy
    
    
def add_vectors(first_vector, second_vector):
    """ (dict, dict) -> NoneType

    The function takes two dictionaries representing vectors as input.
    It adds the second vector to the first one.
    It modifies only the first input dictionary.
    
    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1['a']
    2
    >>> v1 == {'a' : 2, 'b' : 3, 'c' : 1}
    True
    >>> v2 == {'a' : 1, 'c' : 1}
    True
    
    >>> v1 = {'c' : 5, 'd' : 3, 'a' : 2, 'b' : 2}
    >>> v2 = {'a' : -2, 'c' : 3}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1['c']
    8
    >>> v1 == {'c' : 8, 'd' : 3, 'b' : 2}
    True
    >>> v2 == {'a' : -2, 'c' : 3}
    True
    
    >>> v1 = {}
    >>> v2 = {'d' : 3, 'c' : 3}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    2
    >>> v1['d']
    3
    >>> v1 == {'d' : 3, 'c' : 3}
    True
    >>> v2 == {'d' : 3, 'c' : 3}
    True
    
    >>> v1 = {}
    >>> v2 = {}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    0
    >>> v1 == {}
    True
    >>> v2 == {}
    True
    """
    # add each vector component from the second vector to the first 
    for key in second_vector:
        # in case the first vector already has such key
        if key in first_vector:
            first_vector[key] += second_vector[key]
            # delete key-value pair if its value is 0
            if first_vector[key] == 0:
                del first_vector[key]
                
        # in case the first vector has no such key
        else:
            first_vector[key] = second_vector[key]


def sub_vectors(first_vector, second_vector):
    """ (dict, dict) -> dict
    
    The function takes two dictionaries representing vectors as input.
    It substracts the second vector to the first one.
    It returns a dictionary representing the resulting vector.
    
    >>> d1 = {'a' : 3, 'b' : 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c' : -1}
    True
    >>> d1 == {'a' : 3, 'b': 2}
    True
    >>> d2 == {'a': 2, 'c': 1, 'b': 2}
    True
    
    >>> d1 = {'a' : -3, 'b' : 2, 'c' : 4}
    >>> d2 = {'a': 2, 'c': -4}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': -5, 'c' : 8, 'b' : 2}
    True
    >>> d1 == {'a' : -3, 'b' : 2, 'c' : 4}
    True
    >>> d2 == {'a': 2, 'c': -4}
    True
    
    >>> d1 = {}
    >>> d2 = {'a': 1, 'c': 3, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': -1, 'c': -3, 'b': -2}
    True
    >>> d1 == {}
    True
    >>> d2 == {'a': 1, 'c': 3, 'b': 2}
    True
    
    >>> d1 = {}
    >>> d2 = {}
    >>> d = sub_vectors(d1, d2)
    >>> d == {}
    True
    >>> d1 == {}
    True
    >>> d2 == {}
    True
    """
    # initialize the vector to be returned
    result_vector = copy_dict(first_vector)
    
    # compute each vector component of the resulting vector
    for key in second_vector:
        # in case the first vector already has such key
        if key in first_vector:
            result_vector[key] = first_vector[key] - second_vector[key]
            # delete key-value pair if its value is 0
            if result_vector[key] == 0:
                del result_vector[key]
                
        # in case the first vector has no such key
        else:
            result_vector[key] = -second_vector[key]
            
    # return the resulting vector
    return result_vector
    

def merge_dicts_of_vectors(first_dict, second_dict):
    """ (dict, dict) -> NoneType

    The function takes two dictionaries containing values
    which are dictionaries representing vectors.
    It merges the first dictionary with the second one.
    It modifies only the first input dictionary.   
    
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}} 
    >>> d2 = {'p' : {'papaya' : 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> d1['a'] == {'apple': 2}
    True
    >>> d1['p'] == {'pear': 1, 'plum': 3, 'papaya' : 6}
    True
    >>> d2 == {'p' : {'papaya' : 6}}
    True
    >>> merge_dicts_of_vectors(d2, d1)
    >>> d2['a']['apple']
    2
    >>> d2['p']['papaya']
    12
    
    >>> d1 = {'A' : {'Annie' : 1, 'Andy' : 3, 'Annabelle' : 1}, 'B' : {'Bob' : 1, 'Bella' : 1}}
    >>> d2 = {'A' : {'Anna' : 1}, 'B' : {'Bob' : 2, 'Bobby' : 1}, 'C' : {'Connie' :2}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    3
    >>> len(d1['A'])
    4
    >>> len(d1['B'])
    3
    >>> d1['A'] == {'Annie' : 1, 'Andy' : 3, 'Annabelle' : 1, 'Anna' : 1}
    True
    >>> d1['B'] == {'Bob' : 3, 'Bella' : 1, 'Bobby' : 1}
    True
    >>> d2 == {'A' : {'Anna' : 1}, 'B' : {'Bob' : 2, 'Bobby' : 1}, 'C' : {'Connie' :2}}
    True
    
    >>> d1 = {}
    >>> d2 = {1 : {}, 2 : {'a' : 1}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1[1])
    0
    >>> len(d1[2])
    1
    >>> d1[1] == {}
    True
    >>> d1[2] == {'a' : 1}
    True
    >>> d2 == {1 : {}, 2 : {'a' : 1}}
    True
    """
    # add each key-value pair from the second dictionary into the first
    for key in second_dict:
        
        # in case the first dictionary already has such key
        if key in first_dict:
            
            for sub_key, value in second_dict[key].items():
                # in case the first dictionary already has such sub-key
                # the value becomes the sum of the two vectors
                if sub_key in first_dict[key]:
                    first_dict[key][sub_key] += value
                # otherwise, add the sub-key-value pair to it
                else:
                    first_dict[key][sub_key] = value
                    
        # in case the first dictionary does not have such key   
        else:
            first_dict[key] = second_dict[key]
    
   
def get_dot_product(first_vector, second_vector):
    """ (dict, dict) -> dict 

    The function takes two dictionaries representing vectors as input.
    It returns the dot product between the two vectors.

    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10
    
    >>> v3 = {'a' : 5, 'b': 3, 'c' : 3}
    >>> v4 = {'d': 1}
    >>> get_dot_product(v3, v4)
    0
    
    >>> v5 = {}
    >>> v6 = {}
    >>> get_dot_product(v5, v6)
    0
    
    >>> v7 = {'a' : 2, 'b' : -2, 'c' : -4}
    >>> v8 = {'a' : 1, 'b' : 3, 'c' : 2}
    >>> get_dot_product(v7, v8)
    -12
    """
    # initialize dot product variable
    dot_product = 0
    
    # compute product for values whose key is in both vectors 
    for key in first_vector:
        if key in second_vector:
            # add product to the sum
            product = first_vector[key] * second_vector[key]
            dot_product += product
            
    # return sum of products (dot product)
    return dot_product
    
  
def get_vector_norm(vector):
    """ (dict) -> float

    The function takes a dictionary representing a vector as input.
    It returns the norm of such vector.
    
    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0
    
    >>> v2 = {'a': 2, 'c': 4, 'b': -2}
    >>> round(get_vector_norm(v2), 3)
    4.899
    
    >>> v3 = {}
    >>> get_vector_norm(v3)
    0.0
    """
    # compute the sum of squares
    sum_of_squares = 0
    for key in vector:
        sum_of_squares += (vector[key])**2
    
    # return the vector norm
    return math.sqrt(sum_of_squares)
  

def normalize_vector(vector):
    """ (dict) -> NoneType

    The function takes a dictionary representing a vector as input.
    the function modifies the dictionary by normalizing the vector.
    If the input vector has a norm of zero, then the vector is unchanged.
    
    >>> v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6
    >>> v1['b']
    0.8
    
    >>> v2 = {'a': 3, 'c': 1, 'b': 4, 'd' : 1}
    >>> normalize_vector(v2)
    >>> round(v2['c'], 3)
    0.192
    
    >>> v3 = {}
    >>> normalize_vector(v3)
    >>> v3 == {}
    True
    """
    # compute the vector's norm
    norm = get_vector_norm(vector)
    
    # normalize each component of the vector
    try:
        for key in vector:
            vector[key] /= norm
            
    # in case the norm is 0   
    except ZeroDivisionError:
        return
    
    

# TEST MODULE
if __name__ == "__main__":
    doctest.testmod() 
    