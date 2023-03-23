import pandas as pd
import util

from transformers import pipeline

# Functionality you need - solving confusing conveersations
# Step 1: identify them


class ReactionManager(object):

    def __init__(self, con):
        self.con = con 
        self.classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)

    def get_user_baseline_values(self, user_id):
        """
        Given a con and a user_id, get baseline values for their emotional reactions

        The plan - look at all of the emotional reactions of each user on messages ranked at different levels of offense 
        95e3f1bdb3f517e697280bb555eea85d9e197e31a59d59e4b1dba147cec4bf07
        """
        emotions = {
            "sadness": [],
            "joy": [],
            "love": [],
            "anger": [],
            "fear": [],
            "surprise": []
        }
        all_user_messages = self.con.get_all_user_messages(user_id)
        for id, row in all_user_messages.iterrows():
            prediction = self.classifier(row["raw_message"])
            for emotion in prediction[0]:
                emotions[emotion['label']].append(emotion['score'])

        for key in emotions:
            emotions[key] = sum(emotions[key]) / len(emotions[key])

        return emotions

    def quantify_reaction(self, convo, message_id, time_window=False, nr_window=False):
        """
        Given a convo, return a value for the strength of the reaction of all other users in each emotion
        
        Strength of reaction = the difference between their baseline level and their average level in the time or number winodw
        """
        users = {}
        for id, message in convo.iterrows():
            if message['account_id'] not in users:
                users[message['account_id']] = [message]
            else:
                users[message['account_id']].append(message)
        
        # what are these users' baselines?
        baselines = {}
        for user in users.keys():
            baselines[user] = self.get_user_baseline_values(user)
        
        print(baselines)



if __name__ == "__main__":
    print("Fake database connection")
    con = util.Connector(["backend\data-store\chat_messages_1.csv\chat_messages_1.csv", "backend\data-store\chat_messages_2.csv\chat_messages_2.csv"])
    print("connected")
    # this convo features unhappy reactions
    # reaction = print(quantify_reaction(convo, "", con))
    # util.print_transcript(convo)
    # print(get_user_baseline_values(con, '95e3f1bdb3f517e697280bb555eea85d9e197e31a59d59e4b1dba147cec4bf07'))
    rm = ReactionManager(con)
    print("reaction manager initiated")

    convo = con.get_conversation('c58f81d1b0f6fd904eda0508a20e1967511383e26f6e579ce5f6b3fb391fe1e6')
    rm.quantify_reaction(convo, "")