import re

pattern = "ab{2,3}"
text = input()
matches = re.findall(pattern, text)
print(matches)