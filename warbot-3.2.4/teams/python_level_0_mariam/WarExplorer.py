
def actionWarExplorer():

   messages = getMessages();
   percepts = getPercepts();

   for percept in percepts:
                     
       if(percept.getType().equals(WarAgentType.WarFood)):
           if((percept.getDistance() < getMaxDistanceTakeFood()) and (not isBagFull())):
               broadcastMessageToAll("foooddd!!!!!", "")
               setHeading(percept.getAngle())
               take()
              
               for message in messages:
                   if(message.getMessage() == "foooddd!!!!!"):
                       setDebugString("foodddd!!!à gogo")
                       setHeading(message.getAngle())
                       return take()
           elif (not isBagFull()) :
               setHeading(percept.getAngle())
       
       
       #if(percept.getType().equals(WarAgentType.WarExplorer)):
        #   messages = getMessages();
         #  for message in messages:
          #     if(message.getMessage() == "foooddd!!!!!"):
           #        setDebugString("foodddd!!!à gogo");
                   #setHeading(message.getAngle());
                   #return take();
                   #return move();
       #if(percept.getType().equals(getPerceptsEnemiesByType(WarAgentType.WarBase))):   
       else:    
           
           perceptA = getPerceptsEnemiesByType(WarAgentType.WarBase);
           if((perceptA is None) or (len(perceptA) == 0)):
              return move();
           else:   
              setDebugString("mes bb");
              broadcastMessageToAgentType(WarAgentType.WarBase, "whereAreYou", ""); 
                
          
                      
   if (isBlocked()) :
       RandomHeading()
        
   return move()
    
 
    
