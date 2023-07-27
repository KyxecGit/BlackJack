import random
from art import logo

def deal_card(): # Раздача карт
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards): # Подсчет карт
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21: # Если попался туз и сумма с ним превышает 21 установить его значение на 1
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "Перебор. Ты проиграл 😤"
  
  if user_score == computer_score:
    return "Ничья 🙃"
  elif computer_score == 0:
    return "Проигрыш, у компьютера 21 😱"
  elif user_score == 0:
    return "Победа с 21 😎"
  elif user_score > 21:
    return "Перебор. Ты проиграл 😭"
  elif computer_score > 21:
    return "У компьютера перебор. Ты победил 😁"
  elif user_score > computer_score:
    return "Ты победил 😃"
  else:
    return "Ты проиграл 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Твои карты: {user_cards}, текущий счет: {user_score}")
    print(f"   Первая карта компьютера: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Набери 'да' чтобы взять еще одну карту, набери 'нет' чтобы пропустить: ")
      if user_should_deal == "да":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Твоя рука: {user_cards}, финальный счет: {user_score}")
  print(f"   Рука компьютера: {computer_cards}, финальный счет: {computer_score}")
  print(compare(user_score, computer_score))

while input("Сыграем в 21? Набери 'да' или 'нет': ") == "да":
  play_game()