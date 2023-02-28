import re
pattern="a.+b"
text = input()
ans = re.findall(pattern, text)
print(ans)