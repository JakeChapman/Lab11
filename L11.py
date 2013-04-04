# L11.py
#James Holdren
#Jacob Chapman
#Sugyon Won
#Text Games II
#
def getName():
 
    name = requestString("What is the name of your player?")
 
    return name
 
 
 
def getWeapon():
 
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
 
    self.name = name
 
    self.position = pos
 
    self.level = 1
 
    self.inventory = invt
 
    self.weapon = wpn
 
    self.health = health
 
 
 
  #Function to determine whether or not a battle will occur
 
  def battle(self):
 
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
 
      while not(dwarf_health == 'Dead'):
 
        if self.weapon == 'Bow':
 
          dwarf_health  = dwarf.updateHealth(8)
 
        elif self.weapon == 'Axe':
 
          dwarf_health = dwarf.updateHealth(3)
 
        elif self.weapon == 'Sword':
 
          dwarf_health = dwarf.updateHealth(5)
 
        self.health = self.health - 2
 
        if self.health <= 0:
 
          printNow('DEAD!!!')
 
          break         
 
        else:
 
          printNow('Your current health is ' + str(self.health))
 
    elif chance > 75:
 
      while elf_health != 'Dead':
 
        if self.weapon == 'Bow':
 
          elf_health = elf.updateHealth(8)
 
        elif self.weapon == 'Axe':
 
          elf_health = elf.updateHealth(3)
 
        elif self.weapon == 'Sword':
 
          elf_health = elf.updateHealth(5)
 
        self.health = self.health - 2
 
        if self.health <= 0:
 
          printNow('DEAD!!!')
 
          break
 
        else:
 
          printNow('Your current health is ' + str(self.health))
 
  # function for moving
 
  def rePos(self, direction):
 
    """Updates the players location"""
 
    if (direction == 'n'):
 
      self.position[1] += 1
 
    elif (direction == 'e'):
 
      self.position[0] += 1
 
    elif (direction == 'w'):
 
      self.position[0] -= 1
 
    elif (direction == 's'):
 
      self.position[1] -= 1
 
    elif (direction == "up"):
 
      self.level += 1
 
    elif (direction == "down"):
 
      self.level -= 1
 
 
 
class Dwarf:
 
  def __init__(self, health):
 
    self.health = health
 
       
 
  def updateHealth(self,damage):
 
      self.health = self.health - damage
 
      if self.health <= 0:
 
        return 'Dead'
 
      else:
 
        return 'Alive'
 
 
 
class Elf:
 
    def __init__(self,health):
 
      self.health = health
 
   
 
    def updateHealth(self, damage):
 
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
 
    """
 
   
 
    self.items = items
 
    self.description = description
 
 
 

class Forest(Location):
 
 
 
  def __init__(self):
 
    """Makes a dummy location object as a forest"""
 
    description = "You see a forest, nothing more"
 
    Location.__init__(self, [], description)
 
 
 
  def info(self):
 
    printNow(self.description)
 
 
 

class Landmark(Location):
 
  def __init__(self, items, description):
 
    """
 
    Makes a landmark
 
    @param list of items contained here
 
    @param The description
 
    """
 
   
 
    Location.__init__(self, items, description)
 
 
 
  def info(self):
 
    """Displays info for the location"""
 
    printNow(self.description)
 
    if (self.items):
 
      printNow("You see:")
 
      for item in self.items:
 
        printNow(item)
 
    else:
 
      printNow("There are no items here")
 
 
 

class WarpZone(Location):
 
  """Location that allows a player to warp to a different zone"""
 
  def __init__(self):
 
    description = "You see the warp zone, a gateway to another realm"
 
    Location.__init__(self, [], description)
 
 
 

class Game:
  
  def __init__(self):
 
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
    """Generates the map"""
    
    import random
    # Initialize the landmarks
    
    tower = Landmark([], '')
    well = Landmark([], '')
    
    landmarks = [tower, well]
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
   """The game loop of the game"""
   """@param the locations"""
   
   textIn = ""
   
   startPos = [0,0]
   
   player = Player(getName(), startPos, [], getWeapon(), 50)
   
   printNow(textIn)
   while ((textIn != "exit") and (player.health > 0)):
      # get the current location
      currentLoc = locs[player.level][player.position[1]][player.position[0]]
      
      # print the description
      currentLoc.info()
      
      player.battle()
      turnIsDone = false
      
      # generate possible directions
      possibles = self.generatePossibleActions(player.position)
      
      printNow("You may move:")
      
      for action in possibles:
        printNow(action)
      
      textIn = requestString("What will you do?")

  def generatePossibleActions(self, pos):
    """Returns a list of all possible actions based on player location"""
    actions = []
    
    if (pos[0] < 4):
      actions.append("E")
    if (pos[0] > 0):
      actions.append("W")
    if (pos[1] < 4):
      actions.append("N")
    if (pos[1] > 0):
      actions.append("S")
    
    return actions

def runGame():
  """Runs the game"""
  game = Game()
