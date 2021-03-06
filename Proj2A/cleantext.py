#!/usr/bin/env python3

"""Clean comment text for easier parsing."""

from __future__ import print_function

import re
import string
import argparse
import json

__author__ = ""
__email__ = ""

# You may need to write regular expressions.


def sanitize(text):
    """Do parse the text in variable "text" according to the spec, and return
    a LIST containing FOUR strings 
    1. The parsed text.
    2. The unigrams
    3. The bigrams
    4. The trigrams
    """
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = re.sub('\[([\s\S]+)\] \((https?:\/\/)?(www.)?\w+\.\w+\)','\\1',text)
    parsed_text = re.findall('[\w\-\']+|[.,;:?!]', text)
    for i in range(len(parsed_text)):
        parsed_text[i] = (parsed_text[i]).lower()
    parsed_text = list(filter(None,parsed_text))
    parsed_text_str = ' '.join(parsed_text)
    u_sequences = re.findall('[\w\-\']+',parsed_text_str) 
    b_sequences = [u_sequences[i:i+2] for i in range(len(u_sequences)-1)]
    t_sequences = [u_sequences[i:i+3] for i in range(len(u_sequences)-2)]
    unigrams_str = ' '.join(u_sequences)
    bigrams = ['_'.join(b_sequence) for b_sequence in b_sequences]
    bigrams_str = ' '.join(bigrams)
    trigrams = ['_'.join(t_sequence) for t_sequence in t_sequences] 
    trigrams_str = ' '.join(trigrams)
    return [parsed_text_str, unigrams_str, bigrams_str, trigrams_str]


if __name__ == "__main__":
    data = []
    with open('../sample.json','r') as f:
        for line in f:
            data.append(json.loads(line))
   
    print(sanitize(data[4]['body']))

    # This is the Python main function.
    # You should be able to run
    # python cleantext.py <filename>
    # and this "main" function will open the file,
    # read it line by line, extract the proper value from the JSON,
    # pass to "sanitize" and print the result as a list.

    # YOUR CODE GOES BELOW.

    # We are "requiring" your write a main function so you can
    # debug your code. It will not be graded.
