#4.1

'''def my_greet():
    print("환영합니다.")
    
my_greet()
my_greet()'''


#4.3

'''m=200
n=100

def max2(m,n):
    if m>n:
        return m
    else:
        return n

def min2(m,n):
    if m<n:
        return m
    else:
        return n

print("100과 200 중 큰 수는: ",m)
print("100과 200 중 작은 수는: ",n)'''



#4.5

'''def inch2cm():
    cm=inch*2.54
    return

for i in range(0,5):
    i += 1
    cm=i*2.54
    print(i,'인치=',cm,'센티미터')'''



#4.7

'''a, b, c = map(int,input("세 개의 숫자를 입력해 주세요: ").split())
#print(a, b, c)
def get_m(a,b,c):
    mean3=(a+b+c)/3
    max3=max(a,b,c)
    min3=min(a,b,c)
    return mean3, max3, min3

mean3, max3, min3 = get_m(a,b,c)

print(a,b,c,'의 평균값은',mean3)
print(a,b,c,'의 최댓값은',max3)
print(a,b,c,'의 최솟값은',min3)'''


#4.9

'''nums=list(map(int,input('정수를 여러 개 입력하시오: ').split()))

def mean_of_n(nums):
    mean1=sum(nums)/len(nums)
    return mean1

def max_of_n(nums):
    max1=max(nums)
    return max1

def min_of_n(nums):
    min1=min(nums)
    return min1

mean1=mean_of_n(nums)
max1=max_of_n(nums)
min1=min_of_n(nums)

print('평균값은',"{:.1f}".format(mean1))
print('최댓값은',max1)
print('최솟값은',min1)'''


#4.11

'''x1=int(input('x1 좌표를 입력하시오: '))
y1=int(input('y1 좌표를 입력하시오: '))
x2=int(input('x2 좌표를 입력하시오: '))
y2=int(input('y2 좌표를 입력하시오: '))

x2>x1
y2>y1

def area(x1,y1,x2,y2):
    r_area=((x2-x1)*(y2-y1))/2
    return r_area

r_area=area(x1,y1,x2,y2)

print('직각삼각형의 면적은',r_area)'''


#4.15

'''def my_sort(*nums):
    my_sort=[]
    for i in nums:
        my_sort.append(i)
        my_sort.sort()
    return my_sort

print(my_sort(45,3,4,56,5))
print(my_sort(9,8,7,6,5,4,3))'''



#4.17

'''def sum_range(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        sum += i
    return sum

#sum=sum_range(n1,n2)
n1=10
n2=20
print(n1,'에서',n2,'까지의 정수의 합: ',sum_range(n1,n2))

n1=40
n2=100
print(n1,'에서',n2,'까지의 정수의 합: ',sum_range(n1,n2))'''




#4.19

'''def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    

n=int(input('fibo(n)의 n을 입력하세요: '))
print('fibo(',n,')=',fibo(n))'''



#4.21

'''num=input('주민등록번호 첫 6숫자 형식 입력: ')

yr = num[0:2]
mon = num[2:4]
day = num[4:6]

if num[0:2] < str(50):
    yr = '20' + yr
else:
    yr = '19' + yr
    
print(yr,'년',mon,'월',day,'일')'''




