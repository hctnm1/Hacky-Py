import turtle, keyboard
print('Press ESC to end the program')
print('Press SHIFT to change color')
def correct(x,y):
    ans=(x-y)*90
    if ans==270:
        ans=-90
    elif ans==-270:
        ans=90
    return ans
t = turtle.Turtle()
t.speed(10)
t.left(90)
x=0
angle=1
d=1
colors=['yellow','red','green','blue']
col=0
px,py=0,0
done=set()
t.fillcolor('yellow')
t.begin_fill()
while 1:
    if keyboard.is_pressed('up'):
        t.left(correct(d,1))
        t.forward(5)
        d=1
        done.add(str(px)+' '+str(py))
        py+=5
    elif keyboard.is_pressed('right'):
        t.left(correct(d,2))
        t.forward(5)
        d=2
        done.add(str(px)+' '+str(py))
        px+=5
    elif keyboard.is_pressed('down'):
        t.left(correct(d,3))
        t.forward(5)
        d=3
        done.add(str(px)+' '+str(py))
        py-=5
    elif keyboard.is_pressed('left'):
        t.left(correct(d,4))
        t.forward(5)
        d=4
        done.add(str(px)+' '+str(py))
        px-=5
    elif keyboard.is_pressed('esc'):
        break
    elif keyboard.is_pressed('shift'):
        col+=1
    if str(px)+' '+str(py) in done:
        t.end_fill()
        t.fillcolor(colors[col%4])
        t.begin_fill()
turtle.done()
