# program to get the view of pornhub vido, just copy link address to the clipboard and then run this program
import bs4, requests, webbrowser, pyperclip, sys
sys.argv

def get_view(view):
    res = requests.get(view)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#hd-leftColVideoPage > div:nth-child(1) > div.video-actions-menu > div.ratingInfo > div.views > span')
    return elem[0].text.strip()

url = pyperclip.paste()
view = get_view(url)
print('the view for this video is:'+ view)

goto = int(input('tpye 1 to see video, or 2 to exit:'))
if(goto == 1):
    webbrowser.open(url)
else:
    print('goodbye')