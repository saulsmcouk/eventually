# Simulates a datebase connection, does some other util stuff 
import csv
import json
import pandas as pd 
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tqdm import tqdm
import torch


class Connector(object):
    def __init__(self, database_paths):
        self.df = pd.DataFrame()
        for path in database_paths:
            print(path)
            df = pd.read_csv(path) 
            self.df = pd.concat([self.df, df])

        self.df = self.df.dropna(how='all')

        self.users_df = pd.read_csv("backend\data-store\\accounts.csv\\accounts.csv")

        print(len(self.df))

    def get_message_context(self, user_id, alliance_id, time, window_before = 10, window_after = 10):
        the_conversation = self.get_conversation(alliance_id)
        # idk why I need to do this 
        the_conversation = the_conversation.to_dict('records')
        for i in range(0, len(the_conversation)):
            if (the_conversation[i]["account_id"] == user_id) and (the_conversation[i]["timestamp"] == time):
                before = max(0, i - window_before)
                after = min(len(the_conversation) - 1, i + window_after)
                return the_conversation[before:after]

    def get_conversation(self, alliance_id):
        conversation = self.df[self.df['alliance_id'] == alliance_id]
        return conversation

    def get_all_user_messages(self, user_id):
        all_messages = self.df[self.df['account_id'] == user_id]    
        return all_messages

    def get_individual_message(self, user_id, alliance_id, time):
        message = self.df[(self.df["account_id"] == user_id) & (self.df["alliance_id"] == alliance_id) & (self.df["timestamp"] == time)].iloc[0]
        return message.to_dict()

    def get_user_information(self, user_id):
        return self.users_df[self.users_df["account_id"] == user_id].iloc[0].to_dict()

def print_transcript(convo):
    [print(f'{row["account_id"]}: {row["raw_message"]}') for id, row in convo.iterrows()]
    

def add_sentiment_to_csv(path, outpath):
    print("loading")
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    print("loaded")
    header = data[0]
    header.append("sentiment-neg")
    header.append("sentiment-pos")

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    print("model loaded")
    with open(outpath, "w", encoding="utf-8") as of:
        writer = csv.writer(of)
        writer.writerow(header)

    prog = 0

    for row in tqdm(data[1:]):
        inputs = tokenizer(row[4], return_tensors="pt", truncation=True)
        with torch.no_grad():
            logits = model(**inputs).logits.numpy()
        # 0 is neg, 1 is pos
        row.append(logits[0][0])
        row.append(logits[0][1])
        
        with open(outpath, "a", encoding="utf-8") as of:
            writer = csv.writer(of)
            writer.writerow(row)


def generate_user_baseline_sentiments(messages):
    user_sentiment_vals = {
        "neg": [],
        "neu": [],
        "pos": [],
        "compound": []
    }
    user_messages = messages

    for id, row in user_messages.iterrows():
        this_sent = row["sentiment"].replace("'", '"')
        this_sent = json.loads(this_sent)
        for key in this_sent.keys():
            user_sentiment_vals[key].append(this_sent[key])

    for key in user_sentiment_vals.keys():
        user_sentiment_vals[key] = sum(user_sentiment_vals[key]) / len(user_sentiment_vals)

    return user_sentiment_vals


def get_reaction_strength(reacting_messages, con: Connector):
    """for each user, get their baseline, and then look at their messages"""
    reacting_messages = pd.DataFrame().from_records(reacting_messages)
    users = set(reacting_messages['account_id'])
    user_baselines = {
        user: generate_user_baseline_sentiments(con.get_all_user_messages(user)) for user in users
    }
    diffs = []
    for user in user_baselines.keys():
        this_user_messages = reacting_messages[reacting_messages["account_id"] == user]
        user_reaction_sentiments = {
            "compound": [],
            "neg": [],
            "neu": [],
            "pos": []
        }
        user_reaction_diffs = dict(user_reaction_sentiments)
        for id, message in this_user_messages.iterrows():
            # insecure, oh don't know what for, turning heads when you walk through the injection vulnerability
            this_message_sentiment = ast.literal_eval(message.sentiment)
            for key in this_message_sentiment.keys():
                user_reaction_sentiments[key].append(this_message_sentiment[key])
        
        for key in user_reaction_sentiments:
            user_reaction_sentiments[key] = sum(user_reaction_sentiments[key]) / len(user_reaction_sentiments[key])
        
        # diff against baseline
        for key in user_baselines[user].keys():
            user_reaction_diffs[key] =  abs(user_reaction_sentiments[key] - user_baselines[user][key])
        diffs.append(user_reaction_diffs)

    aggregate_diffs = {
            "compound": [],
            "neg": [],
            "neu": [],
            "pos": []
        }    
    for diff in diffs:
        for key in diff.keys():
            aggregate_diffs[key].append(diff[key])
    
    for key in aggregate_diffs.keys():
        aggregate_diffs[key] = sum(aggregate_diffs[key]) / len(aggregate_diffs)

    return aggregate_diffs


moderation_q = [
    ['e668bc85eb3ed7f3ee45d55bf7ecd4aee7ff957753fc9b119da9a72fbb755661', '11cf0f6b70280de8e21157a87da895c0db0dcc34222386600fb5d4959c88ee51', '20230301T031530.717Z'],
    ['01d5d5afed4a055a6532ecc94fc3eebf78ca8117cadbf13acf7c4fa992901427', '4a8900ef0888491a6cfc2143bf8b6919281b30388c7ebacd65a980623c8b1704', '20230301T090721.129Z']
]


