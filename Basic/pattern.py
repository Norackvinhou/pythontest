height=int(input("height of the tree"))
char_tree=input("charactor of the tree")
char_fill=input("char to fill the free")


# %%%%%%%%%%%%%%%%%%%
# *%%%%%%%%%%%%%%%%%*
# **%%%%%%%%%%%%%%%**
# ***%%%%%%%%%%%%%***
# ****%%%%%%%%%%%****
# *****%%%%%%%%%*****
# ******%%%%%%%******
# *******%%%%%*******
# ********%%%********
# *********%*********

for row in range(height,0,-1):
    for x in range(height-row):
        print(char_fill,end='')
    for x in range (2*row-1):
        print(char_tree,end='')
    for x in range(height-row):
        print(char_fill,end='')
    print()


# &&&&*&&&&
# &&&***&&&
# &&*****&&
# &*******&
# *********
# for row in range(1,height+1):
#     for x in range(height-row):
#         print(char_fill,end='')
#     for x in range (2*row-1):
#         print(char_tree,end='')
#     for x in range(height-row):
#         print(char_fill,end='')
#     print()


# primes = []

# while(n<=1):
#     n =int(input("give number above 1:"))

# for i in range(2, n + 1):
#     root=int(math.sqrt(i))
#     for j in range(2, root + 1):
#  	    if i%j == 0:
#  		    break
#     else:
# 	    primes.append(i)

# print(primes)