# Author: ankan2526

from tkinter import *

sudoku = [[0 for i in range(9)] for j in range(9)]

def error(message):
    color = "red"
    if message=="Solution found!":
        color ="green"
    lbl_msg = Label(root, text = message, fg=color, relief="solid")
    lbl_msg.place(x=160,y=250)

def isValidSudoku(board):
    # checking rows and columns
    for i in range(9):
        store1=set()
        store2=[]
        for j in range(9):
            store1.add(board[i][j])
            store2.append(board[i][j])
        if len(store1)!=len(store2):
            return False
        store1=set()
        store2=[]
        for j in range(9):
            store1.add(board[j][i])
            store2.append(board[j][i])
        if len(store1)!=len(store2):
            return False
    
    # checking squares
    for i in range(0,9,3):
        for j in range(0,9,3):
            store1=set()
            store2=[]
            for k in range(3):
                for l in range(3):
                    store1.add(board[i+k][j+l])
                    store2.append(board[i+k][j+l])
            if len(store1)!=len(store2):
                return False    
    return True

def check(todo,hlines,vlines,boxes,arr):
    if len(todo)==0:
        if isValidSudoku(arr)==False:
            return False
        print("Solution:")
        for i in range(9):
            x=list(arr[i])
            print(*x)
        for i in range(9):
            for j in range(9):
                sdk[i][j].configure(text='  '+str(arr[i][j])+'  ')
        return True
    p=todo.pop()
    x,y=p[0],p[1]
    for i in range(1,10):
        if i not in hlines[x] and i not in vlines[y] and i not in boxes[x//3][y//3]:
            hlines[x].add(i)
            vlines[y].add(i)
            boxes[x//3][y//3].add(i)
            arr[x][y]=str(i)
            if check(todo,hlines,vlines,boxes,arr)==1:
                return 1
            hlines[x].remove(i)
            vlines[y].remove(i)
            boxes[x//3][y//3].remove(i)
    todo.append([x,y])
    return 0

def solve(a):
    todo=[]
    hlines=[set() for i in range(9)]
    vlines=[set() for i in range(9)]
    boxes=[[set() for i in range(3)] for j in range(3)]
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                todo.append([i,j])
            else:
                hlines[i].add(int(a[i][j]))
                vlines[j].add(int(a[i][j]))
                boxes[i//3][j//3].add(int(a[i][j]))
    return check(todo,hlines,vlines,boxes,a)

def clicked():
    btn.configure(fg='red')
    try:
        for i in range(9):
            for j in range(9):
                digit = txt[i][j].get().strip()
                if digit=='':
                    sudoku[i][j]=0
                    continue
                else:
                    sudoku[i][j]=int(digit)
        result=solve(sudoku)
        if result:
            error("Solution found!")
        else:
            error("Invalid  Puzzle")
    except:
        error("Invalid   input !")
            

root = Tk()
root.title("Sudoku Solver")
root.geometry('430x300')

lbl_1 = Label(root, text = "Puzzle", fg="blue")
lbl_1.place(x=79,y=190)

lbl_2 = Label(root, text = "Solution", fg="blue")
lbl_2.place(x=280,y=190)


txt = [[Entry(root, width=3) for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        txt[i][j].grid(row=i,column=j)

space = [Label(root, text = '     ') for i in range(9)]
for i in range(9):
    space[i].grid(row=i,column=j+9)

sdk = [[Label(root, text = '      ', borderwidth=1, relief="groove") for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        sdk[i][j].grid(row=i,column=j+30)

btn = Button(root, text = "Try", fg = "green", command = clicked)
btn.place(x=86,y=210)

root.mainloop()
