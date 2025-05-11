# a = int(input())
# b = int(input())
#
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
#
# print(max(a,b))
# print(min(a,b))
from unicodedata import digit

a = [12,24,36,48,52]
total = sum(a)
print(total)
print(total/len(a))

new = []
for i in a:
    count = 0
    for x in str(i):
        count = count+int(x)
    new.append(count)




