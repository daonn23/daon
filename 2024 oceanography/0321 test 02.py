def hyacsu(a):#정수의진약수구하는거
    hap=0
    for m in range(1,a):
        if a%m == 0:
            hap += m
    return hap
d=hyacsu(18)
print(d)
