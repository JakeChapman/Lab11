# L11.py
#James Holdren
#Jacob Chapman
#Sugyon Won
#Text Games II
#
def getName():
    """Jake Chapman"""
    name = requestString("What is the name of your player?")
 
    return name
 
 
 
def getWeapon():
    """Jake Chapman"""
    weapon = requestString("What is your weapon of choice?(Sword, Axe, Bow)")
 
    if weapon == 'Sword' or weapon == 'sword':
      return 'Sword'
 
    elif weapon == 'Axe' or weapon == 'axe':
      return 'Axe'
 
    elif weapon == 'Bow' or weapon == 'bow':
      return 'Bow'
 
    else:
      showInformation("Please reenter a weapon with the correct spelling")
      getWeapon()
 
     
 
class Player:
 
  """Constructor for the generic player class"""
 
  def __init__(self,name,pos,invt, wpn, health):
    """Jake Chapman"""
    self.name = name
 
    self.position = pos
 
    self.level = 1
 
    self.inventory = invt
 
    self.weapon = wpn
 
    self.health = health
 
  def addItem(self, key):
    """
    Adds an item to the player's inventory
    @param string the name of the item
    @return void
    James Holdren
    """
    self.inventory.append(key)
  
  def getHealth(self):
    """
    Retrieves the player's health
    @return int the player's health
    James Holdren
    """
    
    return self.health
 
  #Function to determine whether or not a battle will occur
 
  def battle(self):
    """Jake Chapman"""
    import random
 
    #Variable that holds value that determines if a battle will occur
 
    chance =  100 * random.random()
 
    #creates the enemies from two different classes
 
    dwarf = Dwarf(10)
 
    elf = Elf(10)
    
    elf_health = elf.updateHealth(0)
    
    dwarf_health = dwarf.updateHealth(0)
 
    #if loops that contain a while loop that does the battle
 
    if chance > 50 and chance < 75:
      
      showInformation("A dwarf has appeared and is attacking!")
      
      while not(dwarf_health == 'Dead'):
 
        if self.weapon == 'Bow':
          
          printNow("You fire an arrow at him")
          
          dwarf_health  = dwarf.updateHealth(8)
          
          showInformation("The dwarf's health is " + str(dwarf.health))
 
        elif self.weapon == 'Axe':
 
          
          printNow("You strike the elf with your axe")
          
          dwarf_health = dwarf.updateHealth(3)
          
          showInformation("The dwarf's health is " + str(dwarf.health))
 
        elif self.weapon == 'Sword':
 
          
          printNow("You slash at the creature")
          
          dwarf_health = dwarf.updateHealth(5)
          
          showInformation("The dwarf's health is " + str(dwarf.health))
          
 
        self.health = self.health - 2
 
        if self.health <= 0:
 
          showInformation('DEAD!!!')
 
          break         
 
        else:
 
          showInformation('Your current health is ' + str(self.health))
 
    elif chance > 75:
      
      showInformation("An elf has appeared and is attacking!")
      
      while elf_health != 'Dead':
       
        if self.weapon == 'Bow':
          
          printNow("You fire an arrow at him")
          
          elf_health = elf.updateHealth(8)
          
          showInformation("The elf's health is  " + str(elf.health))
 
        elif self.weapon == 'Axe':
          
          printNow("You strike the elf with your axe")
          
          elf_health = elf.updateHealth(3)
          
          showInformation("The elf's health is " + str(elf.health))
 
        elif self.weapon == 'Sword':
 
          
          printNow("You slash at the creature")
          
          elf_health = elf.updateHealth(5)
          
          showInformation("The elf's health is " + str(elf.health))
 
        self.health = self.health - 2
 
        if self.health <= 0:
 
          showInformation('DEAD!!!')
 
          break
 
        else:
 
          showInformation('Your current health is ' + str(self.health))
 
  # function for moving
 
  def rePos(self, direction):
    """Updates the players location"""
    """James Holdren"""
 
    if (direction == 'n'):
      self.position[1] += 1
    elif (direction == 'e'):
      self.position[0] += 1
    elif (direction == 'w'):
      self.position[0] -= 1
    elif (direction == 's'):
      self.position[1] -= 1
    elif (direction == 'warp'):
      self.level = not self.level
  
  def checkEnding(self):
    """
    Checks if the user has won
    @return boolean
    Sug Yon
    """
    
    if (len(self.inventory) == 4):
      return true
    return false
 
 
