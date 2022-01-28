#10으로 나눴을 때 몫이 0 -> 1의 자리 수
#100으로 나눴을 때 몫이 0 -> 10자리 수
#1000으로 나눴을 때 몫이 0 -> 100의 자리 수
def d(n):
    sum = 0
    digit = 10
    while int(n/digit) != 0:
        digit *= 10
    sum += n
    while True:
        digit = int(digit / 10)
        quotient = int(n / digit)
        remainder = n % digit
        sum += quotient
        n = remainder
        if int(remainder/10) == 0: #연산 후 반복 종료
            sum += remainder
            return sum
i = 1
a = []
for l in range(10000):
    a.append(d(i))
    i = i + 1
for i in range(1,10001):
    if i in a:
        continue
    else:
        print(i)