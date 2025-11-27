import easygui

class Board:
    def __init__(self):
        self.data = [' '] * 9

    def display(self):
        data = self.data
        print(f'| {data[0]} | {data[1]} | {data[2]} |')
        print('-------------')
        print(f'| {data[3]} | {data[4]} | {data[5]} |')
        print('-------------')
        print(f'| {data[6]} | {data[7]} | {data[8]} |')

    def set_cell(self, x, y, marker):
        index = x + y * 3
        if 0 <= index < 9 and self.data[index] == ' ':
            self.data[index] = marker
            return True
        return False
    
   
    def check_win(self):
        d = self.data
        
        
        winning_lines = [
            
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
           
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            
            (0, 4, 8), (2, 4, 6)
        ]

        for line in winning_lines:
            if d[line[0]] == d[line[1]] == d[line[2]] and d[line[0]] != ' ':
                return d[line[0]]  # Return 'X' or 'O' (the winner)
        
        if ' ' not in d:
            return 'Tie'
            
        return None  

def ask_for_move(board, marker):
    while True:
        try:
            spot_num = input(f"Player {marker}, choose your spot (1-9): ")
            index = int(spot_num) - 1
            
            if 0 <= index <= 8:
                x = index % 3
                y = index // 3
                
                if board.set_cell(x, y, marker):
                    break
                else:
                    print("That spot is already taken or invalid. Try again.")
            else:
                print("Please enter a number between 1 and 9.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")


board = Board()
current_player = 'X'
winner = None

print("Welcome to Tic-Tac-Toe!")

print("\n--- Spot Mapping ---")
print("| 1 | 2 | 3 |")
print("-------------")
print("| 4 | 5 | 6 |")
print("-------------")
print("| 7 | 8 | 9 |")
print("--------------------")

while winner is None: 
    print(f"\n--- Player {current_player}'s Turn ---")
    board.display()
    
    ask_for_move(board, current_player)
    
    winner = board.check_win()
    
    if winner is None:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

print("\n--- Final Board ---")
board.display()

if winner == 'Tie':
    print("\nIt's a Tie!")
    easygui.msgbox("U guys are boring :( its a draw",'GAME RESULT')
    
else:
    print(f"\n Player {winner} Wins the Game!")
    easygui.msgbox(f"PLAYER {winner} WINS THE GAME!",'GAME RESULT')
