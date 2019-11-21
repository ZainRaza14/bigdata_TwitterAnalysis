import json
import csv
from nltk.corpus   import stopwords
from nltk.tokenize import TweetTokenizer
from collections   import Counter
from prettytable   import PrettyTable
from nltk.stem.wordnet import WordNetLemmatizer
import re, sys, csv, nltk, string


def convert_JsontoCSV(name):
    json_Data = open(name, mode='r').read()
    py_Data = json.loads(json_Data)
    csv_out = open('tweets.csv', mode='w') 
    writer = csv.writer(csv_out)
    fields = ['screen_name','followers', 'rt', 'text'] 
    writer.writerow(fields)
    for line in py_Data:
        if line:
            writer.writerow([line.get('screen_name'),
                             line.get('followers_count'),
                             line.get('retweet_count'),
                             line.get('text').encode('unicode_escape')]) 
            
    csv_out.close()
    
def text_Cleaning(tmp_Text):
    sw = stopwords.words('english')
    lemma = WordNetLemmatizer()
    tmp_Text   = re.sub(r'\$\w*', '', tmp_Text)
    tmp_Text   = re.sub(r'http?:.*$', '', tmp_Text)
    tmp_Text   = re.sub(r'https?:.*$', '', tmp_Text)
    tmp_Text   = re.sub(r'pic?.*\/\w*', '', tmp_Text)
    tmp_Text   = re.sub(r'[' + string.punctuation + ']+', ' ', tmp_Text)  
    
    tmp_Tokens = TweetTokenizer(strip_handles=True, reduce_len=True).tokenize(tmp_Text)
    tmp_Tokens = [w.lower() for w in tmp_Tokens if w not in sw and len(w) > 2 and w.isalpha()]
    tmp_Tokens = [lemma.lemmatize(word) for word in tmp_Tokens]
    
    return tmp_Tokens

def get_TopWords(in_Words, top = 5):
    tmp_PT = PrettyTable(field_names=['Words', 'Count'])
    c = Counter(in_Words)
    [tmp_PT.add_row(kv) for kv in c.most_common()[:top]]
    tmp_PT.align['Words'], tmp_PT.align['Count'] = 'l', 'r'
    return tmp_PT


def getCleaned_Tweets(text):
    return " ".join(text_Cleaning(text))


def cleanWords(texts):
    temp_Words = []
    for text in texts:
        temp_Words += text_Cleaning(text)
    return temp_Words


