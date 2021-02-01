# for_fetchrewards
# Coded by: Fatih ATCI
# Date: 2/1/21

* This repo is for fetch rewards interview exercise.

* Just run the code in a Python 3.x environment.

* Texts to be compared are defined in the code.

* The code creates a dictionary of frequencies (a vector) of words in each text and then calculates a similarity score based on cosine similarity algorithm.

* Based on preferance, abbreviations can be expanded (i.e. you're -> you are, won't -> will not)
  Below is the translation table for abbreviations:
  abbr_to_replace = {'won\'t': 'will not',
		     'don\'t': 'do not',
                     'can\'t': 'can not',
                     'haven\'t': 'have not',
                     'mustn\'t': 'must not',
                     'didn\'t': 'did not',
                     'isn\'t': 'is not',
                     'aren\'t': 'are not',
                     '\'ll': ' will',
                     '\'re': ' are',
                     '\'m': ' am',
		     '\'ve': ' have'}
