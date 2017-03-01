import urllib.request

def read_url(filename):
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('UTF-8')
    else:
        return open(filename).read()

buffer = read_url("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")

lines = buffer.splitlines()

size = int(lines[0])
print("Size is:",size)

'''function that can make two-dimension list '''    
def a2d(size):
    a2d = [[False] * size for _ in range(size)]
    return a2d
'''function that count the number of True in the 2d list'''
def count_lighting(size, a):
    num = 0
    for i in range(0, size):
        for j in range(0, size):
            num += a[i][j]
    return num

'''function that change the specific element from False to True in the range'''
def turn_on (x1, y1, x2, y2, a):
    for row in range (x1, x2 + 1):
        for col in range (y1, y2 + 1):
            a[row][col] = True    
    return

'''function that change the specific element from True to False in the range'''
def turn_off (x1, y1, x2, y2, a):
    for row in range (x1, x2 + 1):
        for col in range (y1, y2 + 1):
            a[row][col] = False    
    return

'''function that switch the specific element's value in the range'''
def switch (x1, y1, x2, y2, a):
    for row in range (x1, x2 + 1):
        for col in range (y1, y2 + 1):
            if a[row][col]:
                a[row][col] = False
            else:
                a[row][col] = True  
    return

'''function that will check if the coordinates out index of the range'''
def check_border(n, size):
    if n < 0:
        n = max(0, n)
    elif n > size:
        n = min(size-1, n)
    else:
        n = n
    return n







