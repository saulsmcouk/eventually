def quantify_reaction(context):
    """
    Given a convo, return a value for the strength of the reaction of all other users in each emotion
    
    Strength of reaction = the difference between their baseline level and their average level in the time or number winodw
    """
    total_pos = 0
    total_neg = 0
    for message in context:
        total_pos += message["sentiment-pos"]
        total_neg += message["sentiment-neg"]
    
    return total_pos/(total_pos + total_neg)
        
