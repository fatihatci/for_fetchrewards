import math, string, sys
from collections import Counter

#expands abbreviated words (i.e. you're -> you are, won't -> will not)
def expand_abbreviations(text):
	expanded = text
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
                        '\'m': ' am'}
	for key, value in abbr_to_replace.items():
		expanded = expanded.replace(key, value)

	return expanded
    

# returns list of the words in the text 
def get_words(text, expand_abbr):  
    
	# translation table is mapping uppercases to lowers and punctuations to spaces 
    translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)
    
    if expand_abbr:
    	text = expand_abbreviations(text)
        
    text = text.translate(translation_table) 
    word_list = text.split() 
      
    return word_list 
  
# returns dictionary of word frequency. 
def analyze_text(text, text_no, expand_abbr):  
      
    word_list = get_words(text, expand_abbr) 
    freq_mapping = Counter(word_list)
  
    print("Text", text_no, ":", len(word_list), "words, ", len(freq_mapping), "distinct words") 
  
    return freq_mapping 
  
  
# returns the dot product of two documents 
def dot_product(D1, D2):  
	Sum = 0.0
	shared = 0
      
	for key in D1: 
		if key in D2: 
			Sum += (D1[key] * D2[key])
			shared += min(D1[key], D2[key])

	if D1 != D2:
		print("Shared :", shared)
        
	return Sum
  
# calculates the cosine similarity 
def score_similarity(D1, D2):

    numerator = dot_product(D1, D2) 
    denominator = math.sqrt(dot_product(D1, D1) * dot_product(D2, D2)) 
        
    return numerator/denominator 
    
def similarity(text_1, text_2, expand_abbr): 
      
    mapped_text_1 = analyze_text(text_1, 1, expand_abbr) 
    mapped_text_2 = analyze_text(text_2, 2, expand_abbr) 
    score = score_similarity(mapped_text_1, mapped_text_2) 
      
    print("The similarity score between the documents is: % 0.3f "% score, "(abbreviations expanded)"*expand_abbr, '\n') 

# run code for test texts
if __name__ == '__main__':   

    t1="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    t2="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    t3="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

    # if 3rd argument is set to 1, then abbreviations will be expanded (i.e. you're -> you are, won't -> will not) 
    similarity(t1, t2, 0)
    similarity(t1, t2, 1)

    similarity(t1, t3, 0)
    similarity(t1, t3, 1)

    similarity(t2, t3, 0)
    similarity(t2, t3, 1)


