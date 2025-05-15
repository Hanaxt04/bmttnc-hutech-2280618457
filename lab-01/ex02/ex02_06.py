input_str = input("Nhập x,y: ")
dimensions = [int(x) for x in input_str.split(",")]
rown= dimensions[0]
coln= dimensions[1]
multilist = [[0 for col in range(coln)] for row in range(rown)]
for row in range(rown):
    for col in range(coln):
        multilist[row][col] = row*col
print(multilist),