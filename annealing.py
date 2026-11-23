import random
import math


def display_board(board):
   """Print the N-Queens board."""
   n = len(board)
   for r in range(n):
       print(" ".join("Q" if board[r] == c else "." for c in range(n)))
   print()


def compute_attacks(board):
   """Returns the number of conflicting queen pairs."""
   n = len(board)
   conflicts = 0
   for i in range(n):
       for j in range(i + 1, n):
           same_column = board[i] == board[j]
           same_diag = abs(board[i] - board[j]) == abs(i - j)
           if same_column or same_diag:
               conflicts += 1
   return conflicts


def random_move(board):
   """Moves one queen to a new random column in its row."""
   n = len(board)
   new_board = board.copy()
   row = random.randrange(n)
   new_col = random.randrange(n)
   new_board[row] = new_col
   return new_board


def simulated_annealing(n, start_temp=120, cooling_factor=0.92,
               stop_temp=0.5):
   # Create a random start board
   current = [random.randrange(n) for _ in range(n)]
   curr_cost = compute_attacks(current)
   temperature = start_temp
   step = 1
   print("Initial Board:")
   display_board(current)
   print(f"Initial Cost = {curr_cost}\n")
   while temperature > stop_temp and curr_cost > 0:
       nxt = random_move(current)
       nxt_cost = compute_attacks(nxt)
       delta = nxt_cost - curr_cost
       # Move to neighbor if better OR based on probability
       if delta < 0 or random.random() < math.exp(-delta / temperature):
           current = nxt
           curr_cost = nxt_cost
           print(f"Step {step:3d} | Temp={temperature:6.2f} | Cost={curr_cost}")
       step += 1
       # Cool the system
       temperature *= cooling_factor
   # Final output
   print("\nFinal Board Configuration:")
   display_board(current)
   print(f"Final Cost = {curr_cost}")
   if curr_cost == 0:
       print("Solution Found! (Goal State)")
   else:
       print("Stopped before reaching a perfect solution.")


simulated_annealing(8)