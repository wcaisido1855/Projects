import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'XI8ezizHorsaJLvhR6CpRjBF1'
consumer_secret= 'g9i6PDHqa7VhnBiK58zFuh9ENbVnliob7cqN1JfYAsBG7AyCgS'

access_token='1688826414-eHrrNLNWH52Ct5TSmK2Wnwxaj2gTh8y49opH6wc'
access_token_secret='78xDrsJnZhIdrDYFUW0tYaiNKqvg8aaNmfPk9f8QjC27Y'

auth = tweepy. OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Kanye')

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