class Dwarf:
 
  def __init__(self, health):
    """Jake Chapman"""
    self.health = health
 
       
 
  def updateHealth(self,damage):
      """Jake Chapman"""
      self.health = self.health - damage
 
      if self.health <= 0:
 
        return 'Dead'
 
      else:
 
        return 'Alive'
 
 
 
class Elf:
    def __init__(self,health):
      """Jake Chapman"""
      self.health = health
 
   
 
    def updateHealth(self, damage):
      """Jake Chapman"""
      self.health = self.health - damage
 
      if self.health <= 0:
 
        return 'Dead'
 
      else:
 
        return 'Alive'
 
 
 

# The location class
 
 
 

class Location:
 
 
 
  def __init__(self, items, description):
    """
    Constructor for Location base class
    @param list of items contained here
    @param the description
    James Holdren
    """
 
   
 
    self.items = items
    self.description = description
  
  def getName(self):
    """
    @return the name of the current object
    James Holdren
    """
    return self.__class__.__name__
  
  def checkForItem(self, item):
    """
    Checks to see if the location has the item
    @param the item name
    @return true if it does else false
    James Holdren
    """
    
    if (item in self.items):
      return true
    else:
      return false
  
  def removeItem(self, item):
    """
    Removes the item from the location
    @param string the item
    @return void
    James Holdren
    """
    self.items.remove(item)
 
 

class Forest(Location):
 
 
 
  def __init__(self):
    """Makes a dummy location object as a forest"""
    """James Holdren"""
    description = "You see a forest, nothing more"
    Location.__init__(self, [], description)
  
  def info(self):
    """Prints the forest description"""
    """James Holdren"""
    printNow(self.description)
 
 
 

class Landmark(Location):
 
  def __init__(self, items, description):
    """
    Makes a landmark
    @param list of items contained here
    @param The description
    James Holdren
    """
    
    Location.__init__(self, items, description)
 
 
 
  def info(self):
    """Displays info for the location"""
    """James Holdren"""
    printNow(self.description)
    
    # for displaying items
    if (self.items):
      printNow("You see:")
      for item in self.items:
        printNow(item)
      # tell the user how to pick them up
      printNow("Enter the name of an item to pick it up")
    else:
      printNow("There are no items here")
 
 
 

class WarpZone(Location):
  """Location that allows a player to warp to a different zone"""
 
  def __init__(self):
    """James Holdren"""
    description = "You see the warp zone, a gateway to another realm"
    Location.__init__(self, [], description)
  
  def info(self):
    """
    Prints the warp zone description
    James Holdren
    """
    printNow(self.description)

