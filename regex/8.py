import re

txt=input()
pattern = "[A-Z]"
x = re.split(pattern, txt)
print(x)