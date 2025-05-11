s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
new = []
for i in set(dictionary):
    if i in s:
        new.append(i)
print(new)
new_s = "".join(new)
print(len(s)-len(new_s))

