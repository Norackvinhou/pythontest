path = 'D:\\pyfile\\img.png'
pathr= r'D:\pufile\img.png'

print(path,'\n', pathr)

import os
print(os.path.join('folder1','folder2','img.png'))
print(os.sep)

print(os.getcwd())
# path
#.  and ..
# exists
# isfile
# isdir
# os.path.dirname
# os.path.basename
# os.path.getsize
# os.listdir(this is u put path)
print(os.listdir(os.getcwd()))
size = 0
opath ='D:\\playground\\python_playground\\Basic'
for filename in os.listdir(opath):
    if not os.path.isfile(os.path.join(opath, filename)):
        continue
    size += os.path.getsize(os.path.join(opath, filename))

print(size)