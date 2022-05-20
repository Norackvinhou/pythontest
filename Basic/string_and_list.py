n1=list("hello")
print(n1)


#string is actully a list of char
name="jack"
print(name[0])
#but u cannot reassign letter to the string
# name[0]='k'  this doesnt work cuz string is immuable
print(name)

#to work around this we can use
newName= 'k' + name[1:len(name)]
print(newName)



# referencing 

coco = [1,2,3]
caca = coco
coco[0]=7

# both is the same cuz its refer to the memeory
print(coco,"\n",caca)
#to make around this we can use copy
import copy
koko = ['A','B','C']
kaka = copy.deepcopy(koko)
koko[0]='Z'

print(koko,'\n', kaka)