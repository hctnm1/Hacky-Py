print('---Welcome to Hashmart---')
print('First create your account--')
name_1=input('Enter your name = ')
pass_1=int(input("enter your password="))
print('--Account created Successfully--')
name_2=input('Enter your login name = ')
pass_2=int(input("enter your login password="))
if name_1==name_2 and pass_1==pass_2:
    print('--Login successfully---')
else:
    c=1
    while c<3:
        c=c+1
        print('Login failed')
        print(c,'Try left')
        name_3=input('enter your login name = ')
        pass_3=int(input("enter your login pass ="))
        if name_1==name_3 and pass_1==pass_3:
            print('--Login successfully--')
            break
        else:
            print("Try again")
enter_1=input('if you want to continue shopping type yes ==')
if enter_1=='yes' :
    print('continue')
elif enter_1=='no':
    print('Thanks for shopping')
def Hashmart(location_1,location_2,location_3):
    infile_1=open(location_1,'r+')
    infile_2=open(location_2,'r+')
    infile_3=open(location_3,'r+')
    r_1=infile_1.read()
    r_2=infile_2.read()
    r_3=infile_3.read()
    print('* Bakery *')
    print(r_1)
    print('* Grocery *')
    print(r_2)
    print('* Freshers *')
    print(r_3)
    infile_1.close()
    infile_2.close()
    infile_3.close()
    #part2
    location_1='C:/Users/hashm/OneDrive/Desktop/Bakery.txt'
    infile_1=open(location_1)
    d_1={}
    for line_1 in infile_1:
        key,value = line_1.split()
        d_1[key] = value 
    location_2='C:/Users/hashm/OneDrive/Desktop/Grocery.txt'
    infile_2=open(location_2)
    d_2={}
    for line_2 in infile_2:
        key,value = line_2.split()
        d_2[key] = value 
    location_3='C:/Users/hashm/OneDrive/Desktop/Freshers.txt'
    infile_3=open(location_3)
    d_3={}
    for line_3 in infile_3:
        key,value = line_3.split()
        d_3[key] = value
    d={}
    d[1]=d_1
    d[2]=d_2
    d[3]=d_3
    #print(d)
    c=20
    while c>0:
        a=eval(input("Type 1-3 to enter in products sections = "))
        print(d[a])
        b=input("enter items name = ")
        c_1=d[a][b] 
        print(c_1)
        des={}
        for x,y in d.items():
            des[b]=c_1
        #print(des)
    
        infile_4=open('C:/Users/hashm/OneDrive/Desktop/Cart.txt','a')
        for key, value in des.items(): 
             infile_4.write( '%s %s\n'%(key,value))
        infile_4.close()
        d[a].pop(b)
        print(d[a])
        print("you want to continue or not")
        ask_1=input('yes or no = ')
        if ask_1=='yes':
            print('continue')
        else:
            break
    infile_5=open('C:/Users/hashm/OneDrive/Desktop/Cart.txt')
    cart={}
    for line_4 in infile_5:
        key,value=line_4.split()
        cart[key]=value
    print(cart)
    infile_5.close()
    
#dimagi code
location_1='C:/Users/hashm/OneDrive/Desktop/Bakery.txt'
location_2='C:/Users/hashm/OneDrive/Desktop/Grocery.txt'
location_3='C:/Users/hashm/OneDrive/Desktop/Freshers.txt'

x=Hashmart(location_1,location_2,location_3)
print(x)
[12:40 PM, 2/9/2022] Daniyal Uit: from datetime import date
def recipt(d):
    c=0
    while c<d:
        c=c+1
        user=input("name your name=")
        today = date.today()
        bt=input("enter burger type=")
        qy=int(input("enter quantity ="))
        ra=int(input("enter rate ="))     
        SUM=ra*qy
        GST=(SUM * 13)/100
        Netprice=SUM+GST
        print('    RECIPT     ')
        print('Customer=',user)
        print("Today's date:", today)
        print('Burger type is ',bt)
        print('The quantity of item is ',qy)
        print('The rate of item is',ra)
        print('The total sum is ',SUM)
        print('The GST on total amount is',GST)
        print('The Net price is ',Netprice)
        print('       ')
x=recipt(4)
print(x)
