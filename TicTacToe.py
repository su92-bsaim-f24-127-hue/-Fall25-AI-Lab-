instructions = ''' 
This will be over tic tac toe board 

    1| 2  | 3
  ---|----|---
    4| 5  | 6
  ---|----|---
    7| 8  | 9 
     
1. Put the number (1-9) to put your sign.
3. Player_1 will go first. '''
part = []
for i in range(9):
      part.append(' ')

def print_board():
     board= f'''
          {part[0]}  | {part[1]}  | {part[2]}
        -----|----|------
          {part[3]}  | {part[4]}  | {part[5]}
        -----|----|------
          {part[6]}  | {part[7]}  | {part[8]}
'''
     print(board)
index_list = []
def take_input(player_name):
     while True:
          try:
              x = int(input(f"{player_name}:"))
              x-=1
              if 0 <= x < 10:
                 if x in index_list:
                     print("this spott is blocked")
                     continue
                 index_list.append(x)
                 return x
              else:
                   print("PLease enter number between 1-9")
          except ValueError:
               print("Invalid input ! . Numbers only.")

    

def result(player_1,player_2):
    if  part[0] == part[1] == part[2] == 'X' or part[1] == part[4] == part[7] == 'X' or part[0] == part[4] == part[8] == 'X' or part[2] == part[5] == part[8] == 'X' or part[3] == part[4] == part[5] == 'X' or part[2] == part[4] == part[6] == 'X' or part[6] == part[7] == part[8] == 'X' or part[0] == part[3] == part[6] == 'X' :
            print(f'Congratulations {player_1}.!!! You WON.')
            return True
    elif part[0] == part[1] == part[2] == 'O' or part[1] == part[4] == part[7] == 'O' or part[0] == part[4] == part[8] == 'O' or part[2] == part[5] == part[8] == 'O' or part[3] == part[4] == part[5] == 'O' or part[2] == part[4] == part[6] == 'O' or part[6] == part[7] == part[8] == 'O' or part[0] == part[3] == part[6] == 'O' :
             print(f'Congratulations {player_2}.!!! You WON.')
             return True
    return False




def main():
    print("Welcome to the tic tac game. ")
    player_1 = input("Enter the palyer_1 name :")
    player_2 = input("Enter the player_2 name:")
    print(f"THank you for joining {player_1} and {player_2  }")

    print(instructions)
    print(f" {player_1}'s sign is - X")
    print(f"{player_2}'s sign is - O")
    print("Enter any key to start the game:")
    print_board()

    for j in range(9):
        if j % 2 == 0:
             i = take_input(player_1)
             part[i] = 'X'
        else:
             i = take_input(player_2)
             part[i] = 'O'
        print_board()
        if result(player_1,player_2):
             return 

    print("This is a tie. Play Again")
             
 

main()