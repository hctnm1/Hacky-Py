def pigeonhole_sort(a):
    minimum = min(a)
    maximum = max(a)
    size = maximum - minimum + 1
    pigeonholes = [0] * size
    for i in a:
        pigeonholes[i - minimum] += 1
    j = 0
    for count in range(size):
        while pigeonholes[count] > 0:
            pigeonholes[count] -= 1
            a[j] = count + minimum
            j += 1
              
  
a = [12, 16, 19, 10,  9]
print("The array is :")
print(a)
print("Sorted array is :")
pigeonhole_sort(a)
print(a)
