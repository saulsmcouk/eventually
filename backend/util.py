# Simulates a datebase connection, does some other util stuff 
import csv
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Connector(object):
    
    def __init__(self, database_paths):
        self.df = pd.DataFrame()
        for path in database_paths:
            print(path)
            df = pd.read_csv(path) 
            self.df = pd.concat([self.df, df])
        
        

    def get_conversation(self, alliance_id):
        conversation = self.df[self.df['alliance_id'] == alliance_id]
        return conversation

    def get_all_user_messages(self, user_id):
        all_messages = self.df[self.df['account_id'] == user_id]    
        return all_messages

def print_transcript(convo):
    [print(f'{row["account_id"]}: {row["raw_message"]}') for id, row in convo.iterrows()]
        
# import pandas as pd
from multiprocessing import Pool
# from nltk.sentiment import SentimentIntensityAnalyzer

def add_sentiment_to_csv(path, outpath):
    print("loading")
    data = pd.read_csv(path)

    print("loaded")
    header = list(data.columns)
    header.append("sentiment")

    # create the SentimentIntensityAnalyzer object once
    sid = SentimentIntensityAnalyzer()

    # define a function to calculate the sentiment for a single row
    def calculate_sentiment(row):
        scores = sid.polarity_scores(row[4])
        row.append(scores)
        return row

    # use a multiprocessing pool to calculate the sentiment for each row
    with Pool() as pool:
        results = pool.map(calculate_sentiment, data.itertuples(index=False))

    # write the results to a new CSV file
    with open(outpath, "w", encoding="utf-8") as of:
        writer = csv.writer(of)
        writer.writerow(header)
        writer.writerows(results)
if __name__ == "__main__":
    # paths = ["backend\data-store\chat_messages_1.csv\chat_messages_1.csv", "backend\data-store\chat_messages_2.csv\chat_messages_2.csv"]
    # print(typeof)
    # print(con.get_conversation('11cf0f6b70280de8e21157a87da895c0db0dcc34222386600fb5d4959c88ee51'))
    add_sentiment_to_csv('backend\data-store\chat_messages_1.csv\chat_messages_1.csv', 'backend\data-store\messages-1-with-sentiment.csv')


