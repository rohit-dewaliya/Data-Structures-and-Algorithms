def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    index, step = 0, 1

    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return "".join(rows)

    '''
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag_array = [[" "] * len(s) for _ in range(numRows)]
    row, col = 0, 0
    going_down = True

    for char in s:
        zigzag_array[row][col] = char

        if going_down:
            if row < numRows - 1:
                row += 1
            else:
                going_down = False
                row -= 1
                col += 1
        else:
            if row > 0:
                row -= 1
                col += 1
            else:
                going_down = True
                row += 1

    # Build result string by reading row by row
    result = ""
    for r in zigzag_array:
        result += "".join(r).replace(" ", "")

    return result
    '''

# ---- Test ----
print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(convert("A", 1))               # A
