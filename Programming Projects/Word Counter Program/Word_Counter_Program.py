# File: Week8-Word_Count.py
# Name: Adrian Rybinski
# Date: February 2, 2020
# Course: DSC 510 - Introduction to Programming
# Assignment: 8.1
# Desc: Program to open a .txt file and perform a series of actions to present a complete word count.

import string


def add_word(words, word_count_dict, counts):  # add words to dictionary
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts, word_count_dict


def pretty_print(counts, word_count_dict):  # format the printing of the list
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    print('Length of Dictionary: {}'.format(len(counts)))
    print('{:<15} {:<15}'.format('Word', 'Count'))
    print('-----------------------')
    for key, val in lst:
        print('{:<17} {:<15}'.format(val, key))


def process_line(txt_file, word_count_dict, counts):
    for line in txt_file:  # split the text into a list of words without spaces, punctuation, etc.
        line = line.strip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        add_word(words, word_count_dict,counts)
    pretty_print(counts, word_count_dict)


def main():  # main function of the program.
    word_count_dict = {}
    counts = dict()
    txt_file = open('pride.txt', 'r')
    process_line(txt_file, word_count_dict,counts)


if __name__ == "__main__":
    main()
