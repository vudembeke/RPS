from getpass import getpass as input
print("Rock, Paper, Scissors")
print()
print("Select your move (R, P, or S)")
print()
print("Round one")
player1score = 0
player2score = 0
while True:
  player1 = input("Player1 > ")
  print()
  player2 = input("Player2 > ")
  print()
  if player1 == "R" and player2 == "R":
    print("It's a tie!You both picked rock")
    player1score += 1
    player2score += 1
  elif player1 == "R" and player2 == "P":
    print("Player2 wins! Paper covered rock")
    player2score += 1
  elif player1 == "R" and player2 == "S":
    print("Player1 wins!Rock smashed scissors")
    player1score += 1
  elif player1 == "P" and player2 == "R":
    print("Player1 wins!Paper covered rock")
    player1score += 1
  elif player1 == "P" and player2 == "P": 
    print("It's a tie!You both picked paper")
    player1score += 1
    player2score += 1
  elif player1 == "P" and player2 == "S":
    print("Player2 wins! Scissors cut paper")
    player2score += 1
  elif player1 == "S" and player2 == "R":
    print("Player2 wins!Rock smashed scissors")
    player2score += 1
  elif player1 == "S" and player2 == "P":
    print("Player1 wins! Scissors cut paper")
    player1score += 1
  elif player1 == "S" and player2 == "S":
    print("It's a tie! You both picked scissors")
    player1score += 1
    player2score += 1
  else:
    print("Invalid move, try again!")
  if player1score == 3 or player2score == 3:
    print()
    print("Player 1 has",player1score,"wins")
    print("Player 2 has",player2score,"wins")
    print("Thanks for playing!")
    exit()
  else:
    continue
          