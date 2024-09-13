def saddle_points(matrix):
    # Check for an empty matrix
    if not matrix:
        return []

    # Check for irregular matrix
    if len(set(len(row) for row in matrix)) != 1:
        raise ValueError("irregular matrix")

    rows = len(matrix)
    cols = len(matrix[0])

    # Find largest values in each row
    row_maxes = [max(row) for row in matrix]

    # Find smallest values in each column
    col_mins = [min(matrix[i][j] for i in range(rows)) for j in range(cols)]

    # Find saddle points
    result = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == row_maxes[i] and matrix[i][j] == col_mins[j]:
                result.append({"row": i + 1, "column": j + 1})

    return result


# Test the function
print(saddle_points([]))  # Should return an empty list []
