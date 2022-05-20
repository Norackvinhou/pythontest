## user define exception

# raise Exception('This is the error message')

# def box(symble, width=7, height=5):
#     if len(symble) != 1:
#         raise Exception ('symble can only be 1 char')
#     elif width < 7 and height < 5:
#         raise Exception ('by deafault it is a 7x5, anything lower than this would not work')
#     print(symble * width)
#     for i in range(height-2):
#         print(symble + ' ' * (width - 2 ) + symble)
#     print(symble * width)
    
# box('%%',10,5)
# box('%',7,5)

# to except the error and still let the program running u need to import traceback

# from distutils.log import error 
# import traceback
# import os
# try:
#     raise Exception('This is error message')

# except:
#     errorFile = open('error.log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('the traceback info was written to error log')

# assertion is use to check asanity check
# assert False, 'this is error from assertion'

from code import interact

# normally assert is use for programmer errors
market = {'ns':'green', 'ew':'red'}

def switchlight(insert):
    for key in insert.keys():
        if insert[key]=='green':
            insert[key]='green but modified'
        elif insert[key]=='red':
            insert[key]='red but modified'
    assert 'red' in insert.values(), 'red is red' + str(insert)
print(market)
switchlight(market)
print(market)
