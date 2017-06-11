from prefix import *
from suffix import *
def get_word_list(chain, prefix, random_func,n,NONWORD):
    x = get_word_list_helper(chain, prefix, random_func, n, NONWORD)
    return x
    #return get_word_list_helper(chain, prefix, random_func, n, NONWORD)

def get_word_list_helper(chain, prefix, random_func, n, NONWORD, curr_tuple = ()):
    if n == 0:
        return curr_tuple
    else:
        random_word = choose_word(chain, prefix, random_func)
        if random_word == NONWORD:
            return curr_tuple
        word_tuple = (random_word,)
        new_tuple = curr_tuple + word_tuple
        prefix2 = shift_in(prefix, random_word)
        return get_word_list_helper(chain, prefix2, random_func, n-1, NONWORD, new_tuple)

def generate(chain, random_func, n, NONWORD):
    init_prefix = (NONWORD, NONWORD)
    word_tuple = get_word_list(chain, init_prefix, random_func, n, NONWORD)
    s = map(lambda x: str(x), word_tuple)
    s_list = list(s)
    string = reduce(lambda x,y: x + " " + y, s_list, "")
    return string