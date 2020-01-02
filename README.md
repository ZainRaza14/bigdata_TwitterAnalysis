# bigdata_TwitterAnalysis


Analyzing Twitter Data


We got streaming data from Twitter and random tweets from https://archive.org/. 

We performed the following analysis using the data:

1.	Word Count: We created a word bubble showing the most frequent words related to the hashtag. 

2. Clustering: We applied a clustering model to the queried tweets and cluster them into “k” number of clusters. Once the clusters were formed, we analyzed them to find out the similarity between the tweeters to compare their behavior. 

3. Sentiment Analysis: We used benchmark sentiment analysis models in NLP to classify tweets into categories such as “positive” and “negative” to understand the general feelings toward a given trend. 

4. We took around 11,252,553 number of tweets and performed analysis on that using EMR. Compared training time and accuracies of algorithms such as Naïve Bayes, Logistic Regression and SVM. We analyzed that accuracies increased by increasing the number of samples from 1-Million to 4-Million to 8-Million and then almost 12-Million on both Local and EMR.

Technologies:
-	Twitter API
-	Kafka for managing twitter data
-	Spark
-	EC2 Instance on AWS
-	EMR – 3 instances 
