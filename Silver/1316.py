# 그룹 단어 : 단어의 각 문자가 모두 연속으로 나열된 단어. aabbbccb는 그룹단어가 아니다.
n = int(input())
words = []


def is_group(s):
    data = []
    for now in list(s):
        if now not in data:
            data.append(now)
            continue
        else:
            if data[-1] != now:
                return False
    return True


for _ in range(n):
    words.append(input())
count = 0
for word in words:
    if is_group(word):
        count += 1
print(count)
