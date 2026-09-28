import random


def print_board(board):
    print("")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("")


def check_win(board, player):
    
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input.")


def ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    move = random.choice(available_moves)
    board[move[0]][move[1]] = "O"


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board(board)
    
    while True:
        
        player_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("You win!")
            break
        if check_draw(board):
            print("draw!")
            break

        
        print("AI move")
        ai_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("AI wins.")
            break
        if check_draw(board):
            print("draw!")
            break

if __name__ == "__main__":
    main()