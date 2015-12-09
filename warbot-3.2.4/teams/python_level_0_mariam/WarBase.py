
def actionWarBase():

    percepts = getPercepts();
    messages = getMessages();

    for message in messages:
        if(message.getMessage() == "whereAreYou"):
            setDebugString("I'm here base mees choupi")
            sendMessage(message.getSenderID(), "here", "")
            
        elif(message.getMessage() == "base enemie trouve"):
              setDebugString("attaques la base");
              sendMessage(message.getSenderID(), "attaques la base", "")

        else:
            setDebugString("") 

    for percept in percepts:
        if(percept.getType().equals(WarAgentType.WarRocketLauncher)):
            if(isEnemy(percept) and ( percept.getDistance() == 0)) :
                setDebugString("Au secours!!!")
                broadcastMessageToAgentType(WarAgentType.WarRocketLauncher, "Au secours!!!", "");
    return idle();

    
