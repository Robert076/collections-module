from collections import defaultdict

normalDict = {}

normalDict['a'] = 1
# print(normalDict['b'] KeyError 'b' is not defined

defaultDict = defaultdict(lambda: 0)

print(defaultDict[5])
