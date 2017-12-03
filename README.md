# Hinglish-Sentiment-Analysis
In this project we work on the sentiment analysis of Hinglish tweets, which are the tweets written entirely in Latin script but containing slang words from English and Hindi, commonly used in India.

## Sections 
+ [Overview](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#overview)
+ [Methodology](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#methodology)
+ [Installation](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#installation)
+ [How to run](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#how-to-run)
+ [Authors](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#authors)
+ [Contributing](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis#contributing)

## Overview 

Given a Hinglish text, for sentiment analysis generally the techniques applicable for the English text are used. Hence we might lose out on the important sentiments that might be conveyed by the part written in Hindi. Thus it is highly important to take into account the sentiment of both the languages. 

for eg. "That restraurant is not good. Itna ghatiya khaana to kabhi nahi khaya"

which means "That restraurant is not good. I haven't had such a bad food ever in my life"

The problem with these texts is that the Hindi written is in an informal manner, also it is not in the script in which the language is originally written. Hence different people might have different versions of spellings and the rule with which they write such texts. In the subsequent sections we have given a brief explanation on how these challenges were handeled. 

## Methodology 

+ **Pre-processing** One of the most initial steps where tasks like removing hashtags, mentions and links in the tweet were completed. We also applied spelling normalisation and found out the stem words using the stemmer package. 

+ **Clustering** In this task we clustered out the Hindi and the English portions of the tweet. One of the main properties of such texts is that the English and the Hindi parts generally exist in groups. Hence we first try to isolate them. We use the corpus generated from a dictionary. For eg if we have to classify the word 'reccommend', which has been wrongly spelt, and the actual spellings are 'recommend'. So we first of all consider this word and compute it's [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) with words in our corpus starting from 'r' and having a length in range (l-2,l+2) where l is the length of the word we are considering. For the example we have considered the levenshtein distance will be less. But for a word in Hindi like 'ghatiya' ,which means 'bad' or 'cheap' depending upon context, will have a large value of the levenshtein distance with any word beginning with g in the dictionary. Hence we alot a distance to every word and then finally apply the k-means algorithm to get two clusters of Hindi and English. In certain cases like the Hindi word 'main' means 'me'. But this is also an English word, however classifying this word as Hindi won't have any effect on our results since the words like these do not have any overall effect on the sentiment of the tweet. Most of the Hindi words which can effect the overall sentiment have a high levenshtein distance with a word of similar length in the English corpus. 

+ **Processing** Using the googletrans library which has been [licensed by MIT](https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis/blob/master/LICENSE) we translate the Hindi written in Latin script into Hindi written in Devanagari script. Then we use the ESWN and the HSWN to interact with our text and assigne senti scores to all the words. For emojis we have used the python regular expression for assigning score to the emojis. 

+ **Feature set** We then construct a feature set consisting of 7 features for every tweet: 

  + Whether it has a positive score or not
  + Whether it has a negative score or not 
  + Word count greater than 8 
  + Contains adjectives 
  + Contains emojis 
  + Contains hashtag 
  + Contains mentions 
  
 + **Classification** We use SVM classifier. 
 
 ## Installation 
 
 The libraries required are : numpy, pandas, xlrd, XlsxWriter, scikit-learn, regex, pyparsing, nltk, googletrans, sklearn
 
 These libraries can be installed by using the pip installer 

If you have pip installed on your system then use `pip install library_name` to install the required library. 
If you do not have pip then please look [here](https://pip.pypa.io/en/stable/installing/) on how to install pip

## How to Run 

In command line run as `python main.py <InputFileName.xlsx>` where InputFileName.xlsx consists of the tweets you want to classify. 

This will ouput the file Output.csv which consists of the scores of the tweets 

+ 1 for positive
+ -1 for negative 
+ 0 for neutral 

## Authors: 
* [Vipul Khatana](https://github.com/vipul-khatana)

Undergraduate Thesis under [**Dr. Brejesh Lall**](http://ee.iitd.ernet.in/people/brijeshlall.html)

## Contributing

1) Fork it (https://github.com/vipul-khatana/Hinglish-Sentiment-Analysis/fork)
2) Create your feature branch `git checkout -b feature/fooBar`
3) Commit your changes `git commit -am 'Add some fooBar'`
4) Push to the branch `git push origin feature/fooBar`
5) Create a new pull request 

