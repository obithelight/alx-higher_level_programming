#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        biggest_value_key = max(a_dictionary, key=a_dictionary.get) 
        return biggest_value_key
    else:
        return None
