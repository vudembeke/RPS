from getpass import getpass as input
print("Rock, Paper, Scissors")
print()
print("Select your move (R, P, or S)")
print()
player1 = input("Player1 > ")
print()
player2 = input("Player2 > ")
print()
if player1 == "R" and player2 == "R":
  print("It's a tie!You both picked rock")
elif player1 == "R" and player2 == "P":
  print("Player2 wins! Paper covered rock")
elif player1 == "R" and player2 == "S":
  print("Player1 wins!Rock smashed scissors")
elif player1 == "P" and player2 == "R":
  print("Player1 wins!Paper covered rock")
elif player1 == "P" and player2 == "P": 
  print("It's a tie!You both picked paper")
elif player1 == "P" and player2 == "S":
  print("Player2 wins! Scissors cut paper")
elif player1 == "S" and player2 == "R":
  print("Player2 wins!Rock smashed scissors")
elif player1 == "S" and player2 == "P":
  print("Player1 wins! Scissors cut paper")
elif player1 == "S" and player2 == "S":
  print("It's a tie! You both picked scissors")
else:
  print("Invalid move, try again!")