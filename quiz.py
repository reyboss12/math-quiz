import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
h = random.randint(1,100)
score = 0
print(a, "+" ,b, "=")

first = int(input("what is your answer?   "))

if first == a + b:
  score += 1
elif first != a+b:
  score = score -1

print(c, "+" ,d, "=")

second = int(input("what is your answer?   "))

if second == c + d:
  score += 1
elif second != c+d:
  score = score -1

print(e, "+" ,f, "=")

third = int(input("what is your answer?   "))

if third == e + f:
  score += 1
elif third != e+f:
  score = score -1

print(g, "+" ,h, "=")

fourth = int(input("what is your answer?   "))

if fourth == g + h:
  fourth += 1
elif fourth != g+h:
  score = score -1
