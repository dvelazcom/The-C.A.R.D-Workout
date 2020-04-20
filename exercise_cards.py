from random import randint, shuffle
from itertools import product

def createDeck():
    """
    This creates a single list containing tuples which have the values
    (suit, numerical value)
    """
    deck = []
    suits = ['Heart', 'Diamond', 'Spade', 'Club']
    numbers = [i for i in range(1, 14)]
    for c in product(suits,numbers):
        deck.append(c)
    shuffle(deck)
    return deck

def selectCard ():
    num = (randint(0,len(deck)-1))
    return(deck.pop(num))

def find_exercise(card,count):
    #dictionary of each suit and the four excercises for each suit
  card_ex = { 'Spade':['1. Push Ups or incline pushups',
  '2. Pike push ups or vertical pushups', 
  '3. Standing milk jug dumbbell press (serious) [or standing dumbbell press if you have dumbbells]',
  '4. Milk jug lateral raises or doorway lateral raises [or dumbbell/band laterals] a. For the doorway laterals, the “reps” will be the length of the hold in seconds. For example, if you draw a 6, that will be a 16 second doorway lateral hold.'], 
  'Club':['1. Doorway pull ups or tree branch pull ups [or banded pulldowns]',
    '2. Table/Desk inverted row [or dumbbell row]',
    '3. Rear delt flyes with milk jugs [or dumbbell rear delt flyes]',
    '4. Backpack upright row or milk jug upright row [or dumbbell/band upright row]'],
  'Heart':['1. Walking lunges (+backpack for weight) [or dumbbell walking lunges]',
    '2. Bulgarian split squat',
    '3. Single leg hip thrust',
    '4. Nordic ham curl'],
  'Diamond':['1. Biceps: milk jug curl or weightless flex curls (squeeze your biceps as hard as possible with no weight)[or dumbbell curl]',
  '2. Triceps: Bodyweight skullcrushers against a tabletop or close grip pushups [or dumbbell floor skullcrushers','3. Abs: Bicycle crunch or reverse crunch',
  '4. Calves: Standing calf raise (use backpack, milk jug or dumbbell to load)']}
  card_rest = {
      1:'Rest for 2 mins'
  }
  #if the card is an Ace then rest for 2 minutes and not increase suit count
  if card[1] == 1:
      return(card_rest.get(1)),count 

  #first elif is for a suit that is not an 'A' and the list of exercises hasn't reach the end
  elif (card[0] == 'Spade') and (count <= 2):
      count += 1
      return (card_ex.get('Spade', "Invalid card")[count]),count
  #second elif is for a suit that is not an 'A' and the list of exercises has reach the end and list is restarted
  elif (card[0] == 'Spade') and (count == 3):
      count = 0
      return (card_ex.get('Spade', "Invalid card")[count]),count
  elif (card[0] == 'Club') and (count <= 2):
      count += 1
      return (card_ex.get('Club', "Invalid card")[count]),count
  elif (card[0] == 'Club') and (count == 3):
      count = 0
      return (card_ex.get('Club', "Invalid card")[count]),count
  elif (card[0] == 'Heart') and (count <= 2):
      count += 1
      return (card_ex.get('Heart', "Invalid card")[count]),count
  elif (card[0] == 'Heart') and (count == 3):
      count = 0
      return (card_ex.get('Heart', "Invalid card")[count]),count
  elif (card[0] == 'Diamond') and (count <= 2):
      count += 1
      return (card_ex.get('Diamond', "Invalid card")[count]),count
  elif (card[0] == 'Diamond') and (count == 3):
      count = 0
      return (card_ex.get('Diamond', "Invalid card")[count]),count

#number of reps is calualted as the number on the card + 10
def find_reps(num):
    if num in range(2,11):
        return num + 10
    #Jack, Queen, & King cards are all 10 initially and so the return for those 3 will always be 20
    elif num in range (11,14):
        return 20
    #for 'A' we don't return a rep count because it is a rest period
    else:
        return ' '

print("Type S and press enter to start, Q to quit:")
start = input().lower()
next_card = True
deck = createDeck()
#keep track of the # of each suits that have been drawn
spade_count = -1
heart_count = -1
diamond_count = -1
club_count = -1
while (start == 's') and (next_card == True) and (len(deck) > 0):
    card = selectCard()
    if card[0] == 'Spade':
      exercise,spade_count = find_exercise(card,spade_count)
    elif card[0] == 'Club':
      exercise,club_count = find_exercise(card,club_count)
    elif card[0] == 'Diamond':
      exercise,diamond_count = find_exercise(card,diamond_count)
    elif card[0] == 'Heart':
      exercise,heart_count = find_exercise(card,heart_count)
    rep = find_reps(card[1])
    if rep != ' ':
        print('Reps:{}\n{}'.format(rep,exercise))
    else:
        print(exercise)
    print('Press enter to draw another card, press Q and enter to quit')
    next_card = input().lower() != 'q'
    if len(deck) == 0:
      print("Refreshing deck")
      deck = createDeck()
    
exit(0)