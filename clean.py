import string
import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import sys

# Cleans csv files of actual twitter data: remove punctuation, stopwords (as defined by nltk), links

folder = sys.argv[1]

if folder == 'raw_data':
	keyword = sys.argv[2]
	week = sys.argv[3]
	file_in = folder + '/' + keyword + '/' + keyword + '_' + week + '.csv'
	file_out = folder + '/' + keyword + '_' + week + '.txt'
else:
	month = sys.argv[2]
	file_in = folder + '/' + month + '.csv'
	file_out = month + '.txt'

str = ''
    
reader = csv.reader(open(file_in))
for row in reader:
    # remove links
    toAdd = re.sub(r'\S+.com\S+|http\S+|\S+http\S+', '', row[6])
    str = str + " " +(toAdd)
    
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(str) 
  
filtered = [w.lower() for w in word_tokens if not w.lower() in stop_words and w.isalpha()] 
            
# return filtered list as string
cleaned = (" ").join(filtered)

text_file = open(file_out, "w+")
text_file.write(cleaned)