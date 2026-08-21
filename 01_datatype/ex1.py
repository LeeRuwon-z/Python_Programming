# 변수
a = 2
b = 3
print(a,end = "") #엔터(한줄 내려쓰기) 제거
print(b)
print(a,b,sep="") #print(a,b,sep=",") -> 중간에 띄어쓰기 제거

#a = 2, b = 3 # -> a = (2, b) = 3
a = 2; b = 3
print(a, b)

a,b = 2,3       #투플 언패킹
print(a, b)

a = b = c = 0

# 값 swap
a, b = 2, 3
temp = a
a = b
b = temp
print(a,b)

a, b = b, a
print(a, b)

# 변수명 규칙(C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가
# snake_case
# camelCase

#name! = "pororo" name! 이거 안됨
#2name = "pororo" 2name 이것도 안됨
#class = "test" 이것도 안됨

이름 = "뽀로로" #가능은 한데 사용은 자제
print(이름)