n = int(input())
zero = 0
positive = 0
negative = 0
for i in range(n):
    n = int(input())
    if n == 0:
        zero += 1
    elif n > 0:
        positive += 1
    else:
        negative += 1
print(zero, positive, negative)