# Simulates a datebase connection 
import pandas as pd 

class Connector(object):
    
    def __init__(self, database_path):
        df = pd.read_csv(database_path) 
        self.df = df

    def get_conversation(self, alliance_id):
        conversation = self.df[self.df['alliance_id'] == alliance_id]
        return conversation
    



if __name__ == "__main__":
    con = Connector("backend\data-store\chat_messages_1.csv\chat_messages_1.csv")
    print(con.get_conversation('11cf0f6b70280de8e21157a87da895c0db0dcc34222386600fb5d4959c88ee51'))
