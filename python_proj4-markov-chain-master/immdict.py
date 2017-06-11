from functools import *
class ImmDict:

    def __init__(self, initial_val = {}):
        self.dictionary = initial_val

    def put(self, key, value):
        items = self.dictionary.items()
        dict_map = map(lambda x: {x[0]: x[1]}, items)
        dict_map_list = list(dict_map)
        final_dict_map = reduce(lambda x, y: {**x, **y}, dict_map_list, {})
        pair = {key: value}
        added_dict = {**final_dict_map, **pair}
        new_immdict = ImmDict(added_dict)
        return new_immdict


    def get(self, key):
        items = self.dictionary.items()
        mapping = filter(lambda x: x[0] == key, items)
        mapping_list = list(mapping)
        if len(mapping_list) == 0:
            return None
        else:
            return mapping_list[0][1]





    def keys(self):
        items = self.dictionary.items()
        key_map = map(lambda x: x[0], items)
        keys = list(key_map)
        return keys

    def values(self):
        items = self.dictionary.items()
        values_map = map(lambda x: x[1], items)
        values = list(values_map)
        return values

    def items(self):
        return self.dictionary.items()




