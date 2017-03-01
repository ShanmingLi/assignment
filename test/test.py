from nose.tools import *
from src.main import *

def test_1():
    filename = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    buffer =read_url(filename)
    eq_(len(buffer), 9506, "buffer sizes do not match")
    
def test_a2d():
    result = [[False] * 4 for _ in range(4)]
    a = a2d(4)
    eq_(a, result, "Error with a2d function")

def test_count_lighting():
    a = a2d(4)
    count_lighting(4, a)
    eq_(count_lighting(4, a), 0, "Error with count_lighting function")
    
def test_turn_on():
    array = a2d(4)
    a1, b1, a2, b2 = 1, 1, 2, 2
    turn_on(a1, b1, a2, b2, array)
    count_lighting(4, array)
    eq_(count_lighting(4, array), 4, "Error with turn_on function")
    
def test_switch():
    array = [[True] * 4 for _ in range(4)]
    a1, b1, a2, b2 = 1, 1, 2, 2
    switch(a1, b1, a2, b2, array)
    count_lighting(4, array)
    eq_(count_lighting(4, array), 12, "Error with switch function")
    
def test_check_border1():
    size = 1000
    x = -169
    check_border(x, size)
    eq_(check_border(x, size), 0, "Error with check_border function")
    
def test_check_border2():
    size = 1000
    x = 1996
    check_border(x, size)
    eq_(check_border(x, size), 999, "Error with check_border function")    
    
    
    
    
    
    
    
    
    
    
    
    