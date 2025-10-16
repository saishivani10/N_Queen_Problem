

"""
Unique N-Queens solver using backtracking.
Author: Sai_shivani10
"""

def print_board(board):
	for row in board:
		print(' '.join('Q' if x else '.' for x in row))
	print()

def can_place(bd, r, c, n):
	
	for i in range(r):
		if bd[i][c]:
			return False
	
	i, j = r-1, c-1
	while i >= 0 and j >= 0:
		if bd[i][j]:
			return False
		i -= 1
		j -= 1
	
	i, j = r-1, c+1
	while i >= 0 and j < n:
		if bd[i][j]:
			return False
		i -= 1
		j += 1
	return True

def nqueens(n):
	results = []
	board = [[0]*n for _ in range(n)]

	def place(row):
		if row == n:
			
			results.append([r[:] for r in board])
			return
		for col in range(n):
			if can_place(board, row, col, n):
				board[row][col] = 1
				place(row+1)
				board[row][col] = 0

	place(0)
	return results

if __name__ == "__main__":
	N = 8
	sols = nqueens(N)
	print(f"Total solutions for {N}-Queens: {len(sols)}\n")
	for idx, sol in enumerate(sols, 1):
		print(f"Solution {idx}:")
		print_board(sol)
