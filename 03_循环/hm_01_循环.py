
row = 9

while row <= 9:
    col = 1
    while col <= row:
        print(col)
        print("%d*%d=%2d" % (col, row, col * row), end=" ")
        col += 1
    print('row %d', row)
    row += 1