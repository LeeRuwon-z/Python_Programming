# for문

# for (int i = 0; i < 10; i++)       이건 C에서
# for x in iterable객체:             이건 python에서

for i in range(5):              # 0 ~ 4
    print(i,end=" ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1,6):
    print(i,end=" ")
print()

# 1 ~ 10, 2칸씩
for i in range(1,11,2):
    print(i,end=" ")
print()

# 5, 4, 3, 2, 1 거꾸로
for i in range(5,0,-1):
    print(i, end=" ")
print()

# 1 ~ 10까지 합
tot = 0
for i in range(1,11):
    tot += i
else:
    print(f"sum = {tot}")

print(sum(range(1,11)))

s = "hi12!@한글韓國🔥😊"

for c in s:
    print(c,end=" ")

print(len(s))

# 구구단 출력
# 2 * 1 = 2
# 2 * 2 = 4

for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:<5d}",end="")
    print()
else:
    print("End")