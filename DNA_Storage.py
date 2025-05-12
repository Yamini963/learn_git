# t = int(input())
#
# while t > 0:
#     new = ""
#     n = int(input())
#     s = input()
#     # Your code goes
#     for i in range(0,len(s),2):
#         if s[i] == '0' and s[i + 1] == '0':
#             new = new+'A'
#         if s[i] == '0' and s[i+1] == '1':
#             new = new + 'T'
#         if s[i] == '1' and s[i + 1] == '0':
#             new = new + 'C'
#         if s[i] == '1' and s[i+1] == '1':
#             new = new + 'G'
#
#
#     print(new)
#
#
#     t -= 1
#


t = int(input())

while t > 0:
    new = ""
    n = int(input())
    s = input()
    for i in range(0, len(s), 2):
        new = s.replace("00","A").replace("01","T").replace("10","C").replace("11","G")
    print(new)

    t = t-1