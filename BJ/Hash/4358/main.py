import sys
input = sys.stdin.readline
from collections import Counter

trees = []
while True:
    tree = input().rstrip()
    if tree == "":
        break
    trees.append(tree)

dic = Counter(trees)
for key in sorted(dic.keys()):
    print("%s %.4f" % (key, round(100 * dic[key] / len(trees), 4)))