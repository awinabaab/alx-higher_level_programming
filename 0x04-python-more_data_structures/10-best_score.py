#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_dictionary = sorted(
                                    a_dictionary.items(),
                                    key=(lambda key: key[1]),
                                    reverse=True
                                  )
        return sorted_dictionary[0][0]
