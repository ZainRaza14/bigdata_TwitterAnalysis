from textblob import TextBlob


def sent_Analysis(all_Tweets):
    tweets_Pos = 0
    tweets_Neutral  = 0
    tweets_Negative = 0

    for tweet in all_Tweets:
        out_Analysis  = TextBlob(tweet)
        out_Sentiment = out_Analysis.sentiment.polarity

        if out_Sentiment > 0:
            tweets_Pos += 1
        elif out_Sentiment == 0:
            tweets_Neutral += 1
        else:
            tweets_Negative += 1
    tweets_Total = tweets_Pos + tweets_Neutral + tweets_Negative
    percent_Pos = tweets_Pos / tweets_Total * 100
    percent_Neu  = tweets_Neutral  / tweets_Total * 100

    print ("\n Total No. positive tweets = {} Percentage = {}".format(
        tweets_Pos, percent_Pos))
    print ("\n Total No. of neutral tweets  = {} Percentage = {}".format(
        tweets_Neutral, percent_Neu))
    print ("\n Total No. of negative tweets = {} Percentage = {}".format(
        tweets_Negative, 100 - (percent_Pos + percent_Neu)))