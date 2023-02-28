import re


def f(mObject):
    #print(mObject.group("g1"))
    return mObject.group("g1")+" "+mObject.group("g2")

text = input()
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"

print(re.sub(pattern, f, text))