import os
unkowns = []
words = []
with open("contents.txt", 'r') as f:
    contents = f.readline()
    while contents != "":
        unkowns.append(list(contents.replace("\n", "").lower()))
        contents = f.readline()
with open("search.txt", 'r') as f:
    contents = f.readline()
    while contents != "":
        words.append(contents.replace("\n", "").lower())
        contents = f.readline()

longestWord = max([len(x) for x in words])
words = sorted(words)
words.append([x[::-1] for x in words]) 
height = len(unkowns)
width = len(unkowns[0])
validLetters = {x[0] for x in words}
for y in range(height):
    for x in range(width):
        found = False
        increment = 0
        if not (unkowns[y][x] in validLetters):
            pass
        else:
            if not found:
                word = ""
                while(x + increment < width and (not found) and (len(word) < longestWord)):
                    word = word + (unkowns[y][x + increment])
                    if word in words:
                        print(word)
                        found = True
                    increment += 1
                word = ""
                while(y + increment < height and (not found) and (len(word) < longestWord)):
                    word = word + (unkowns[y + increment][x])
                    if word in words:
                        print(word)
                        found = True
                    increment += 1
                    
            #right
            #down
            #diagnol
