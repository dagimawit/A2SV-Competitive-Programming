class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        self.mat = mat
        m = len(self.mat)
        
        left_diagonal_idx = []
        right_diagonal_idx = [] 
        
        # Get left and right diagonal elements
        left_diagonal = [self.mat[i][i] for i in range(m)]
        right_diagonal = [self.mat[i][(m-i)-1] for i in range(m)]
        
        # Get indices for left and right diagonals
        for i in range(m):
            left_diagonal_idx.append(f"self.mat[{i}][{i}]")
            right_diagonal_idx.append(f"self.mat[{i}][{m-i-1}]")
        set_idx = set(left_diagonal_idx + right_diagonal_idx) # get unique indices
        
        # Map index and values
        zip_left = list(zip(left_diagonal_idx, left_diagonal))
        zip_right = list(zip(right_diagonal_idx, right_diagonal))
        
        # Get unique elements in right_diagonal
        unique_right = [i for i in zip_right if i not in zip_left]

        zip_unique = zip_left.copy() # copy zip_left
        for i in unique_right:
            zip_unique.append(i) 
        
        # Compute total
        total = 0
        for _,val in zip_unique:
            total += val
        return total