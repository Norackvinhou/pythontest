import re, pyperclip

# regx for phone number
phone = re.compile(r'''
#it could look like 111-222-3333, (111) 222-3333, 222-3333 ext 12345, ext. 12345, x12345

(((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)   #first seperator
\d\d\d  #first 3 digit
-   #seperator
\d\d\d\d#last 4 digit
(((ext(\.)?\s)|x)(\d{2,5}))?)#ext(optional)

''',re.VERBOSE)

## regx for email
email = re.compile(r'''

[a-zA-Z0-9_.+]+#name
@  #@
[a-zA-Z0-9_.+]+#domain name

''', re.VERBOSE)

#get txt out of clipboard

txt = pyperclip.paste()
#extract phone and email
extractphone = phone.findall(txt)
extractemail = email.findall(txt)


# print(extractphone)
allPH=[]
for phNum in extractphone:
    allPH.append(phNum[0])
# print(allPH)

result='\n'.join(allPH) + '\n'.join(extractemail)
pyperclip.copy(result)