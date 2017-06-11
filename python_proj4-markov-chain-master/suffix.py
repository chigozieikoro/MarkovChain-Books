from immdict import ImmDict
from functools import *

def empty_suffix():
    return ImmDict()

def add_word(suffix, word):
    if suffix.get(word) == None:
        new_dict = suffix.put(word, 1)
        return new_dict
        #dictionary.put(word, 1)
    else:
        value = suffix.get(word)
        freq = value + 1
        new_dict = suffix.put(word, freq)
        return new_dict

def choose_word(chain, prefix, randomizer):
    suffix = chain.get(prefix)
    values = suffix.values()
    denom = reduce(lambda x, y: x + y, values)
    random = randomizer(denom)
    dict_list = suffix.items()
    list_map = map(lambda x: [x[0]] * x[1], dict_list)
    converted_map = list(list_map)
    reduced_mapping = reduce(lambda x, y: x + y, converted_map, [])
    element = reduced_mapping[random-1]
    return element







#xy = [[1,2,3,4,4],[4,5,4],[5]]

