import re

def f(mObject):
    return mObject.group("g1")+mObject.group("g3").upper()

text = input()
pattern = "(?P<g1>[a-z])(?P<g2>_)(?P<g3>[a-z])"

print(re.sub(pattern, f, text))


