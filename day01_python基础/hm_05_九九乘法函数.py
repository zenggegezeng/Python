def jjcfb():
    #  九九乘法表
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('%s * %s = %s' % (col, row, row * col), end='\t')
            col += 1
        print(" ")
        row += 1



