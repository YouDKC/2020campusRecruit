s = input().strip()
result = []
def find(s,res):
    if len(s)>1:
        if int(s[:2])<=26:
            find(s[2:],res+chr(64+int(s[:2])))
        find(s[1:], res+chr(64+int(s[0])))
    elif len(s) == 1:
        result.append(res + chr(64 + int(s)))
    elif len(s) == 0: 
        result.append(res)

find(s,'')
for r in sorted(list(set(result))):
    print(r)
