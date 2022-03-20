from google.colab import output #output.clear() clear the screen
import random #random function

# returns a random card
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]
  return random.choice(cards)

# return score 0 for blackjack and if cards over 21 converts 11 to 1 and return score
def calculated_score(cards):
  if sum(cards)==21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#compare user and computer score
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Darw 😑"
  elif computer_score == 0:
    return "You loose, opponent has blackjack 😭"
  elif user_score == 0:
    return "You win 😁"
  elif user_score > 21:
    return "You went over, You loose 😩"
  elif computer_score > 21:
    return "Opponent went over, You win 😉"
  elif user_score > computer_score:
    return "You win 😎"
  else:
    return "You loose ☹️"

def playgame():
  
  
  logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

  print(logo)
  

  user = []
  computer = []
  isgame_over = False

  # deals first two cards
  for _ in range(0,2):
    user.append(deal_card())
    computer.append(deal_card())

  while not isgame_over:
    user_score = calculated_score(user)
    computer_score = calculated_score(computer)

    print(f'Your cards {user}, current score: {user_score}')
    print(f"Computer's first card: {computer[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      isgame_over = True
    else:
      user_should_deal = input("type y to get another card, n to pass")
      if user_should_deal == 'y':
        user.append(deal_card())
      else:
        isgame_over = True

  while computer_score !=0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculated_score(computer)

  print(f'Your final hand: {user}, final score: {user_score}')
  print(f"Oponent's final hand {computer}, final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to paly blackjack?y/n") == "y":
  output.clear()
  playgame()
