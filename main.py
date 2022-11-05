import os
CONTENTS = "contents1.txt"
WORDS = "search1.txt"
unkowns = []
words = []
with open(CONTENTS, 'r') as f:
    contents = f.readline()
    while contents != "":
        unkowns.append(list(contents.replace("\n", "").lower()))
        contents = f.readline()
with open(WORDS, 'r') as f:
    contents = f.readline()
    while contents != "":
        words.append(contents.replace("\n", "").lower())
        contents = f.readline()

solutions = {}
longestWord = max([len(x) for x in words])
words = sorted(words)
wordsForward = list(words)
words += ([x[::-1] for x in words]) 
height = len(unkowns)
width = len(unkowns[0])
validLetters = {x[0] for x in words}
for y in range(height):
    for x in range(width):
        if not (unkowns[y][x] in validLetters):
            pass
        else:
            found = False
            word = ""
            increment = 0
            while(x + increment < width and (not found) and (len(word) < longestWord)):
                word = word + (unkowns[y][x + increment])
                if word in words:
                    forward = True
                    if not (word in wordsForward):
                        word = word[::-1]
                        forward = False
                    solutions[word] = [(x, y) if forward else (x + increment, y), "Horizontal", forward]
                    found = True
                increment += 1
            found = False
            word = ""
            increment = 0
            while(y + increment < height and (not found) and (len(word) < longestWord)):
                word = word + (unkowns[y + increment][x])
                if word in words:
                    forward = True
                    if not (word in wordsForward):
                        word = word[::-1]
                        forward = False
                    solutions[word] = [(x, y) if forward else (x, y + increment), "Down", forward]
                    found = True
                increment += 1
            found = False
            word = ""
            increment = 0
            while(y + increment < height and x + increment < width and (not found) and (len(word) < longestWord)):
                word = word + (unkowns[y + increment][x + increment])
                if word in words:
                    forward = True
                    if not (word in wordsForward):
                        word = word[::-1]
                        forward = False
                    solutions[word] = [(x, y) if forward else (x + increment, y + increment), "Diagonal -1", forward]
                    found = True
                increment += 1
            word = ""
            increment = 0
            while(y - increment < height and x + increment < width and (not found) and (len(word) < longestWord)):
                word = word + (unkowns[y - increment][x + increment])
                if word in words:
                    forward = True
                    if not (word in wordsForward):
                        word = word[::-1]
                        forward = False
                    solutions[word] = [(x, y) if forward else (x + increment, y + increment), "Diagonal +1", forward]
                    found = True
                increment += 1
                
            #right
            #down
            #diagnol
found = 0
for key in solutions:
    found += 1
    print("Word: {0} ---> {1}".format(key, solutions[key]))
print(found)