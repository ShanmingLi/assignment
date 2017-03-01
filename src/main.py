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