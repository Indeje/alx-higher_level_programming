#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        best_value = float('-inf')
        for key in a_dictionary:
            best_value = max(float(a_dictionary[key]), best_value)
        best_key = [key for key in a_dictionary if a_dictionary[key] == best_value]
        return best_key[0]
    
    return None
