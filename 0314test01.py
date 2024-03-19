#a=100
#print(type(a))

"""print(input("Insert"))
print(input("Insert").split())"""

#print("11 22 33".split())

"""a, b = map(int,input("두 개의 정수를 입력하세요: ").split())
if a%b == 0:
           print("{0:d}는 {1:d}의 배수입니다".format(a, b))"""
#d는정수를쓰라는의미


"""year = int(input("연도를 입력하세요: "))
if (year%400==0) or (year%100!=0) and (year%4==0):
    print(year,"은 윤년입니다.")"""
#교수님이 설명해주신 코드
#if (year%400==0) or (year%4==0) and (year%100==0)


"""total = 0
numbers = [10, 20, 30, 40, 50]
for m in numbers:
    total=total+m
print(total)"""

#아마도 출제할 듯
"""total = 0
for i in range(10):
    total += i
print(total)
    
total = 0
i = 0
while i < 10:
    total += i
    i += 1
print(total)"""
#i가 10보다 작으면 계속 돌리라는 의미
#while True만 쓰면 무한으로 돌아감 ; 대신 if 문으로 조건과 break 넣어주면 끝낼 수 있음
#continue;여러줄이면 밑으로 내려가서 indent..


total = 0
i = 0
while i < 10:
    if i%3==0:
        i += 1
        continue
    total += i
    i += 1
print(total)
#3의 배수면 아래를 진행하지말고 다시 돌아가라는 의미로 continue 사용
