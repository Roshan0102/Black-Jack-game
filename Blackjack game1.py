import random
import sys
play = int(input("Do you want to play Blackjack game? If yes enter '1' or if no enter '0':"))
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def score_cal(user):
    user_score = 0  
    for i in user:
        user_score += i 
    return user_score
        
def score_cal_com(computer):
    computer_score = 0  
    for j in computer:
        computer_score += j 
    return computer_score

while(play == 1):
    for i in range(0,2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    user_score = score_cal(user)
    print("User cards:", user,",","User score:",user_score)
    print("Computer first card:", computer[0])
#   print("Computer cards for creating purpose:",computer)
    if user_score > 21:
        if cards[0] in user:
            index_11 = user.index(11)
            user = user[:index_11]+[1]+user[index_11+1:]
            print("After changing 11 to 1 for creating purpose:",user)
            user_score = score_cal(user)
            user_input = int(input("Enter '1' if you want to get another card or Enter '0' to stay with the card:"))
            while(user_input == 1):
                user.append(random.choice(cards))
                user_score = score_cal(user)
                print("User cards:",user,"User score:",user_score)
                user_input = int(input("Enter '1' if you want to get another card or Enter '0' to stay with the card:"))
    
    elif user_score <= 21:
         user_input = int(input("Enter '1' if you want to get another card or Enter '0' to stay with the card:"))
         while(user_input == 1):
             user.append(random.choice(cards))
             user_score = score_cal(user)
             print("User cards:",user,"User score:",user_score)
             if user_score > 21:
                 user_input = 0
             elif user_score <= 21:
                 user_input = int(input("Enter '1' if you want to get another card or Enter '0' to stay with the card:"))
    
    while(user_input == 0):
        if score_cal_com(computer) < 17:
            computer.append(random.choice(cards))
            computer_score = score_cal_com(computer)
            print("Computer cards:",computer,"Computer score:",computer_score)
        elif score_cal_com(computer) >= 17:
            computer_score = score_cal_com(computer)
            break
        
    if computer_score == user_score:
        print("Match Draw")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif computer_score > 21 and user_score > 21:
        print("Match Draw")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif user_score < computer_score and computer_score > 21:
        print("User won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif user_score < computer_score and computer_score <=21:
        print("Computer Won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif user_score > computer_score and computer_score <= 21 and user_score <= 21:
        print("User Won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif computer_score > user_score and computer_score <= 21 and user_score <= 21:
        print("Computer Won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif user_score > computer_score and computer_score <= 21 and user_score > 21:
        print("Computer Won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")
    elif computer_score > user_score and computer_score > 21 and user_score <= 21:
        print("User Won")
        play = int(input("Do you want to play again Blackjack game? If yes enter '1' or if no enter '0':"))
        if play == 1:
            user.clear()
            computer.clear()
        else:
            print("OK bye")

