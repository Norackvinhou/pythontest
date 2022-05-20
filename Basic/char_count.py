import pprint
message = "i am from computer science and today is saturday"

count = {}

for char in message.upper():
    count.setdefault(char,0)
    count[char]+= 1

txt=pprint.pformat(count)

print(txt)

# dictionary data structure


anime= {"title":"one piece", "genre":"advanture"}
all_anime = []

all_anime.append({"title":"death note", "genre":"mystery"})
all_anime.append({"title":"fairy tail", "genre":"mystery and advanture"})


print(all_anime)

