import re
from collections import defaultdict

def clean_lexicon(lex_input):
    lex_file_l=open(lex_input, "r").readlines()

    new_lex_file_l=[]
    for i in lex_file_l:
        i=i.strip()
        i= re.sub("_", " ", i)
        new_lex_file_l.append(i)
    return new_lex_file_l

my_positive_list= clean_lexicon("/Users/AnkitaShetty/Documents/sem2/SMM/pos.wn")
my_negative_list= clean_lexicon("/Users/AnkitaShetty/Documents/sem2/SMM/neg.wn")
postweetfile=open("/Users/AnkitaShetty/Documents/sem2/SMM/posTweets.txt", "r").readlines()
negtweetfile=open("/Users/AnkitaShetty/Documents/sem2/SMM/negTweets.txt", "r").readlines()

d=defaultdict(int)

#count number of positive or negative words in any line
def count(l, genre):
    count = 0
    if genre == 'positive':
        w = l.split()
        for w in w:
            if w in my_positive_list:
                count = count + 1
    if genre == 'negative':
        w = l.split()
        for w in w:
            if w in my_negative_list:
                count = count + 1
    print 'Number of ', genre, ' is ', count

#check if sentence is positive or negative
def check(l):
    w = l.split()
    pos_count = 0
    neg_count = 0
    for w in w:
        if w in my_positive_list:
            pos_count = pos_count + 1
        if w in my_negative_list:
            neg_count = neg_count + 1
    if pos_count > neg_count:
        print 'Positive sentence'
    else:
        print 'Negative sentence'

pos_count = 0
neg_count = 0

def updatecount(w, count):
    if w in my_positive_list:
        count = count+1
    if w in my_negative_list:
        count = count-1
    return count

def printlist(positive_tweet, negative_tweet, mixed_tweet):
    print 'positive_tweet', positive_tweet
    print 'negative_tweet', negative_tweet
    print 'mixed_tweet', mixed_tweet

def classify_file_lines(filename):
    positive_tweet=[]
    negative_tweet=[]
    mixed_tweet=[]
    #filename = filename[:20]
    for l in filename:
        count = 0
        if ':)' in l:
            count = count + 1
        if ':(' in l:
            count = count - 1
        w = l.split()
        for w in w:
            count = updatecount(w, count)
        if count>0:
            positive_tweet.append(l)
        if count<0:
            negative_tweet.append(l)
        if count == 0:
            mixed_tweet.append(l)

    printlist(positive_tweet, negative_tweet, mixed_tweet)


while True:
    print ''
    print 'Choose a an option 1,2,3,4: '
    print '1. count number of positive or negative words in any line'
    print '2. check if sentence is positive or negative'
    print '3. run the classifier'
    print '4. exit'

    value = 0

    value = raw_input("Enter value: ")

    if value == str(1):
        sentence = raw_input("Enter a sentence: ")
        genre = raw_input("Choose positive or negative: ")
        count(sentence, genre)

    if value == str(2):
        sentence = raw_input("Enter a sentence: ")
        check(sentence)

    if value == str(3):
        filename = raw_input("Choose a file name: postweetfile or negtweetfile")
        classify_file_lines(filename)

    if value == str(4):
        break

i = postweetfile.split()
for i in i:
    count=0
    print i
    for j in my_positive_list:
        if "great" in i:
            print j
            count+=1
    print count
    for j in my_negative_list:
        if i.find(j) != -1:
            count-=1
    print count
    if count>0:
        print "Positive Tweet"
    elif count<0:
        print "Negative Tweet"
    else:
        print "*Neutral Tweet*"