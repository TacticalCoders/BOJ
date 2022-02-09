# 잃어버린 괄호
# +, - 로만 이루어진 수식에서 괄호를 적절한 위치에 추가하여 최소값을 만드는 문제
# 70 - 50 + 60을 최소로 만드려면 70 - (50 + 60).
# -가 나온다면 괄호를 열고, 다음 -가 나오기 직전이나 식의 맨 끝에 도착하면 괄호를 닫는다.
# 0으로 시작할수도 있다. ex) 00009

# 리스트를 순차적으로 순회하면서 기본으로는 + 연산 수행
# -를 만나면 다음 -를 만나거나 맨 마지막 항목에 도달할 때까지 - 연산 수행
# -연산을 하다 -를 만난다하더라도 어짜피 또 똑같은 과정이 수행되기 때문에 그냥 계속 - 연산을 수행하면 된다.
# 따라서 가장 좋은 탐욕법은 - 가 나온 이후부터는 계속 - 연산을 하는 것이다.

min_sum = 0
a = input()
cal = ''
token = ''
for i in range(len(a)+1):
    if i == len(a):
        if cal == '-': min_sum -= int(token)
        else: min_sum += int(token)
        break
    if a[i] == '+' or a[i] == '-':
        if cal == '-': min_sum -= int(token)
        elif cal != '-':
            if a[i] == '-': cal = '-'
            min_sum += int(token)
        token = ''
    else:
        token += a[i]
print(min_sum)
