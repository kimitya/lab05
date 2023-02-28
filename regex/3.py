import re

pattern = "[a-z]+_[a-z]+"
text = input()
matches = re.findall(pattern, text)
print(matches)