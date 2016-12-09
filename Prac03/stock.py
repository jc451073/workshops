in_file = open('stock.txt', 'r')
for line in in_file:
    line = line.strip()
    #print(line)
    split_line = line.split(',')
    print('name:', split_line[0])
    print('year:', split_line[1])
    print('price:${:.2f}'.format(float(split_line[2])))
in_file.close()
