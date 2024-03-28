"""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

nterms = int(input("몇 개의 피보나치수를 원하세요?"))

if nterms <= 0:
    print("오류 : 양수를 입력하세요")
else:
    print("Fibonacci 수열: ", end='')
    for i in range(nterms):
        print(fibonacci(i), end='')"""

'''a, b, c = map(int,input("세 개의 숫자를 입력해 주세요: ").split(','))
print(a, b, c)'''


'''a_list = list(map(int,input("세 개의 숫자를 입력해 주세요: ").split(',')))
print(type(a_list))
print(a_list)'''
#list 들어갈 때는 map 함수 앞에 list로 변환해야함
#input output결과가 같으면 굳이 list 함수로 변환할 필요 없음
#출제예상
#구분자가 콤마이므로 입력할 때 콤마 사용하지 않으면 error 발생


#"1,2,3".split(',')

'''a='hello'
b=a.upper()
print(b)'''

#뒤에 오는 입력 값을 앞 괄호에 넣으라는 의미
#여러 개를 숫자와 지정하면 위치 지정하는 것 
'{} Test'.format(10)
'{2} {0} {1} Test'.format("my",100,400)
