#3.1
"""print(100>200)
print(100>=200)
print(100<200)
print(100<=200)
print(100==200)
print(100!=200)
print(200==200)
print(200!=200)
print(True or True)
print(True or False)
print(True and False)
print(True and True)
print(True or True and False)
print(True and True or False)
print('Morning'<'morning')
print('A'<'B')"""


#3.3
"""age = int(input("나이를 입력하시오: "))
height = int(input("키를 입력하시오(단위 cm): "))

if age>=19 and height>=150:
    print("입장할 수 있습니다.")
else:
    print("입장할 수 없습니다.")"""


#3.5
"""a,b = map(int,input("두 정수를 입력하시오: ").split())
if a>b:
    print(a, b)

else:
    print(b, a)"""


#3.7
"""game_score = int(input("게임점수를 입력하시오: "))
if game_score>=1000:
    print("고수입니다.")
else:
    print("입문자입니다.")"""


#3.9**
"""n = int(input("정수를 입력하시오: "))
if (n%2==0) and (n%3==0):
    print(n,"는(은) 2와 3 모두로 나누어집니다.")"""


#3.11
"""a,b,c = map(int,input("세 복권번호를 입력하시오: ").split())

if a==2 and b==3 and c==9:
    print("상금 1억 원 !!! ")
elif a==2 and b==3 and c!=9:
    print("상금 1천만 원")
elif a==2 and b!=3 and c==9:
    print("상금 1천만 원")
elif a!=2 and b==3 and c==9:
    print("상금 1천만 원")
elif a==2 and b!=3 and c!=9:
    print("상금 1만 원")
elif a!=2 and b==3 and c!=9:
    print("상금 1만 원")
elif a!=2 and b!=3 and c==9:
    print("상금 1만 원")
else:
    print("다음 기회에...")"""


#3.13
"""x, y = map(int,input("점의 좌표 x, y를 입력하시오: ").split())

z = ((x-3)**1/2 + (y-4)**1/2) **1/2

if z > 10:
    print("원의 외부에 있음")
else:
    print("원의 내부에 있음")"""


#3.15-1
"""i=0
i = i+1

for i in range(1,10):
    total=2*i
    print('2 *',i,'=',total)"""


#3.15-2
"""i = 0

while i < 9:
    total=2*(i+1)
    i += 1
    print('2 *',i,'=',total)"""


#3.17-1
"""for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')"""

#3.17-2
"""for i in range(3):
    print('Python ')
    print('is ')
print('FUN!')"""

#3.17-3
"""for i in range(3):
    print('Python ')
print('is ')
print('FUN!')"""



#3.19
"""b="b"
c="c"
p="p"

print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")


menu = input("메뉴를 선택하세요(알파벳 b, c, p 입력): ")

if menu == b:
    print("햄버거를 선택하였습니다")
elif menu == c:
    print("치킨을 선택하였습니다")
elif menu == p:
    print("피자를 선택하였습니다")
else:
    print(input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력): "))"""




#3.21
"""n = int(input("숫자를 입력하세요: "))

for i in range(2,n):
    if n%i ==0:
        x=True

if x==True:
    print(n,"는 소수가 아닙니다")
else:
    print(n,"는 소수입니다")"""



#3.23
"""n = int(input("숫자를 입력하세요: "))
iend=n
result=0

for i in range(1,n+1):
    result=(i**2)+result

print(result)"""



#3.25
"""day=0
snail=0

while snail<=30:
    snail+=7
    day+=1
    if snail<30:
        snail-=5
    print("day:", day, "달팽이의 위치:",snail,"미터")

print("우물을 탈출하는데 걸린 날은",day,"일 입니다!!")"""


#3.27
"""print("세 자리의 암스트롱 수: ",end=" ")

for n in range(100,1000,1):
    a=n//100
    b=(n%100)//10
    c=(n%100)%10
    
    total = (a**3)+(b**3)+(c**3)

    if n == total:
        print(n, end=" ")"""



#3.29
"""#초기 연료의 양은 500이고 남은 연료가 10%미만이면 경고 출력하고 수행 끝
fuel = 500
remain = 50

while remain>=10:
    x = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: "))
    fuel = fuel + x
    remain = fuel/10
    if remain>=10:
        print("현재 탱크양은",fuel,"입니다.")
    else:
        print("현재 탱크양은",fuel,"입니다.")
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break"""

