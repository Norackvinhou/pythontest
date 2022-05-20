import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status() ## check if it working or not
print(res.status_code)

#write to file

playFile = open('Romeo.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

print(playFile)
