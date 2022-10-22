def oddOrEven():
    num = input().split()
    num = int(num)
    arr = list(num)
    odd = []
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
oddOrEven()
