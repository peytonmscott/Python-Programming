
def all_even(lst):
    new_lst=[num for num in lst if num%2==0]
    return new_lst

def all_not_multiple(lst, n):
    new_lst = [num for num in lst if num % n != 0]
    return new_lst

def max_from_2_tuples(tuples):
    if tuples==[]:return None
    max1 = max([tuple[0] for tuple in tuples])
    max2 = max([tuple[1] for tuple in tuples])
    max_tuple=(max1, max2)
    return max_tuple


def lower_case_words(sentence):
    words_list=[word.lower() for word in sentence.split(' ') if word!='']
    return words_list


def baby_names(names, last_name):
    names_list=[y for x in [[sname+' '+name+' '+last_name for name in names if name!=sname] for sname in names] for y in x]
    return names_list


