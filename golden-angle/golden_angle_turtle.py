from tkinter import *
import turtle as t

def get_var(a):
    diffvarsum = 0
    for i in range(1, 501):
        lst = []
        diff = []
        for j in range(i):
            lst.append((a * j) % 360)
                    
        lst.sort()

        for l in range(0, i - 1):
            diff.append(lst[l + 1] - lst[l])
        diff.append(360 - lst[i - 1])
            
        diffsum = 0
        for m in range(i):
            diffsum += diff[m]
        diffavg = diffsum / i

        diffvar = 0
        diffsqsum = 0
        for n in range(i):
            diffsqsum += (diff[n]) ** 2
        diffsqavg = diffsqsum / (i)
            
        diffvar = diffsqavg - ((diffavg) ** 2)
        diffvarsum += diffvar
        if i == 500:
            return diffvarsum

def draw():
    entry2.delete(0, END)
    a = float(entry1.get())
    entry2.insert(0, get_var(a))
    t.speed(0)
    t.goto(0, 0)
    for i in range(100):
        t.left(a)
        t.fd(300)
        t.bk(300)
        
def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    t.clear()
    t.goto(0, 0)

t.goto(0, 0)
entry1 = Entry(width = 20)
btn1 = Button(text = '실행', command = draw)
btn2 = Button(text = '삭제', command = clear)
entry2 = Entry(width = 20)
label1 = Label(text = '각도 입력:')
label2 = Label(text = '분산의 합:')
label1.place(x = 205, y = 621)
label2.place(x = 205, y = 650)
btn1.pack()
btn2.pack()
entry1.pack()
entry2.pack()


                

    
    
    
    


