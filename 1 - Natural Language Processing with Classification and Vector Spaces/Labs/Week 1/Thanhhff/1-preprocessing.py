import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

### About the Twitter Dataset
# nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

### In thong tin cua bo du lieu
# print('Number of positive tweets: ', len(all_positive_tweets))
# print('Number of negative tweets: ', len(all_negative_tweets))
# print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
# print('The type of a tweet entry is: ', type(all_negative_tweets[0]))
#
# # print positive in greeen
# print('\033[92m' + all_positive_tweets[random.randint(0, 5000)])
# # print negative in red
# print('\033[91m' + all_negative_tweets[random.randint(0, 5000)])

### Preprocessing 1 du lieu
tweet = all_positive_tweets[2277]
print(tweet)

# My beautiful sunflowers on a sunny Friday morning off :) #sunflowers #favourites #happy #Friday off… https://t.co/3tfYom0N1i

### Remove Stopword
# nltk.download('stopwords') # Download Stopword

import re
import string

from nltk.corpus import stopwords  # Modul de remove stopwords
from nltk.stem import PorterStemmer  # Modul de stem
from nltk.tokenize import TweetTokenizer  # Modul Tokenizer

### Su dung `re` de remove

# remove old style retweet text "RT"
tweet2 = re.sub(r'^RT[\s]+', '', tweet)

# remove hyperlinks
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet2)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)

print(tweet2)

### Tokenize the String 
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
tweet_tokens = tokenizer.tokenize(tweet2)

print(tweet_tokens)

### Remove Stopword

stopwords_english = stopwords.words('english')

tweets_clean = []
for word in tweet_tokens:  # Go through every word in your tokens list
    if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
        tweets_clean.append(word)

print('removed stop words and punctuation:')
print(tweets_clean)


### Stemming
stemmer = PorterStemmer()

tweets_stem = []

for word in tweets_clean:
    stem_word = stemmer.stem(word)
    tweets_stem.append(stem_word)

print('stemmed words:')
print(tweets_stem)

### Using ultis.py

from utils import process_tweet # Import the process_tweet function, cần connect vào G-Drive để import utlis

# choose the same tweet
tweet = all_positive_tweets[2277]

print()
print('\033[92m')
print(tweet)
print('\033[94m')

# call the imported function
tweets_stem = process_tweet(tweet); # Preprocess a given tweet

print('preprocessed tweet:')
print(tweets_stem) # Print the result