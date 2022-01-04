from typing import List

import nltk
from nltk.corpus import words as all_english_words
from nltk.tokenize import SyllableTokenizer

# make sure nltk data is downloaded before trying to access the corpus
nltk.download('words')

corpus = all_english_words

# load corpus into memory
words: List[str] = corpus.words()

# filter words by starting letter, 'B' for first name and 'C' for last name
b_words = filter(lambda word: word.casefold().startswith('b'), words)
c_words = filter(lambda word: word.casefold().startswith('c'), words)

# use sonority sequencing tokenizer
SSP = SyllableTokenizer()


# convenience function to count number of syllables in a word
def syl_count(word):
    return len(SSP.tokenize(word))


# programmatically count syllables from target words
first_syllable_count = syl_count('Benedict')
last_syllable_count = syl_count('Cumberbatch')

# export potential first and last names
firsts = list(
    filter(lambda word: syl_count(word) == first_syllable_count, b_words))
lasts = list(
    filter(lambda word: syl_count(word) == last_syllable_count, c_words))
