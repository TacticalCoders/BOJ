
# 그리디
# 한 선택에서 가장 좋은 옵션이 최적의 해를 보장하는가?
# 풀이 1
# 현재 도시의 가격이 다음 도시의 가격보다 높다면 다음 노드 거리까지만 주유
# 현재 도시의 가격이 다음 도시의 가격보다 낮다면 다다음 노드 거리까지 주유.

# 풀이 2
# 현재 도시의 가격이 모든 도시의 가격(맨 마지막 도시는 제외) 중 가장 낮다면 남은 전체 거리 주유
# 현재 도시의 가격이 모든 도시의 가격 중 가장 낮지 않다면 다음칸 까지만 주유.

n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
total = 0
p_min = p[0]
for i in range(n-1):
    if p[i] < p_min:
        p_min = p[i]
    total += p_min * d[i]
print(total)

# 부분 정답 코드 -> 이중 for문 없이도 풀 수 있었다. 코드를 짜고 더 낮은 시간 복잡도로 구현할 수 있는지 체크할 것.
# n = int(input())
# d = list(map(int, input().split()))
# p = list(map(int, input().split()))
# total = 0
# p_min = min(p[0:n-1])
# for i in range(n-1):
#     if p[i] == p_min:
#         for j in range(i,len(d)):
#             total += p[i] * d[j]
#         break
#     else:
#         total += p[i] * d[i]
# print(total)

