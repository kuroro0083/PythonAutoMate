def printTable(lines):
    space_num = []
    new_lines = []
    for line in lines:
        max = 0
        for i in range(len(line)):
            if i >= len(new_lines):
                new_lines.append([line[i]])
            else:
                new_lines[i].append(line[i])
            if max < len(line[i]):
                max = len(line[i])
        space_num.append(max)
    
    for i in range(len(new_lines)):
        for j in range(len(new_lines[i])):
            if j == 0:
                new_lines[i][j] = new_lines[i][j].rjust(space_num[j])
            else:
                new_lines[i][j] = new_lines[i][j].ljust(space_num[j])

    for line in new_lines:
        print(' '.join(line))

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(tableData)