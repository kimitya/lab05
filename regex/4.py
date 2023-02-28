import re
pattern = "[A-Z][a-z]+"
text = input()
matches = re.findall(pattern, text)
print(matches)