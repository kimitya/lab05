import re

pattern = r"ab*"
text = input()
a  = re.findall(pattern, text)
print(a)