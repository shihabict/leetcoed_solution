import re

S = int(input())
for i in range(S):
    pattern1 = re.compile(r'(?<= )(&&)(?= )')
    pattern2 = re.compile(r'(?<= )(\|\|)(?= )')
    print(pattern2.sub('or', pattern1.sub('and', input())))

