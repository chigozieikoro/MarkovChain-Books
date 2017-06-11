from prefix import *
from suffix import *
NONWORD = '\n'

def build(file):
    generator = pairs_gen(file,line_gen)
    return build_chain(add_to_chain, generator, ImmDict())

def build_chain(prefix_func, generator, empty_imm = ImmDict()):
    chain = reduce(lambda imm_dict,tuple: prefix_func(imm_dict, tuple), generator, empty_imm)
    return chain

def add_to_chain(chain, pair):
    #Example pair: (("This", "is"), "another")
    prefix = pair[0]
    suffix = chain.get(prefix)
    if suffix != None:
        new_suffix = add_word(suffix, pair[1])
    else:
        new_suffix = add_word(empty_suffix(), pair[1])

    final_dict = chain.put(prefix, new_suffix)
    return final_dict


def line_gen(file):
    generate = line_gen_helper(file)
    for line in generate:
        yield line


def line_gen_helper(file):
    with open(file) as parse:
        return parse.readlines()

def pairs_gen(file,line_gen_func):
    generator = line_gen_func(file)

    curr_prefix = (NONWORD, NONWORD)
    i = 0
    last_word = None
    for elem in generator:
        j = 0
        words_list = elem.split()
        for word in words_list:
            if (i == 0):
                yield(curr_prefix, word)
                j = j+1
                i = i+1
            elif j == 0:
                curr_prefix = shift_in(curr_prefix, last_word)
                yield(curr_prefix, word)
                j = j+1
            else:
                prev = words_list[j-1]
                curr_prefix = shift_in(curr_prefix, prev)
                yield(curr_prefix, word)
                j = j+1
                last_word = word

    final_prefix = shift_in(curr_prefix, last_word)
    yield (final_prefix, NONWORD)







