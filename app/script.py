#!/usr/bin/env python3
import nltk
import os
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk import pos_tag
""" nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords') """

def generate_word_combinations(words, n=3):
    return [' '.join(words[i:i+n]) for i in range(len(words) - (n-1))]

def filter_combinations_by_pos(all_combinations, patterns):
    filtered_combinations = []
    for comb in all_combinations:
        
        words = word_tokenize(comb)
        tagged = pos_tag(words)
        pos_pattern = '-'.join([ tag for _, tag in tagged ])
        
        if any(pattern == pos_pattern for pattern in patterns):
            filtered_combinations.append(comb)
    return filtered_combinations

def filter_combinations_by_keywords(all_combinations, keywords):
    filtered_combinations = []
    for comb in all_combinations:
        if any(keyword.lower() in comb for keyword in keywords):
            filtered_combinations.append(comb)
    return filtered_combinations

def process(text, keywords=None):
    patterns = ["JJ-NN", "JJ-NN-NN", "RB-JJ-NN", "NN-IN-NN"]
    all_combinations = []
    filtered_combinations_by_keywords = []
   
            
    words = word_tokenize(text.lower())
    for i in range(2, 5):
        combinations = generate_word_combinations(words, i)
        all_combinations.extend(combinations)

    if keywords:
        filtered_combinations_by_keywords = filter_combinations_by_keywords(all_combinations, keywords)
    
    filtered_combinations = filter_combinations_by_pos(all_combinations, patterns)
    print(filtered_combinations_by_keywords)
    filtered_combinations.extend(filtered_combinations_by_keywords)
    counter = Counter(filtered_combinations)
    

    with open('script_results.txt', 'w') as file:
        for key, value in counter.most_common():
            file.write(f"{key} => {value}\n")
    

    return counter.most_common()
    


def main(text):
    keywords = []
    with open('app/keywords.txt', 'r') as file:
        for line in file:
            keywords.append(line.strip('\n'))
    print("Starting...")
    
    

    return process(text, keywords)
    
