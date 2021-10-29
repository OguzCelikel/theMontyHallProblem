import random
import time

# eliminate one door 
def eliminateDoor2(picked, prize):
  allDoors = [1,2,3]
  chosedDoors = []
  chosedDoors.append(picked)
  chosedDoors.append(prize)
  #which is not prize door and picked door
  eliminatedList = list(set(allDoors) - set(chosedDoors))
  # if prize adn user's door is same we have 2 value. But we must choose 1 eliminateDoor
  eliminatedDoor = eliminatedList[0]
  return eliminatedDoor

def play(youPick,prizeDoor):
  time.sleep( 1 )
  if prizeDoor == youPick:
    print("....")
    time.sleep( 1 )
    print("........")
    time.sleep( 1 )
    print("..........")
    time.sleep( 1 )
    print("You WON BMW")
  else:
    print("....")
    time.sleep( 1 )
    print("........")
    time.sleep( 1 )
    print("..........")
    time.sleep( 1 )
    print("Sooory")
  print("You Pick:",youPick,"Prize Door:",prizeDoor)

#Generate a random number between 0 and 2 we have 3 doors (0,1,2)
prizeDoor = random.randint(1,3)
youPick = int(input("Please select a door [1, 2, 3]\n"))
#eliminate
eliminateDoor = eliminateDoor2(prizeDoor, youPick)
print("Eliminated Door",eliminateDoor)
print("Do u want to change your door")
answer = input("[yes] or [no]\n")
if answer == "yes":
  youPick = eliminateDoor2(youPick,eliminateDoor)
  #youPick = 
  play(youPick, prizeDoor)
else:
  play(youPick, prizeDoor)
