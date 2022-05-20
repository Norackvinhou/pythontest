base=int(input("base length:"))
height=int(input("height length:"))
char_para=input("charactor to parallel:")
char_fill=input("charctor to fill:")

area= base * height
print (area)

for row in range (1,height+1):
    for x in range (height-row):
        print(char_fill,end='')
    for x in range (1,base+1):
        print(char_para,end='')
    for x in range (row-1):
        print(char_fill,end='')
    print()