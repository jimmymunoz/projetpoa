
def actionWarBase():

	setDebugString("BaseOk");
	messages = getMessages();

	if( False ):
		for message in messages:
			if(message.getMessage() == "whereAreYou"):
				setDebugString("OurBaseIsHere");
				sendMessage(message.getSenderID(), "OurBaseIsHere", "");
			elif( message.getMessage() == "EnemyBase" ) :
				debugStr = "RocketLaunchersAttack: (" + str(message.getAngle()) + ") Angle ";
				setDebugString(debugStr);
				broadcastMessageToAgentType(WarAgentType.WarRocketLauncher, "RocketLaunchersAttack", str(message.getAngle()) );#str to cast string
	
	#Jimmy: All Enemies	
	if( True ):
		percepts = getPerceptsEnemies();
		for percept in percepts:
			broadcastMessageToAgentType(WarAgentType.WarRocketLauncher, "ThereAreEnemiesInOurBase", "");#str to cast string
			setDebugString("ThereAreEnemiesInOurBase distance:" + str(percept.getDistance()) );
		
	else: #Only Rocket Launchers
		percepts = getPercepts();
		for percept in percepts:
			if (percept.getType().equals(WarAgentType.WarRocketLauncher) and isEnemy(percept) and percept.getDistance() <= 50 ):
				broadcastMessageToAgentType(WarAgentType.WarRocketLauncher, "ThereAreEnemiesInOurBase", "");#str to cast string
				setDebugString("ThereAreEnemiesInOurBase distance:" + str(percept.getDistance()) );
	
	return idle();


