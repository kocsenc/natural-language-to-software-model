#!usr/bin/env python3

import sys, getopt

def main(argv):
    # parse args
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    # In comes the text (filename)
    # Use nltk to tokenize text.

    # Normalize tokenize text (lowercase)

    # Gather nouns => Stem nouns
    # Gather verbs =>

    # Algorithm to go through nouns and verbs to relate them

    # Filter results using hapaxes

    pass

def print_help():
    print('driver.py -i <inputfile> -o <outputfile>')

if __name__ == "__main__":
    main(sys.argv[1:])

