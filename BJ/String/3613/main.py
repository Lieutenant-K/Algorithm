import sys
input = sys.stdin.readline
import re

s = input().rstrip()
if s[0] == '_' or s[-1] == '_' or "__" in s:
    print("Error!")
    exit()

if s.islower():
    r = [sub.capitalize() for sub in s.split('_')]
    r[0] = r[0].lower()
    print("".join(r))
else:
    if 'A' <= s[0] <= 'Z' or '_' in s:
        print("Error!")
        exit()
    s = s[0].upper() + s[1:]
    pattern = re.compile(r'[A-Z][a-z]*')
    r = map(lambda x: x.lower(), pattern.findall(s))
    print("_".join(r))