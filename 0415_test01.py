#from tkinter import*   #tk.TK()를 TK만 사용하도록 하기 위해 * 사용
#window = Tk()


'''window.title('윈도창 연습')
window.geometry('400x100')
window.resizable(width=TRUE, height=TRUE)   #true로 바꾸면 조절이 가


window.mainloop()'''



'''label1 = Label(window, text='COOKBOOK~~ Python을')
label2 = Label(window, text='열심히', font=('궁서체',30),fg='blue')
label3 = Label(window, text='공부 중입니다',bg='magenta',width=20,height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()'''



'''label1 = Label(window, text='오늘 하루도')
label2 = Label(window, text='열심히', font=('고딕체',25),fg='blue')
label3 = Label(window, text='숨 쉬기~',bg='pink',width=20,height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()'''


'''window.title('GUI exercise')

photo1 = PhotoImage(file='image2.gif')
label1=Label(window, image=photo1)
#photo2 = PhotoImage(file='image3.gif')
#label2=Label(window, image=photo2)

label1.pack(side=LEFT)
#label2.pack(side=LEFT)

label1.pack()

window.mainloop()'''


'''button1 = Button(window, text='파이썬 종료', fg='red',command=quit)

button1.pack()

window.mainloop()'''


'''from tkinter import*
from tkinter import messagebox

def myFunc():
    messagebox.showinfo('강아지버튼','강아지가 귀엽져~^^')

window = TK()

photo = PhotoImage(file='image2.gif')
button1 = Button(window,image=photo,command=myFunc)

button1.pack()

window.mainloop()'''



from tkinter import *
from tkinter import messagebox

window = Tk()  #대소문자 구분하니까 주의하기 

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("","체크버튼이 꺼졌어요")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요")

chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요",variable = chk, command = myFunc)

cb1.pack()

window.mainloop()


        
        










