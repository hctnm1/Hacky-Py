#Return the sum of all dividers of a given integer

n = int(input())

div = []
p = 2
while n > 1: 
	if n%p == 0:
		n = n/p
		div.append(p)
	else:
		p += 1
    
a = -1
exp = []
primef = []
for i in div:
    if i in primef:
        exp[a]+=1
    else:
        exp.append(0)
        a+=1
        exp[a]+=1
        primef.append(i)

s=1
for k in range(len(primef)):
    a = primef[k]
    b = exp[k]
    s *=((a**(b+1))-1)/(a-1)

print(int(s))
