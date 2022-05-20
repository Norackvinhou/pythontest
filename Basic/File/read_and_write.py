import os

# helloFile=open('D:\\playground\\python_playground\\Basic\\File\\hello.txt')
# h=helloFile.readlines()
# print(h)
# helloFile.close()

##write to a file if file no have it create it
# helloFile=open('D:\\playground\\python_playground\\Basic\\File\\hello2.txt','w')
# helloFile.write("This is writning from a code :)")
# helloFile.close()

#this code is for appending a file 
# helloFile=open('D:\\playground\\python_playground\\Basic\\File\\hello2.txt','a')
# helloFile.write("\n and this is appending ")
# helloFile.close()

#sotring dictionary or list...
# import shelve
# shelfFile = shelve.open('D:\\playground\\python_playground\\Basic\\File\\cats')
# shelfFile['cats']= ['riky','phlusfy','fishy']
# shelfFile.close()

# shelfFile = shelve.open('D:\\playground\\python_playground\\Basic\\File\\cats')
# print(shelfFile['cats'])

#impoty shutil 
# THIS shutil is use to copy or move file 

# delete file is use in the os library
# os.unlink(), os.rmdir()

#these deletion cannot be recover
# another delte is useing shutil
# shutil.rmtree(),
# 
#  to send it to recycle bin or send to trash
#  we use send2trash 
#  send2trsah.send2trash()

#use os.walk() to list directory (simiilar to ls in linux)