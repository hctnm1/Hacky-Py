# A program to find next 3 candidates of a sequence

def check(b):
    if len(b)<2:
        return
    if len(b)==2:
        if b[0]==b[1]:
            return b[0],b[0],b[0]
        return
    if len(set(b))==1:
        return b[0],b[0],b[0]
    y=b[len(b)-1]
    c=[]
    for i in range(len(b)-1):
        c.append(b[i]-b[i+1])
    x=check(c)
    if x!=None:
        return y-x[0],y-x[0]-x[1],y-x[0]-x[1]-x[2]
    if 0 not in b:
        c=[]
        for i in range(len(b)-1):
            c.append(b[i+1]/b[i])
        x=check(c)
        if x!=None:
            return y*x[0],y*x[0]*x[2],y*x[0]*x[1]*x[2]
print('''Enter a sequence and find the next 3 elements of this sequence.
Sample input: 1 4 7 10''')
a=[int(i) for i in input().split()]
x=check(a)
if x==None:
    print("Insufficient data! Add few more elements...")
else:
    print("Next 3 elements of the sequence are:",x[0],x[1],x[2],sep='   ')
