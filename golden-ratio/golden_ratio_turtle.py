from tkinter import *
import turtle as t

def get_var(a):
    diffvarsum = 0
    for i in range(1, 501):
        lst = []
        diff = []
        for j in range(i):
            lst.append((a / 10000 * j) % 1)
                    
        lst.sort()

        for l in range(0, i - 1):
            diff.append(lst[l + 1] - lst[l])
        diff.append(1 - lst[i - 1])
            
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
t.speed(0)

def draw_rectangle():
    t.up()
    t.goto(-300, 50)
    t.right(90)
    t.down()
    t.fd(100)
    t.left(90)
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(600)
    t.up()
    t.goto(0, 0)
    t.right(180)
    
def write():
    entry2.delete(0, END)
    a = float(entry1.get()) * 10000
    entry2.insert(0, get_var(a))
    draw_rectangle()
    t.up()
    t.goto(-300, 50)
    t.down()
    for i in range(100):
        x = ((a / 10000 * i) % 1) * 600 - 300
        t.goto(x, 50)
        t.right(90)
        t.fd(100)
        t.bk(100)
        t.left(90)
        
def delete():
    entry1.delete(0, END)
    entry2.delete(0, END)
    t.clear()
    t.up()
    t.goto(0, 0)
t.goto(0, 0)
entry1 = Entry(width = 20)
btn1 = Button(text = '실행', command = write)
btn2 = Button(text = '삭제', command = delete)
entry2 = Entry(width = 20)
label1 = Label(text = '0에서 1사이의 값:')
label2 = Label(text = '분산의 합:')
label1.place(x = 165, y = 621)
label2.place(x = 205, y = 650)
btn1.pack()
btn2.pack()
entry1.pack()
entry2.pack()
