def maximalRectangle(matrix):
    if not matrix: 
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Step 1: Build row intervals
    row_intervals = []
    for r in range(rows):
        intervals = []
        c = 0
        while c < cols:
            if matrix[r][c] == "1":
                start = c
                while c < cols and matrix[r][c] == "1":
                    c += 1
                intervals.append((start, c - 1))
            c += 1
        row_intervals.append(intervals)
    
    # Step 2: Build column intervals
    col_intervals = []
    for c in range(cols):
        intervals = []
        r = 0
        while r < rows:
            if matrix[r][c] == "1":
                start = r
                while r < rows and matrix[r][c] == "1":
                    r += 1
                intervals.append((start, r - 1))
            r += 1
        col_intervals.append(intervals)
    
    # Step 3: Compare row and column intervals for overlap
    max_area = 0
    for r_idx in range(rows):
        for start_r, end_r in row_intervals[r_idx]:
            width = end_r - start_r + 1
            # Check vertical extent
            min_height = float('inf')
            for c in range(start_r, end_r + 1):
                # Find column interval that includes this row
                col_height = 0
                for start_c, end_c in col_intervals[c]:
                    if start_c <= r_idx <= end_c:
                        col_height = end_c - r_idx + 1
                        break
                min_height = min(min_height, col_height)
            area = width * min_height
            max_area = max(max_area, area)
    
    return max_area



matrix = [["1","1","1","1","0"],
          ["0","1","1","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","1","0"]]

print(maximalRectangle(matrix))  
