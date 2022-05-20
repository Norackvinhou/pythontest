
def triangle(height):
    for row in range(1,height+1):
        for x in range(height-row):
            print(" ",end='')
        for x in range (2*row-1):
            print("*",end='')
        for x in range(height-row):
            print(" ",end='')
        print()

def square(height):
    for row in range (1,height+1):
        for column in range (1,height+1):
            print("*",end='')
        print()

def para(height):
    for row in range (1,height+1):
        for x in range (height-row):
            print(" ",end='')
        for x in range (1,height+1):
            print("*",end='')
        for x in range (row-1):
            print(" ",end='')
        print()

def line_break():
    print("----------")



tri=int(input("height of the triangle(t):"))
squ=int(input("height of the square(s):"))
par=int(input("height of the paralellogram(p):"))
mn = input("how many do u want to print(eg: t1 s1 p2)")

x= mn.split(' ')


for i in x:
    if(x[0]=='t'):
        tx=int(x[1])
    elif(x[0]=='s'):
        sy=int(x[1])
    elif(x[0]=='p'):
        pz=int(x[1])

for i in y:
    if(x[1]=='t'):
        tx=int(y[1])
    elif(x[1]=='s'):
        sy=int(y[1])
    elif(x[1]=='p'):
        pz=int(x[1])

# for i in z:
#     if(z[0]=='t'):
#         tx=int(z[1])
#     elif(z[0]=='s'):
#         sy=int(z[1])
#     elif(z[0]=='p'):
#         pz=int(z[1])

# def qty(t=0,s=0,p=0):
#     for i in range (0,t):
#         triangle(tri)
#         line_break()
    
#     for i in range (0,s):
#         square(squ)
#         line_break()
    
#     for i in range (0,p):
#         para(par)
#         line_break()
    

# qty(t=tx,s=sy,p=pz)