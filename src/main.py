import urllib.request
import argparse

'''parse the input'''
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()
filename = args.input

'''read the file'''
def read_url(filename):
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('UTF-8')
    else:
        return open(filename).read()

'''function that can make two-dimension list '''    
def a2d(size):
    matrix = [[False] * size for _ in range(size)]
    return matrix

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

'''the main code'''
def main():
    '''read the file from the input over command line '''
    buffer = read_url(filename)
    '''read a list of instructions in the input file'''
    lines = buffer.splitlines()
    '''get the size of the screen'''
    size = int(lines[0])
    print("Size is:",size)
    '''initialize every grid on screen to "False"'''
    square = a2d(size)
    '''read each instruction'''
    for instructions in lines[1:]:
        instruction = instructions.replace(',',' ').split()
        '''get coordinates'''
        if instruction[0] == "turn" and (len(instruction) == 7):
            x1 = (int) (instruction[2])
            y1 = (int) (instruction[3])
            x2 = (int) (instruction[5])
            y2 = (int) (instruction[6])
        elif instruction[0] == "switch" and (len(instruction) == 6):
            x1 = (int) (instruction[1])
            y1 = (int) (instruction[2])
            x2 = (int) (instruction[4])
            y2 = (int) (instruction[5])
        
        '''check if the coordinates out of the size'''    
        x1 = check_border(x1, size)
        y1 = check_border(y1, size)
        x2 = check_border(x2, size)
        y2 = check_border(y2, size)
        
        '''execute the instruction'''
        if instruction[0] == "turn" and (len(instruction) == 7):
            if instruction[1] == "on":
                turn_on(x1, y1, x2, y2, square)
            elif instruction[1] == "off":
                turn_off(x1, y1, x2, y2, square)
        elif instruction[0] == "switch" and (len(instruction) == 6):
            switch(x1, y1, x2, y2, square)
    '''print the number of lights that are on'''       
    print(count_lighting(size, square))
    return

main()



