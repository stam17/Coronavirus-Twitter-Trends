import string
import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import sys

# Cleans csv files of actual twitter data: remove links

folder = sys.argv[1]

if folder == 'raw_data':
	keyword = sys.argv[2]
	week = sys.argv[3]
	file_in = folder + '/' + keyword + '/' + keyword + '_' + week + '.csv'
	file_out = 'cleaned_data_sent' + '/' + keyword + '/' + keyword + '_' + week + '.txt'
else:
	month = sys.argv[2]
	file_in = folder + '/' + month + '.csv'
	file_out = month + '_cleaned.txt'

lines = []
    
reader = csv.reader(open(file_in))
for row in reader:
    # remove links
    toAdd = re.sub(r'\S+.com\S+|http\S+|\S+http\S+', '', row[6])
    lines.append(toAdd)

with open(file_out, "w") as text_file:
	for tweet in lines[1:]:	
		text_file.write(tweet + '\n')