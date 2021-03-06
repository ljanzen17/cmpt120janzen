# emotions.py
# Get the mode of interaction from the user
# Params: none

emotions = ["anger","happiness","disgust","fear","sadness","surprise"]
interactions = ["reward","punish","threaten","joke"]

emotion_matrix = [[1,0,0,5],[5,4,3,1],[2,2,3,2],[5,3,3,5],[1,0,3,1],[5,0,3,1]]

expressions = ["I am so angry!",
               "I'm over the moon with happiness!",
               "I am disgusted!",
               "I am so afraid!",
               "I am so sad I might cry",
               "I am so surprised!"]

def intro(emotions,currEmotion):
    print("I am feeling ", currEmotion)
    print("Interact with me and I might change how I'm feeling")

# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction(interactions):
    interaction = interactions.index(input("Please enter an interaction(reward, punish, threaten, or joke): "))
    return(interaction)
                                     
# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion
def lookupEmotion(currEmotion, userAction,emotions,emotion_matrix):
    new_emotion = emotions[emotion_matrix[emotions.index(currEmotion)][userAction]]
    return(new_emotion) # return an integer corresponding to an emotion

def showEmotion(currEmotion,expressions):
    print(expressions[currEmotion])

def main():
    currEmotion = 'anger'
    intro(emotions,currEmotion)
    while 1:
        currEmotion = lookupEmotion(currEmotion,getInteraction(interactions), emotions, emotion_matrix)
        showEmotion(emotions.index(currEmotion),expressions)

main()
    


