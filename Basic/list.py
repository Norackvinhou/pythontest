
spam = [['naruto','sasuke','itachi','minato'], [1,2]]
print(spam[1])
print(spam[0])
print(spam[0][1])
print(spam[0][2])
print(spam[1][1])
print(spam[1][0])


spam1=['human','animal','house','anime']
#slice, slice give new list
print(spam1[1:3])

spam1[1:3]= ['anime1','house1']

print(spam1[1:3])

del spam1[0]

print(spam1)

#list function
fun=list('Human')
print(fun)

print(list(range(4)))

anime = ['funny','20','s1']
genre, time, season = anime

print(genre, time, season)


# list method

print(spam1.index('house1'))
spam1.append('this is new')
print(spam1)
spam1.insert(0,"this is insert")
print(spam1)
spam1.remove('this is new')
print(spam1)
