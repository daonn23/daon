#5.1

list_ex=[10,20,30,40,50,60,70]
high=5
low=3
list_ex[low]
list_ex[low+2]
list_ex[high-low]
list_ex[low-high]
list_ex[-1]
list_ex[-low]
list_ex[2*3]
list_ex[2]*3
list_ex[5%4]
len(list_ex)

#5.3

list1=[3,5,7]
list2=[2,3,4,5,6]
#print(type(i))
for i in list1:
    for j in list2:
        print(int(i),'*',int(j),'=',i*j)


#5.5

list1=['I like','I love']
list2=['pancakes.','kiwi juice.','espresso.']

for i in list1:
    for j in list2:
        print(i,'',j)


#5.7

n_list=[10, 20, 30, 50, 60]
n_sum=0
for i in n_list:
    n_sum += i
#print(n_sum)

print("리스트 원소들:",n_list)
print("리스트 원소들의 합:",n_sum)


#5.9

n_list=[10, 20, 30, 50, 60]
n_max=n_list[0]

for i in n_list:
    if n_max < i:
        n_max = i

print("리스트 원소들:",n_list)
print("리스트 원소들 중 최댓값:",n_max)



#5.11

list1=[]
n_list = list(map(int, input('5개의 수를 입력하세요:').split()))

print('합:',sum(n_list))
print('평균:',sum(n_list)/len(n_list))
print('최댓값:',max(n_list))
print('최솟값:',min(n_list))

#45 67 20 34 2



#5.13

import numpy as np

list1=[]
n_list = list(map(int, input('10개의 수를 입력하세요:').split()))

mean_value = np.mean(n_list)
std_value = np.std(n_list)

print('합:',sum(n_list))
print("평균:", mean_value)
print("표준편차:", std_value)

#45 67 20 34 2 100 23 45 67 89



#5.15

greet='Have a beautiful day'

print(greet[0:4])
print(greet[7:16])
print(greet[17:20])



#5.19

s_list=['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list=[]

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)
        
print(new_s_list)
