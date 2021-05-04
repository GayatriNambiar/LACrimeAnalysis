import pandas as pd
import csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

df = \
    pd.read_csv('testtweets.csv')

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', -1)

# print("==================Head========================")
# print(df.head())
# #
# print("==================Tail========================")
# print(df.tail())
#
# print("==================Columns========================")
# print(df.columns)
#
# print("==================Shape========================")
# print(df.shape)
#
# print("==================Info========================")
# print(df.info())

# rows = str(len(df))

emoji = []
emoji_sentiment = []
NB_p_pos = []
NB_n_neg = []
NB_sentiment = []
PA_sentiment = []
PA_polarity = []
PA_subjectivity = []

happylist = [":)", ":D", ":*", ";)"]
sadlist = [":(", ":'("]
neutrallist = [":|"]
count=0
for index, row in df.iterrows():
    text = row['Tweet Text']
    emo = ""
    emo_sent = ""

    for x in happylist:
        if x in text:
            emo = emo + " , " + x
            emo_sent = emo_sent + " positive,"

    for x in sadlist:
        if x in text:
            emo = emo + " , " + x
            emo_sent = emo_sent + " negative,"

    for x in neutrallist:
        if x in text:
            emo = emo + " , " + x
            emo_sent = emo_sent + " neutral,"

    emo = emo.lstrip(" ,")
    emo_sent = emo_sent.rstrip(",")
    emoji.append(emo)
    emoji_sentiment.append(emo_sent)

    # Naive Bayes Analyzer

    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    a = (blob.sentiment)
    if a.__getattribute__("p_pos") > a.__getattribute__("p_neg"):
        NB_sentiment.append("positive")

    elif a.__getattribute__("p_pos") < a.__getattribute__("p_neg"):
        NB_sentiment.append("negative")
    else:
        NB_sentiment.append("neutral")

    NB_p_pos.append(str(a.__getattribute__("p_pos")))

    NB_n_neg.append(str(a.__getattribute__("p_neg")))

    # Pattern Analyzer

    blob2 = TextBlob(text)
    PA_polarity.append(blob2.sentiment.polarity)

    PA_subjectivity.append(blob2.sentiment.subjectivity)

    if (blob2.sentiment.polarity > 0):
        PA_sentiment.append("positive")
    elif (blob2.sentiment.polarity == 0):
        PA_sentiment.append("neutral")
    elif (blob2.sentiment.polarity < 0):
        PA_sentiment.append("negative")

    count = count + 1

    print(count)

df1 = pd.DataFrame()
df1 = pd.DataFrame(emoji, columns=['Emoji'])
df2 = pd.DataFrame()
df2 = pd.DataFrame(emoji_sentiment, columns=['Emoji Sentiment'])
df3 = pd.DataFrame()
df3 = pd.DataFrame(NB_p_pos, columns=['NB p_pos'])
df4 = pd.DataFrame()
df4 = pd.DataFrame(NB_n_neg, columns=['NB n_neg'])
df5 = pd.DataFrame()
df5 = pd.DataFrame(NB_sentiment, columns=['NB sentiment'])
df6 = pd.DataFrame()
df6 = pd.DataFrame(PA_sentiment, columns=['PA sentiment'])
df7 = pd.DataFrame()
df7 = pd.DataFrame(PA_polarity, columns=['PA polarity'])
df8 = pd.DataFrame()
df8 = pd.DataFrame(PA_subjectivity, columns=['PA subjectivity'])

df9 = pd.DataFrame()
df9 = pd.concat([df, df1, df2, df3, df4, df5, df6, df7, df8], axis=1)

df9.to_csv(r'testtweets_sentiments.csv', header='True', index='False', encoding='utf-8')
