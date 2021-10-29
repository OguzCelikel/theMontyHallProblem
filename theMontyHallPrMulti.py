import random

countWin1 = 0
countWin2 = 0
countWin3 = 0
playedTimes = 10000

# eliminate one door 
def eliminateDoor(picked, prize):
  allDoors = [1,2,3]
  chosedDoors = []
  chosedDoors.append(picked)
  chosedDoors.append(prize)
  #which is not prize door and picked door
  eliminatedList = list(set(allDoors) - set(chosedDoors))
  # if prize adn user's door is same we have 2 value. But we must choose 1 eliminateDoor
  eliminatedDoor = eliminatedList[0]
  return eliminatedDoor
# if user win the game win will increase
def play(youPick,prizeDoor):
  if prizeDoor == youPick:
    return True
  else:
    return False

for i in range(playedTimes):
  #Generate a random number between 0 and 2 we have 3 doors (0,1,2)
  prizeDoor = random.randint(1,3)
  playerOne = random.randint(1,3)
  playerTwo = random.randint(1,3)

  #playerThree radomly changes
  playerThree = random.randint(1,3)
  eliminateDoorThree = eliminateDoor(prizeDoor, playerThree)
  randomSwitch = random.randint(0,1)
  if randomSwitch == 1:
    #player three will SWITCH
    playerThree = eliminateDoor(playerThree,eliminateDoorThree)
 
  eliminateDoorOne = eliminateDoor(prizeDoor, playerOne)
  eliminateDoorTwo = eliminateDoor(prizeDoor, playerTwo)
  playerTwo = eliminateDoor(playerTwo,eliminateDoorTwo)
  #control if the user win
  control1 = play(playerOne, prizeDoor)
  if control1 == True:
    countWin1 += 1
  control2 = play(playerTwo, prizeDoor)
  if control2 == True:
    countWin2 += 1
  control3 = play(playerThree, prizeDoor)
  if control3 == True:
    countWin3 += 1
  
print("Don't Switch Ratio :", countWin1/playedTimes, "of", playedTimes,"games")
print("Switch Ratio :", countWin2/playedTimes, "of", playedTimes,"games")
print("Random Switch Ratio :", countWin3/playedTimes, "of", playedTimes,"games")

"""
Don't Switch Ratio : 0.3366 of 10000 games
Switch Ratio : 0.662 of 10000 games
Random Switch Ratio : 0.5012 of 10000 games
"""
