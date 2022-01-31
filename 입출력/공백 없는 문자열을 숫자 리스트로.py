n = int(input())
data = list(map(int,list(input()))) #split()은 공백 기준이므로 입력에 공백이 없다면 이런 방식을 취해야 한다.
sum = 0
for i in data:
  sum = sum + i
print(sum)