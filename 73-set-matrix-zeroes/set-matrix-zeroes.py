class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Step 1: Check if first row or first column has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Step 2: Mark zeros on first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 3: Use marks to set elements to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Set first row and first column to zero if necessary
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        