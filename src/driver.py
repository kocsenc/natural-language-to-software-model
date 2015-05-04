#!usr/bin/env python3
__author__ = 'David Kisluk'

import argparse
import json
import nltk

def main():
    # parse args
    input_file = ''
    output_file = ''

    args = parse_args()
        
    input_file = args.infile
    output_file = args.outfile
    
    # In comes the text (filename)
    f = open(input_file)
    raw_text = f.read()

    # Use nltk to tokenize text.
    tokens = nltk.word_tokenize(raw_text)

    # Normalize tokenize text (lowercase)
    words = [w.lower() for w in tokens if w.isalpha()]

    # mark words with POS tags
    tagged_words = nltk.pos_tag(words)

    # Gather nouns => Stem nouns
    nouns = [w for w in tagged_words if w[1].startswith('N')] 
    untagged_nouns = nltk.Text([noun[0] for noun in nouns])
    noun_freq_dist = nltk.FreqDist(untagged_nouns)

    # Gather verbs =>
    verbs = [w for w in tagged_words if w[1].startswith('V')]
    untagged_verbs = nltk.Text([verb[0] for verb in verbs])
    verbs_freq_dist = nltk.FreqDist(untagged_verbs)

    # Algorithm to go through nouns and verbs to relate them

    # Filter results using hapaxes

    pass
    
def parse_args():
    """Parses command line arguments and returns a collection of them"""

    parser = argparse.ArgumentParser()

    format_group = parser.add_mutually_exclusive_group()
    format_group.add_argument("-j", "--json", action="store_true")
    format_group.add_argument("-x", "--xml", action="store_true")

    parser.add_argument("infile", help="the input file")
    parser.add_argument("outfile", help="the output file")

    return parser.parse_args()

if __name__ == "__main__":
    main()