class Game:
  
  def __init__(self):
    """
    James Holdren
    Sug Yon
    """
    import random
    
    # The locations
    self.locs = [0,0]
    self.locs[0] = [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                    ]
 
    self.locs[1] = [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                    ]
 
    # now fill in the map
    self.generateMap()
    # now begin the game
    self.gameLoop(self.locs)
 
 
  def generateMap(self):   
    """
    Generates the map
    James Holdren
    Sug Yon
    """
    
    import random
    # Initialize the landmarks
    
    # put down two warp zones
    for i in range(2):
      # get the location
      x = random.randint(0,4)
      y = random.randint(0,4)
      z = i
      
      # place a warp zone
      self.locs[z][y][x] = WarpZone()
      
    
    tower = Landmark(['staff'], 'You see a crumbling tower.')
    well = Landmark(['gold piece'], 'You see an old well.')
    grave = Landmark(['medallion'], 'Before you is a creepy grave.')
    stone = Landmark(['piece of eight'], 'You see a large stone, towering '
    + 'the trees')
    
    landmarks = [tower, well, grave, stone]
    # Now attempt to place the landmarks
 
    for landmark in landmarks:
      # Keep track if we have placed it or not
      placed = false
      
      while(not placed):
        # get the location
        x = random.randint(0,4)
        y = random.randint(0,4)
        z = random.randint(0,1)
        
        # get the location we're looking at
        loc = self.locs[z][y][x]

        #check if something's there or not
        if (loc == 0):
          self.locs[z][y][x] = landmark
          placed = true
 
    # now fill in everything else in the map with forests
    for z in range(2):
      for y in range(5):
        for x in range(5):
          if (self.locs[z][y][x] == 0):
            # we've found an empty spot
            # place a forest
            self.locs[z][y][x] = Forest()
    
  def gameLoop(self, locs):
    """
    The game loop of the game
    @param the locations
    @return void
    James Holdren
    Sug Yon
    Jake Chapman
    """
    
    clearScreen()
    
    # put up the prologue
    prologue()
    textIn = raw_input("Press enter to continue")
    
    clearScreen()
    
    textIn = ""
   
    startPos = [0,0]
    
    player = Player(getName(), startPos, [], getWeapon(), 100)
    
    # keep track if the player has won or not
    hasWon = false
    
    while ((textIn != "exit") and (player.getHealth() > 0) and (not hasWon)):
      # get the current location
      currentLoc = locs[player.level][player.position[1]][player.position[0]]
      # get the location's name
      locName = currentLoc.getName()
      
      
      #keep track if the user is done with the turn
      turnIsDone = false
      
      # check if the player is in a battle and then carry out the battle
      player.battle()
        
      
      # generate all movements for the player
      possibles = self.generatePossibleActions(player.position, locName)
      
      # print the description
      currentLoc.info()
      
      # begin the player's turn
      while ((textIn != 'exit') and (not turnIsDone) and (not hasWon)):
        # tell the user the possible movements
        self.outputPossibleMovements(possibles)
        
        textIn = requestString("What will you do?").lower()
        
        # check the user input
        # check if it's a valid direction
        if (textIn in possibles):
          player.rePos(textIn)
          turnIsDone = true
          clearScreen()
        # check if they entered a valid item name
        elif (currentLoc.checkForItem(textIn)):
          player.addItem(textIn)
          currentLoc.removeItem(textIn)
          
          printNow("You picked up: " + textIn)
        elif (textIn == 'exit'):
          pass
        elif (textIn == 'help'):
          help()
        elif (textIn == 'info'):
          currentLoc.info()
        else:
          printNow("Invalid Input")
        
        # check to see if the player has won the game
        hasWon = player.checkEnding()
    
    # player has either exited, won, or died. Check to see which
    if (player.getHealth() <= 0):
      # the player has died
      printNow("You are overcome by the creatures of the forest. GAME OVER")
    elif (player.checkEnding()):
      # the player has collected all items
      printNow("Congradulations! You have collected all items!")
    else:
      # the player has entered exit. Quit without messages
      pass

  def generatePossibleActions(self, pos, type):
    """
    Determins all possible actions based on where the player is.
    @param the array of the player position
    @param string of the class name of the player's current tile
    @return a list of strings that are the possible actions
    """
    
    actions = []
    
    if (pos[0] < 4):
      actions.append("e")
    if (pos[0] > 0):
      actions.append("w")
    if (pos[1] < 4):
      actions.append("n")
    if (pos[1] > 0):
      actions.append("s")
    # check if we're in a warp zone
    if (type == 'WarpZone'):
      actions.append('warp')
    
    return actions
  
  def outputPossibleMovements(self, movements):
    """
    Prints to the screen a formatted list of movements
    @param the list of possible movements
    """
    
    # store the prompt so we can use one line
    prompt = "You may move: "
    for movement in movements:
      prompt += movement + " "
    
    printNow(prompt)

def clearScreen():
  """
  Clears the console
  @return void
  James Holdren
  """
  
  printNow("\n"*15)

def help():
  """
  Displays the help for the screen
  Sug Yon
  James Holdren
  """
  printNow("Help ---------")
  printNow("There are four landmarks in the forest, each with an item for "
  + "collection. Retreive them all and you win.")
  printNow("Monsters -----")
  printNow("As you move between locations in the forest, you may be attacked "
  + "by monsters.")
  printNow("Movement -----")
  printNow("You will be prompted for a direction at each location; however, "
  + "you may not be able to move in some direction based on your position.")
  printNow("Items --------")
  printNow("If you are at a location that contains an item, you may pick "
  + "it up by entering it's name.")
  printNow("Info ---------")
  printNow("Entering in 'info' at any time will display info about your "
  + "current location.")

def prologue():
  """
  Prints the prologue to the screen
  James Holdren
  """
  printNow("You are lost in a forest, and the only ways out are to either "
  + "collect each item at randomly placed landmarks around the forest or "
  + "succumb to death by creatures calling the forest home.")

def runGame():
  """
  Runs the game
  Jake Chapman
  """
  game = Game()
