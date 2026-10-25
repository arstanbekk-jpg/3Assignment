# x = int(input())
# s = ""
# while x > 0:
#     l = x % 2
#     s = str(l) + s
#     x //= 2
# print(s)

n = input()
result = 0

for digit in n:
    result = result * 2 + int(digit)

print(result)