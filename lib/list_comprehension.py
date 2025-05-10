#!/usr/bin/env python3

#A function that returns even numbers 
def return_evens(num_list):
    evens_nums = [n for n in num_list if n % 2 ==0]
    return evens_nums

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]