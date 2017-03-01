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
    
def a2d(size):
    a2d = [[False] * size for _ in range(size)]
    return a2d

def count_lighting(size, a):
    num = 0
    for i in range(0, size):
        for j in range(0, size):
            num += a[i][j]
    return num

def turn_on (x1, y1, x2, y2, a):
    for row in range (x1, x2 + 1):
        for col in range (y1, y2 + 1):
            a[row][col] = True    
    return

def turn_off (x1, y1, x2, y2, a):
    for row in range (x1, x2 + 1):
        for col in range (y1, y2 + 1):
            a[row][col] = False    
    return







