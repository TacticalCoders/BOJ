# 1000이하의 자연수가 중, 한수를 모두 구하여라
# 한수 : 어떤 자연수의 각 자리수가 등차수열을 이루는 것

#정답
def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))

# 내가 작성한 답 -> 시간 초과 (등차 수열의 성질을 이용하지 못하고 무식하게 짬)
# def getCount(n):
#     if len(n) == 1:
#         return n[0]
#     count = 0
#     for d in range(-9, 10):
#         ishan = True
#         a = n[0]
#         for i in range(len(n) - 1):
#             a = a + d
#             if a >= 10 or a < 0 or a > n[i + 1]:
#                 ishan = False
#                 break
#         if ishan:
#             count = count + 1
#
#     for j in range(len(n)):
#         if j == 0:
#             x = n[j]
#         elif j == len(n) - 1:
#             count = count + 9
#             return count
#         else:
#             x = 10
#         while x > 0:
#             x = x - 1
#             if x == 0:
#                 break
#             for d in range(-9, 10):
#                 a = x
#                 ishan = True
#                 for i in range(len(n) - (j + 1)):
#                     a = a + d
#                     if a >= 10 or a < 0:
#                         ishan = False
#                         break
#                 if ishan:
#                     count = count + 1
#
#     return count
#
# n_int = input()
# n_list = [int(i) for i in n_int]
# j = 0
# while True:
#     if n_list[j] == 0:
#         del n_list[j]
#     if j == len(n_list) - 1 or n_list[j+1] != 0:
#         break
# print(getCount(n_list))