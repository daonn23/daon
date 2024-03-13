#2.1
"""print(200 ,'+', 300 ,'+', 400 ,'=', 200 + 300 + 400)"""

#2.3
"""width = 30
height = 60
area = width * height
print(area)"""

#2.5
"""x = int(input('정사각형의 밑변을 입력하시오 : '))
print(str(x**2))"""

#2.7
"""x = str(10*9*8*7*6*5*4*3*2*1)
print('10''!' '=' +x)"""

#2.9
"""fahrenheit = (9/5) * celsius + 32

celsius = [' 0', 10, 20, 30, 40, 50]
fahrenheit = []

for i in range(6):
    #fahrenheit.append((9/5) * float(celsius[i]) + 32)


print('섭씨','   ', '화씨')

for i in range(6):
    print(str(celsius[i]),'   ', str(fahrenheit[i]))"""

#2.11
"""x = int(input('화씨 온도를 입력하세요 : '))
y = celsius
y = (5/9) * (x - 32)

print('화씨', int(x), '도는 섭씨', float(y), '도 입니다.')"""

#2.13
"""r = float(input('원의 반지름을 입력하세요: '))
PI = 3.141592

a = 2 * PI * r
b = PI * (r**2)

print('원의 둘레 =',float(a),',','원의 면적 =' ,float(b))"""

#2.15
"""a = int(input('밑변의 길이를 입력하세요: '))
b = int(input('높이의 길이를 입력하세요: '))

c = (a**2 + b**2)**(1/2)

print('빗변의 길이: ',float(c))"""

#2.17
"""print(2<<0, end=' ')
print(2<<1, end=' ')
print(2<<2, end=' ')
print(2<<3, end=' ')
print(2<<4, end=' ')
print(2<<5, end=' ')
print(2<<6, end=' ')
print(2<<7, end=' ')
print(2<<8, end=' ')
print(2<<9, end=' ')"""

#2.19
"""n = int(input('정수를 입력하세요: '))

if 0<=n<=100 and n%2==0:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True')
else:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False')"""

#2.21
"""n=int(input('정수를 입력하세요: '))

print(int(n),'의 2진수 값:',bin(n))
print(int(n),'의 2진수 값에 대한 비트단위 부정값:',bin(~n))"""

#2.23
n = int(input('세 자리 정수를 입력하세요: '))

print('백의 자리: ',n//100)
print('십의 자리: ',n%100//10)
print('일의 자리: ',n%10)

