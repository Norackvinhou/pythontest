import webbrowser, sys, pyperclip

## sys.arv is a argument for commandline
sys.argv 
#check if cmd line argument were passed
# argument that were passed is in this form ['web.py', '870' 'Valecia', 'St.']
if len(sys.argv) > 1:
    #['web.py', '870' 'Valecia', 'St.'] we want this format to be in a signle string
    address = ' '.join(sys.argv[1:])
else:
    # else we assume they have a cilpboard
    # 219 Keo Chenda St
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#if want to run go to cmd in this directory and syntax is
# -> python web.py 219 Keo Chenda St
# anther syntax is we need to copy the address and just run web.py
