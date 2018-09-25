s = "Eva, Can I Stab Bats In A Cave?"
ss = s.lower()
sss = ss.split()
newStr = "".join(sss)
alpha = "abcdefghijklmnopqrstuvwxyz"

newS = ""
for i in newStr:
    if i in alpha:
        newS += i

begin = 0
ending = len(newS) - 1

while begin <= ending:
    if (newS[begin] != newS[ending]):
        print("NO")
        break
    begin += 1
    ending -= 1

print("all set")
