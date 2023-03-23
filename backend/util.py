# Simulates a datebase connection 
import pandas as pd 

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
        

if __name__ == "__main__":
    paths = ["backend\data-store\chat_messages_1.csv\chat_messages_1.csv", "backend\data-store\chat_messages_2.csv\chat_messages_2.csv"]
    # print(typeof)
    print(con.get_conversation('11cf0f6b70280de8e21157a87da895c0db0dcc34222386600fb5d4959c88ee51'))

