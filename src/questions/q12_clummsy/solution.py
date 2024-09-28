from collections import defaultdict
from pprint import pprint
def q12_solution(dictionary: list[str], mistypes: list[str]):
    '''
    [
    {
      "dictionary": ["purple", "purgze","rocket", "silver", "gadget", "window", "dragon"],
      "mistypes": ["purqle", "gadgat", "socket", "salver"],
    }
]
    '''
    dict_map = {}
    for word in dictionary:
        for i in range(len(word)):
            dict_map[word[:i] + word[i + 1:]] = word


    res = []
    for word in mistypes:
        for i in range(len(word)):
            partial_word = word[:i] + word[i + 1:]
            # print(partial_word)
            if partial_word in dict_map:
                res.append(dict_map[partial_word])
                break

    print(f"dictionary={len(dictionary)}, mistypes={len(mistypes)}, res={len(res)}")
    return res

def build_freq_str(s: str):
    pass