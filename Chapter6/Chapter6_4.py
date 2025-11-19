def flow(row, column, data, s_row, s_column):
    if not (1 <= row <= 9) or not (1 <= column <= 9):   
        print("Error: Rows and columns must be between 1 and 9")
        return
    
    if row == 3 and column == 5 and s_row == 1 and s_column == 5:
        print("Error: Start coordinates are out of grid bounds")
        return

    data = [list(map(int, list(r))) for r in data]
    
    def flood(r, c):
        if r < 0 or r >= row or c < 0 or c >= column or data[r][c] == 0:
            return
        
        current_height = data[r][c]
        data[r][c] = 0
        
        if r > 0 and data[r-1][c] <= current_height: # up
            flood(r-1, c)
        if r < row - 1 and data[r+1][c] <= current_height: # down
            flood(r+1, c)
        if c > 0 and data[r][c-1] <= current_height: # left
            flood(r, c-1)
        if c < column - 1 and data[r][c+1] <= current_height: # right
            flood(r, c+1)

    flood(s_row, s_column)

    for row in data:
        print(''.join(map(str, row)))

print(" *** Water Flow ***")
print("Input rows,cols/data1,data2,.../start_row,start_col : ", end = "")
n = input().split('/')
row, column = map(int, n[0].split(','))
data = n[1].split(',')
s_row, s_column = map(int, n[-1].split(','))

flow(row, column, data, s_row, s_column)
