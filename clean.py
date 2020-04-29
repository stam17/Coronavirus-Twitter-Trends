import string
import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import sys

# Cleans csv files of actual twitter data: remove punctuation, stopwords (as defined by nltk), links

keyword = sys.argv[1]
week = sys.argv[2]
file_in = keyword + '/' + keyword + '_' + week + '.csv'
file_out = keyword + '_' + week + '.txt'

str = ''
    
reader = csv.reader(open(file_in))
for row in reader:
    # remove links
    toAdd = re.sub(r'\S+.com\S+|http\S+|\S+http\S+', '', row[6])
    str = str + " " +(toAdd)
    
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(str) 
  
filtered = [w.lower() for w in word_tokens if not w in stop_words and w.isalpha()] 
            
# return filtered list as string
cleaned = (" ").join(filtered)

with open(file_out, "w") as text_file:
    text_file.write(cleaned)