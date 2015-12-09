    
def actionWarRocketLauncher():

    percepts = getPercepts();
    messages = getMessages()
    for message in messages: 
        if(message.getMessage() == "Au secours!!!"):
            setDebugString("On arrive!")        
            setHeading(message.getAngle())
            
        else:
            setDebugString("No cible")        

    for percept in percepts:
        if(percept.getType().equals(WarAgentType.WarBase)):
            if(isEnemy(percept)):    
                setHeading(percept.getAngle())
                
                # Question a: ==> Enlevez  cette partie  
                
                broadcastMessageToAll("base enemie trouve","")# Question  b
                setDebugString("base enemie trouve")

                for message in messages: 
                    if(message.getMessage() == "attaques la base"):
                        setDebugString("Mode hunter")
                        setHeading(percept.getAngle())# Question b
                        
                #Eenlevez  jusqu'a  là  pour  avoir la question a 
                        if (isReloaded()):
                            return fire()
                        else :
                            return reloadWeapon()
                    else:
                        setDebugString("No cible")       
            else:
                setDebugString("No cible")

        else:
            setDebugString("No cible")           
        
        
    

    if(isBlocked()):
        RandomHeading()


    return move();  