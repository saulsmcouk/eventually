import gensim
import nltk
import util as util

print("loading model")
model = gensim.models.KeyedVectors.load('pretrained_model.bin')
print("loaded model")


def rank_messages(message, context, number = 5):
    
    print("MESSAGE")
    print(message.iloc[0].to_dict()["raw_message"])
    print("\n\n")
    message = message.iloc[0].to_dict()
    print("CHAT LOG IN ORDER")
    print("\n")
    [print(message["raw_message"]) for message in context]
    print(f"\n-------\n{message['raw_message']}\n")
    target_tokens = nltk.word_tokenize(message["raw_message"].lower())
    similarity_scores = []
    for message in context:
        tokenised_message = nltk.word_tokenize(message["raw_message"].lower())
        similarity_score = model.n_similarity(target_tokens, tokenised_message)
        similarity_scores.append(similarity_score)
    try: 
        sorted_messages = [sent for _, sent in sorted(zip(similarity_scores, context), reverse=True)]
        relevant_messages = []
        irrel = []
        for i, message in enumerate(sorted_messages):
            i += 1
            if i < number:
                relevant_messages.append(message)
            else: 
                irrel.append(message)
        print("rel")
        [print(m["raw_message"]) for m in relevant_messages]
        print("irrel")
        irrel.reverse()
        [print(m["raw_message"]) for m in irrel]
        return relevant_messages
    except TypeError:
        return []
                
        
moderation_q = [
    ['e668bc85eb3ed7f3ee45d55bf7ecd4aee7ff957753fc9b119da9a72fbb755661' , '11cf0f6b70280de8e21157a87da895c0db0dcc34222386600fb5d4959c88ee51', '20230301T031530.717Z'],
    ['01d5d5afed4a055a6532ecc94fc3eebf78ca8117cadbf13acf7c4fa992901427', '4a8900ef0888491a6cfc2143bf8b6919281b30388c7ebacd65a980623c8b1704', '20230301T090721.129Z'],
    ['a7af5959631cb2a2276cab33053b2d1f9bcf4ffcf64b7446d95ccc5703ba6761', 'ebb591cdd218bd6e00ff632f2acd350d1f6f9c46f15cbd69a59f6b54523b6d16', '20230301T154033.755Z'],
    ['471746b381dcd10cb3ff781b0a343e5ffeb38d5fe29fee009e41673293aed918', '38f06fe05b0d3585c82ce43331dc47c4b927fb9493249d1f879e9b2e5b0f5011', '20230301T185525.550Z'],
    ['1ee1b428c5bdead4f4b809e0ef5dae44d1a60ee38fd8e56d73d86aeda8d1e2ce', 'bcfccf86ec22ef621a537bc693ffc64445480f499b9c9192a0da9ba45ae45935', '20230301T032618.905Z'],
    ['bacd01be997e5988a0b6f914f162c72cd5671663c21c0e141bcaa4c0c6efb68b', '75c8e78a2dbc5239db5dcbd6b986f6b20223f8b2b1b2a347b03548d7d51853da', '20230301T013427.816Z']
]

test_index = 5 # 5 is a good example

con = util.Connector([
    'backend\data-store\messages-1-with-sentiment.csv',
    'backend\data-store\messages-2-with-sentiment.csv'
])

# messages = con.get_message_context(
#     moderation_q[test_index][0],
#     moderation_q[test_index][1],
#     moderation_q[test_index][2],
#     window_before=10,
#     window_after=10
# )

# rank_messages(
#     con.get_message(
#         moderation_q[test_index][0],
#         moderation_q[test_index][1],
#         moderation_q[test_index][2]
#         ),
#         messages
#     )
