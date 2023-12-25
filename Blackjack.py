"""
Write a program that plays the game Blackjack or 21 with a user. Give the user the option to “hit” or “stay”.
"""

import random

#Player
def playerVal(playerCard):
  playerValue = 0
  for i in range(len(playerCard)):
    if playerCard[i] == "Ace":
      if playerValue + 11 > 21: #Ace is 1
        playerValue += 1
      else: #Ace is 11
        playerValue += 11
        break
    if playerCard[i] == "Jack" or playerCard[i] == "Queen" or playerCard[i] == "King":
      playerValue += 10
    elif playerCard[i].isdigit() == True:
      playerValue += int(playerCard[i])
    elif playerCard[i].isdigit() == True:
      playerValue += int(playerCard[i])
  return playerValue

#Dealer
def dealerVal(dealerCard):
  dealerValue = 0
  for j in range(len(dealerCard)):
    if dealerCard[j] == "Ace":
      if dealerValue + 11 > 21: #Ace is 1
        dealerValue += 1
      else: #Ace is 11
        dealerValue += 11
        break
    if dealerCard[j] == "Jack" or dealerCard[j] == "Queen" or dealerCard[j] == "King":
      dealerValue += 10
    elif dealerCard[j].isdigit() == True:
      dealerValue += int(dealerCard[j])
    elif dealerCard[j].isdigit() == True:
      dealerValue += int(dealerCard[j])
  return dealerValue

playerValue = 0
dealerValue = 0
gameOver = False
cards = ["Ace", "Ace", "Ace", "Ace", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King"]

playerCard = [cards.pop(cards.index(random.choice(cards))), cards.pop(cards.index(random.choice(cards)))]
dealerCard = [cards.pop(cards.index(random.choice(cards))), cards.pop(cards.index(random.choice(cards)))] #2nd card hidden,revealed when win

while gameOver != True:
  print("Your cards are %s." %playerCard)
  print("The value of your cards is %s." %playerVal(playerCard))
  print()
  print("One of the dealer's card are %s." %dealerCard[0])
  
  print()
  print()
  
  while gameOver == False:
    while True:
      play = input("Would you like to hit or stand: ")
      print()
    
      if play == "hit":
        playerCard.append(cards.pop(cards.index(random.choice(cards))))
        if playerVal(playerCard) < 21:
          print("Your cards are %s." %playerCard)
          print("The value of your cards is %s." %playerVal(playerCard))
          print()
          print("The dealer's cards are %s." %dealerCard)
          print("The value of the dealer's cards is %i." %dealerVal(dealerCard))

          while dealerVal(dealerCard) < 17:
            dealerCard.append(cards.pop(cards.index(random.choice(cards))))
        else:
          while dealerVal(dealerCard) < 17:
            dealerCard.append(cards.pop(cards.index(random.choice(cards))))
          gameOver = True
          break
      if play == "stand":
        gameOver = True
        break
      else:
        print("Please enter a valid response.")
        print()
        
if play == "stand" or gameOver == True:
  gameOver = True
  print("Your cards are %s." %playerCard)
  print("The value of your cards is %s." %playerVal(playerCard))
  print()
  print("The dealer's cards are %s." %dealerCard)
  print("The value of the dealer's cards is %i." %dealerVal(dealerCard))
  if playerVal(playerCard) == 21 or dealerVal(dealerCard) > 21: 
    winner = "you have"
  elif dealerVal(dealerCard) == 21 or playerVal(playerCard) > 21:
    winner = "the dealer has"
  elif dealerVal(dealerCard) < 21 and playerVal(playerCard) < 21: #who's closer
    playerDiff = 21 - playerVal(playerCard)
    dealerDiff = 21 - dealerVal(dealerCard)
    if playerDiff > dealerDiff:
      winner = "the dealer has"
    else:
      winner = "you have"
  else: #Tie
    gameOver = "Tie"
    print("It was a tie.")
  if gameOver == True:
    print("Game Over, %s won." %winner)
