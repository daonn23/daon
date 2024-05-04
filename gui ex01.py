'''from tkinter import *
# module 불러옴 

window = Tk()
# window라는 instance를 하나 만든 것
# 대소문자 주의할 것
# 시작 코드

# 이 부분에서 화면 구성하고 처리 : event
window.title('윈도창 연습')
window.geometry('400x100')
window.resizable(width=FALSE, height=FALSE)
# 크기 지정해서 조절이 안 됨 

window.mainloop()
# loop의 끝'''



'''from tkinter import *
window = Tk()

label1 = Label(window, text='COOKBOOK~~ Python을')
label2 = Label(window, text='열심히', font=('고딕체',25),fg='blue')
label3 = Label(window, text='공부 중입니다.',bg='white',width=20,height=5,anchor=SE)
# label로 문자, 색, 폰트 등 설정 가능
# anchor를 사용해서 위치 지정

label1.pack()
label2.pack()
label3.pack()

window.mainloop()'''




'''from tkinter import *
window = Tk()

photo = PhotoImage(file='image2.gif')
label1 = Label(window, image=photo)

label1.pack()
# 사진을 쌓는 것
# 4가지의 option을 가짐 : up의 경우 아래에서 위로 쌓음 

window.mainloop()'''





'''from tkinter import *
window = Tk()

button01 = Button(window, text='파이썬 종료', fg='red', command=quit)

button01.pack()

window.mainloop()'''


'''from tkinter import *
window = Tk()

# 함수 선언 부분
# var에 저장하는 방법 
def myFunc():
    if var.get()==1:
        label1.configure(text='파이썬')
    elif var.get() == 2:
        label.configure(text='C++')
    else:
        label1.configure(text='Java')


# 메인 코드 부분
var = IntVar()
rb1 = Radiobutton(window, text='파이썬', variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text='C++', variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text='Java', variable=var, value=1, command=myFunc)
# 셋 중 하나를 선택 
label1 = Label(window, text='내가 선택한 언어:',fg='red')

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()'''




from tkinter import *
window = Tk()

btnList = [None] * 3

for i in range(0,3):
    btnList[i] = Button(window, text='버튼'+str(i+1))

for btn in btnList:
    btn.pack(side = RIGHT)

window.mainloop()






























































