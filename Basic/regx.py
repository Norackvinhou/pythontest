import re

# mess= "Good day welcome to our company contact us viea 111-222-333"
# mess1= "Good day welcome to our company contact us viea 222-333"



# phone= re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d)')
# mo = phone.search(mess)
# mo1 = phone.search(mess1)
# print(mo.group())
# print(mo1.group())
# print(mo.group(1))
# print(mo.group(2))

# batRegx = re.compile(r'Bat(man|mobile|bat)')
# mo2 = batRegx.search('Batman lost a wheel man')
# print(mo2)

# another_regx = re.compile(r'Bat(wo)?man')
# mo3 = another_regx.search("this is really Batman")
# print(mo3.group())

# wo can appear as many time
# another_regx = re.compile(r'Bat(wo)*man')
# mo3 = another_regx.search("this is really Batwowowoman")
# print(mo3.group())

## the + return 1 or more time
# another_regx = re.compile(r'Bat(wo)+man')
# mo3 = another_regx.search("this is really Batwoman")
# print(mo3.group())


# phone = re.compile(r'((\d-\d-\d-)?\d\d\d-\d\d\d(,)?){3}')
# mo = phone.search("thing are just nuumber: 111-222-333,444-444,777-777-777")
# print(mo.group())

## by default if we try to match between 3 and 5 digit it match 5 digit
# yes = re.compile(r'(\d){3,5}')
# mo = yes.search("123456789")
# print(mo)

# this is to make it match 3 digit is between 3 and 5
# yes = re.compile(r'(\d){3,5}?')
# mo = yes.search("123456789")
# print(mo)

## return a list of string
# yes = re.compile(r'(\d)')
# mo = yes.findall("123456789")
# print(mo)

#return a tuble of its have different group
# yes = re.compile(r'(\d\d)(\d\d)')
# mo = yes.findall("123456789")
# print(mo)


# beginswithhello= re.compile(r'^Hello')
# mo = beginswithhello.search("Hello there!")
# print(mo)

# beginswithhello= re.compile(r'there!$')
# mo = beginswithhello.search("Hello there!")
# print(mo)


# name = re.compile(r'Agent \w+')
# mo = name.findall('Agent Lock gave the pillow to me with Agent Alice')
# print(mo)
# mo = name.sub('NONO', 'Agent Lock gave the pillow to me with Agent Alice')
# print(mo)

name = re.compile(r'Agent (\w)\w+')
mo = name.findall('Agent Lock gave the pillow to me with Agent Alice')
print(mo)
mo = name.sub(r'Agent \1***', 'Agent Lock gave the pillow to me with Agent Alice')
print(mo)

