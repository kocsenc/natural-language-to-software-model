#!usr/bin/env python3
__author__ = 'David Kisluk'

import argparse

def main():
    # parse args
    input_file = ''
    output_file = ''

    args = parse_args()
        
    input_file = args.infile
    output_file = args.outfile
    
    # In comes the text (filename)
    # Use nltk to tokenize text.

    # Normalize tokenize text (lowercase)

    # Gather nouns => Stem nouns
    # Gather verbs =>

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

