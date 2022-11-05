import os

def letter_search(y, x, words, unkown):
    maxH = unkown.len()
    maxW = unkown[0].len()
    



unkowns = []
with open("contents.txt", 'r') as f:
    contents = f.readline()
    while contents != "":
        unkowns.append(list(contents[:-1]))
        contents = f.readline()

height = unkowns.len()
width = unkowns[0].len()
