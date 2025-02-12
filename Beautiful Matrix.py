def beautiful_matrix(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                row, col = i, j
                break
    center_row, center_col = 2, 2
    moves = abs(center_row - row) + abs(center_col - col)
    return moves
matrix = [list(map(int, input().split())) for _ in range(5)]
print(beautiful_matrix(matrix))
