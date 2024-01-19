def score_after_flipping_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Step 1: Flip rows to ensure the leftmost element in each row is 1
    for row in range(rows):
        if matrix[row][0] == 0:
            for col in range(cols):
                matrix[row][col] = 1 - matrix[row][col]

    # Step 2: Flip columns to maximize the number of 1s in each column
    for col in range(1, cols):
        count_ones = sum(matrix[row][col] for row in range(rows))
        if count_ones < (rows + 1) // 2:
            for row in range(rows):
                matrix[row][col] = 1 - matrix[row][col]

    # Calculate the total score
    total_score = sum(int("".join(map(str, row)), 2) for row in matrix)
    return total_score

print(score_after_flipping_matrix([[1,1],[1,0]]))